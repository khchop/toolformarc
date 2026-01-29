"""Routing decision service for IVR system."""

import logging
import re
import time
from dataclasses import dataclass

from app.core.config import settings

logger = logging.getLogger(__name__)

# E.164 phone number validation pattern (basic)
PHONE_NUMBER_PATTERN = re.compile(r'^\+?[1-9]\d{1,14}$')


def redact_phone_number(phone: str) -> str:
    """Redact phone number for logging (show last 4 digits only).

    Args:
        phone: Phone number to redact.

    Returns:
        Redacted phone number (e.g., "***1234").
    """
    if len(phone) <= 4:
        return "***"
    return "***" + phone[-4:]


@dataclass
class RoutingDecision:
    """Result of a routing decision."""

    target_dialer: str
    target_phone: str
    decision_time_ms: float


def make_routing_decision(
    caller_number: str,
    request_id: str = "",
) -> RoutingDecision:
    """Make a routing decision for an incoming call.

    For MVP, this returns a simple hardcoded routing to Dialfire.
    Future iterations will support Braze customer lookup and rule-based routing.

    Args:
        caller_number: The caller's phone number (E.164 format expected).
        request_id: Request ID for logging correlation.

    Returns:
        RoutingDecision containing target dialer and phone number.

    Raises:
        ValueError: If caller_number is not a valid phone number format.
    """
    start_time = time.time()

    # Validate phone number format
    if not PHONE_NUMBER_PATTERN.match(caller_number):
        logger.warning(
            {
                "request_id": request_id,
                "event": "routing.invalid_phone",
                "caller_number": caller_number,
            }
        )
        raise ValueError(f"Invalid phone number format: {caller_number}")

    # MVP: Simple hardcoded routing to Dialfire
    target_dialer = "dialfire"
    target_phone = settings.DIALFIRE_PHONE_NUMBER

    decision_time_ms = (time.time() - start_time) * 1000

    # Log the routing decision (with PII redaction)
    logger.info(
        {
            "request_id": request_id,
            "event": "routing.decision",
            "caller_number": redact_phone_number(caller_number),
            "target_dialer": target_dialer,
            "target_phone": redact_phone_number(target_phone),
            "decision_time_ms": decision_time_ms,
        }
    )

    return RoutingDecision(
        target_dialer=target_dialer,
        target_phone=target_phone,
        decision_time_ms=decision_time_ms,
    )
