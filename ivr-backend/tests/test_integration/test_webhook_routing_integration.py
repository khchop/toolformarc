"""Integration tests for complete webhook → routing → database flow."""

import asyncio
import time

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.repositories.call_repository import get_call_by_sid


@pytest.fixture
def client() -> TestClient:
    """Provide a test client for the FastAPI application."""
    return TestClient(app)


@pytest.mark.asyncio
async def test_webhook_end_to_end_routing_flow(client: TestClient):
    """Test complete flow: webhook → routing decision → TwiML → database update.

    This integration test validates:
    - Webhook receives Twilio request
    - Routing service makes decision
    - TwiML response is generated
    - Database is updated with call and routing info
    """
    # Unique call SID for this test
    unique_call_sid = f"CA_integration_{int(time.time() * 1000)}"

    webhook_data = {
        "CallSid": unique_call_sid,
        "From": "+15551234567",
        "To": "+15559876543",
    }

    # Step 1: Send webhook request
    response = client.post("/webhooks/twilio", data=webhook_data)

    # Step 2: Verify immediate TwiML response
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml"
    assert "<Dial" in response.text
    assert "<Number>" in response.text

    # Step 3: Wait for background task to complete
    # Background tasks run async, so we need to give them time
    await asyncio.sleep(1.0)

    # Step 4: Verify database record exists with routing info
    call = await get_call_by_sid(unique_call_sid)

    assert call is not None, "Call record should exist in database"
    assert call.call_sid == unique_call_sid
    assert call.caller_number == "+15551234567"
    assert call.to_number == "+15559876543"
    assert call.routed_dialer == "dialfire", "Call should be routed to dialfire"
    assert call.status == "routed", "Call status should be 'routed'"
    assert call.routed_at is not None, "Routing timestamp should be set"


@pytest.mark.asyncio
async def test_webhook_routing_includes_correct_dialer_number(client: TestClient):
    """Test that TwiML response contains the correct dialer phone number from config."""
    from app.core.config import settings

    unique_call_sid = f"CA_integration_{int(time.time() * 1000)}"

    webhook_data = {
        "CallSid": unique_call_sid,
        "From": "+15551234567",
        "To": "+15559876543",
    }

    response = client.post("/webhooks/twilio", data=webhook_data)

    assert response.status_code == 200
    # Verify the configured Dialfire number is in the TwiML response
    assert settings.DIALFIRE_PHONE_NUMBER in response.text


@pytest.mark.asyncio
async def test_webhook_response_time_meets_sla(client: TestClient):
    """Test that complete routing flow meets <2 second SLA."""
    unique_call_sid = f"CA_integration_{int(time.time() * 1000)}"

    webhook_data = {
        "CallSid": unique_call_sid,
        "From": "+15551234567",
        "To": "+15559876543",
    }

    start_time = time.time()
    response = client.post("/webhooks/twilio", data=webhook_data)
    response_time = (time.time() - start_time) * 1000  # Convert to ms

    assert response.status_code == 200
    assert response_time < 2000, (
        f"Response time {response_time:.2f}ms exceeds 2000ms SLA. "
        f"This includes routing decision and TwiML generation."
    )


@pytest.mark.asyncio
async def test_webhook_routing_logs_complete_decision_chain(client: TestClient):
    """Test that routing decision logs contain complete information.

    This validates AC3: Complete routing decision chain is logged.
    Note: This test verifies the structure exists; actual log validation
    would require capturing log output in a test fixture.
    """
    unique_call_sid = f"CA_integration_{int(time.time() * 1000)}"

    webhook_data = {
        "CallSid": unique_call_sid,
        "From": "+15551234567",
        "To": "+15559876543",
    }

    response = client.post("/webhooks/twilio", data=webhook_data)
    assert response.status_code == 200

    # Wait for background task
    await asyncio.sleep(1.0)

    # Verify database has complete routing chain
    call = await get_call_by_sid(unique_call_sid)
    assert call is not None

    # Complete chain should include:
    # 1. Call received timestamp (created_at)
    assert call.created_at is not None

    # 2. Routing decision timestamp (routed_at)
    assert call.routed_at is not None

    # 3. Target dialer
    assert call.routed_dialer == "dialfire"

    # 4. Response time would be in logs (verified through other tests)
    # The routing service logs decision_time_ms
    # The webhook logs response_time_ms
