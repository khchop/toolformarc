"""Twilio webhook endpoints."""

import logging
import time
import traceback
import uuid
from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Form, Request, Response
from pydantic import ValidationError

from app.core.twilio_service import generate_twiml_routing
from app.schemas.webhook_schemas import TwilioWebhookData
from app.services.routing_service import make_routing_decision, redact_phone_number

router = APIRouter()

logger = logging.getLogger(__name__)


async def save_call_and_routing_background(
    call_sid: str,
    caller_number: str,
    to_number: str,
    routed_dialer: str,
    max_retries: int = 3,
) -> None:
    """Background task to save call record and update routing atomically.

    This combines call creation and routing update to avoid race conditions.
    Includes retry logic for transient failures.

    Args:
        call_sid: Twilio call SID.
        caller_number: Caller's phone number.
        to_number: Twilio phone number receiving the call.
        routed_dialer: Target dialer name.
        max_retries: Maximum number of retry attempts.
    """
    import asyncio

    from app.repositories.call_repository import create_call, update_call_routing

    retry_count = 0
    last_error = None

    while retry_count <= max_retries:
        try:
            # Create call record first
            await create_call(
                call_sid=call_sid,
                caller_number=caller_number,
                to_number=to_number
            )

            # Then update with routing decision
            await update_call_routing(
                call_sid=call_sid,
                routed_dialer=routed_dialer,
            )

            logger.info(
                {
                    "event": "call.saved_and_routed",
                    "call_sid": call_sid,
                    "routed_dialer": routed_dialer,
                    "retry_count": retry_count,
                }
            )
            return  # Success!

        except Exception as e:
            last_error = e
            retry_count += 1

            if retry_count <= max_retries:
                wait_time = 2 ** retry_count  # Exponential backoff: 2, 4, 8 seconds
                logger.warning(
                    {
                        "event": "call.save_retry",
                        "error_type": type(e).__name__,
                        "error_message": str(e),
                        "call_sid": call_sid,
                        "retry_count": retry_count,
                        "wait_time": wait_time,
                    }
                )
                await asyncio.sleep(wait_time)
            else:
                logger.error(
                    {
                        "error_type": "DatabaseError",
                        "error_message": (
                            f"Failed to save call after {max_retries} retries: "
                            f"{str(last_error)}"
                        ),
                        "call_sid": call_sid,
                    }
                )


@router.post("/webhooks/twilio")
async def twilio_webhook(
    request: Request,
    background_tasks: BackgroundTasks,
    CallSid: Annotated[str, Form()],
    From: Annotated[str, Form()],
    To: Annotated[str, Form()],
) -> Response:
    """Handle incoming Twilio call webhooks.

    Args:
        request: FastAPI request object.
        background_tasks: Background tasks for async operations.
        CallSid: Twilio call SID.
        From: Caller phone number.
        To: Twilio phone number receiving the call.

    Returns:
        Response: TwiML XML response.
    """
    request_id = str(uuid.uuid4())
    start_time = time.time()

    try:
        webhook_data = TwilioWebhookData(CallSid=CallSid, From=From, To=To)

        # Make routing decision
        routing_decision = make_routing_decision(
            caller_number=webhook_data.From,
            request_id=request_id,
        )

        # Generate TwiML with target dialer phone number
        twiml_response = generate_twiml_routing(routing_decision.target_phone)
        response_time_ms = (time.time() - start_time) * 1000

        # Log successful request with structured JSON (PII redacted)
        logger.info(
            {
                "request_id": request_id,
                "event": "webhook.received",
                "call_sid": webhook_data.CallSid,
                "caller_number": redact_phone_number(webhook_data.From),
                "to_number": redact_phone_number(webhook_data.To),
                "routed_dialer": routing_decision.target_dialer,
                "target_phone": redact_phone_number(routing_decision.target_phone),
                "response_time_ms": response_time_ms,
                "status": "success",
            }
        )

        # Save call record and routing decision atomically in background
        background_tasks.add_task(
            save_call_and_routing_background,
            call_sid=webhook_data.CallSid,
            caller_number=webhook_data.From,
            to_number=webhook_data.To,
            routed_dialer=routing_decision.target_dialer,
        )

        return Response(
            content=twiml_response,
            media_type="application/xml",
        )

    except ValidationError as e:
        response_time_ms = (time.time() - start_time) * 1000
        logger.error(
            {
                "request_id": request_id,
                "error_type": "ValidationError",
                "error_message": str(e),
                "path": "/webhooks/twilio",
                "response_time_ms": response_time_ms,
            }
        )

        error_content = (
            '{"error": {"type": "ValidationError", '
            f'"message": "Invalid request data", "request_id": "{request_id}"}}'
        )

        return Response(
            content=error_content,
            status_code=400,
            media_type="application/json",
        )

    except Exception as e:
        response_time_ms = (time.time() - start_time) * 1000
        logger.error(
            {
                "request_id": request_id,
                "error_type": "InternalServerError",
                "error_message": str(e),
                "traceback": traceback.format_exc(),
                "path": "/webhooks/twilio",
                "response_time_ms": response_time_ms,
            }
        )

        error_content = (
            '{"error": {"type": "InternalServerError", '
            f'"message": "An unexpected error occurred", "request_id": "{request_id}"}}'
        )

        return Response(
            content=error_content,
            status_code=500,
            media_type="application/json",
        )
