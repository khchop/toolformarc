"""Call repository for database operations."""

import logging
from datetime import datetime, timezone

from sqlalchemy import select

from app.db.session import async_session_factory
from app.models.call import Call

logger = logging.getLogger(__name__)


async def create_call(call_sid: str, caller_number: str, to_number: str) -> Call:
    """Create a new call record.

    Args:
        call_sid: Twilio call SID.
        caller_number: Caller's phone number.
        to_number: Twilio phone number receiving the call.

    Returns:
        The created Call instance.
    """
    async with async_session_factory() as session:
        call = Call(
            call_sid=call_sid,
            caller_number=caller_number,
            to_number=to_number
        )
        session.add(call)
        await session.commit()
        await session.refresh(call)
        return call


async def get_call_by_sid(call_sid: str) -> Call | None:
    """Retrieve a call by its Twilio SID.

    Args:
        call_sid: Twilio call SID.

    Returns:
        The Call instance if found, None otherwise.
    """
    async with async_session_factory() as session:
        result = await session.execute(
            select(Call).where(Call.call_sid == call_sid)
        )
        return result.scalar_one_or_none()


async def update_call_routing(
    call_sid: str,
    routed_dialer: str,
) -> Call | None:
    """Update a call record with routing decision.

    Args:
        call_sid: Twilio call SID.
        routed_dialer: Target dialer name ('dialfire', 'zendesk_talk', etc).

    Returns:
        The updated Call instance if found, None otherwise.
    """
    async with async_session_factory() as session:
        # Query for the call
        result = await session.execute(
            select(Call).where(Call.call_sid == call_sid)
        )
        call = result.scalar_one_or_none()

        if not call:
            logger.warning(
                {
                    "event": "routing.update_failed",
                    "call_sid": call_sid,
                    "reason": "call_not_found",
                }
            )
            return None

        # Update routing fields
        call.routed_dialer = routed_dialer
        call.status = "routed"
        call.routed_at = datetime.now(timezone.utc)

        session.add(call)
        await session.commit()
        await session.refresh(call)

        logger.info(
            {
                "event": "routing.updated",
                "call_sid": call_sid,
                "routed_dialer": routed_dialer,
                "routed_at": call.routed_at.isoformat() if call.routed_at else None,
            }
        )

        return call
