"""Tests for Twilio webhook endpoints."""

import time
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    """Provide a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def mock_background_task():
    """Mock the background task for saving call records and routing."""
    with patch(
        "app.api.webhooks.save_call_and_routing_background", new_callable=AsyncMock
    ) as mock:
        yield mock


class TestTwilioWebhookEndpoint:
    """Test suite for Twilio webhook endpoint."""

    def test_twilio_webhook_returns_twiml_response(
        self, client: TestClient, mock_background_task
    ):
        """Test that valid Twilio webhook returns TwiML response with Dial verb."""
        unique_call_sid = f"CA{int(time.time() * 1000)}"
        webhook_data = {
            "CallSid": unique_call_sid,
            "From": "+15551234567",
            "To": "+15559876543",
        }

        response = client.post("/webhooks/twilio", data=webhook_data)

        assert response.status_code == 200
        assert response.headers["content-type"] == "application/xml"
        assert "<Response>" in response.text
        assert "<Dial" in response.text  # Contains Dial verb with attributes

    def test_twilio_webhook_requires_all_fields(self, client: TestClient):
        """Test that webhook requires CallSid, From, and To fields."""
        incomplete_data = {"CallSid": "CA1234567890", "From": "+15551234567"}

        response = client.post("/webhooks/twilio", data=incomplete_data)

        assert response.status_code == 422

    def test_twilio_webhook_returns_error_for_empty_call_sid(
        self, client: TestClient
    ):
        """Test that empty CallSid returns validation error."""
        invalid_data = {
            "CallSid": "",
            "From": "+15551234567",
            "To": "+15559876543",
        }

        response = client.post("/webhooks/twilio", data=invalid_data)

        assert response.status_code == 422


class TestTwiMLGeneration:
    """Test suite for TwiML generation."""

    def test_twiml_response_contains_dial_verb(
        self, client: TestClient, mock_background_task
    ):
        """Test that generated TwiML contains Dial verb for routing."""
        unique_call_sid = f"CA{int(time.time() * 1000)}"
        webhook_data = {
            "CallSid": unique_call_sid,
            "From": "+15551234567",
            "To": "+15559876543",
        }

        response = client.post("/webhooks/twilio", data=webhook_data)

        assert response.status_code == 200
        response_text = response.text
        assert "<Response>" in response_text
        assert "<Dial" in response_text

    def test_twiml_response_contains_number_element(
        self, client: TestClient, mock_background_task
    ):
        """Test that generated TwiML contains Number element for dialer."""
        unique_call_sid = f"CA{int(time.time() * 1000)}"
        webhook_data = {
            "CallSid": unique_call_sid,
            "From": "+15551234567",
            "To": "+15559876543",
        }

        response = client.post("/webhooks/twilio", data=webhook_data)

        assert response.status_code == 200
        assert "<Number>" in response.text


class TestErrorHandling:
    """Test suite for error handling in webhook endpoint."""

    def test_missing_field_returns_422(self, client: TestClient):
        """Test that missing fields return 422 validation error."""
        incomplete_data = {"From": "+15551234567", "To": "+15559876543"}

        response = client.post("/webhooks/twilio", data=incomplete_data)

        assert response.status_code == 422

    def test_validation_error_returns_json(self, client: TestClient):
        """Test that validation errors return JSON response."""
        invalid_data = {
            "CallSid": "",
            "From": "+15551234567",
            "To": "+15559876543",
        }

        response = client.post("/webhooks/twilio", data=invalid_data)

        assert response.status_code == 422
        assert response.headers["content-type"] == "application/json"


class TestRouting:
    """Test suite for routing functionality."""

    def test_webhook_calls_routing_service(
        self, client: TestClient, mock_background_task
    ):
        """Test that webhook integrates with routing service."""
        with patch(
            "app.api.webhooks.make_routing_decision"
        ) as mock_routing:
            from app.services.routing_service import RoutingDecision
            mock_routing.return_value = RoutingDecision(
                target_dialer="dialfire",
                target_phone="+15559999999",
                decision_time_ms=10.0,
            )

            unique_call_sid = f"CA{int(time.time() * 1000)}"
            webhook_data = {
                "CallSid": unique_call_sid,
                "From": "+15551234567",
                "To": "+15559876543",
            }

            response = client.post("/webhooks/twilio", data=webhook_data)

            assert response.status_code == 200
            mock_routing.assert_called_once()

    def test_twiml_response_contains_routed_number(
        self, client: TestClient, mock_background_task
    ):
        """Test that TwiML response contains the routed dialer number."""
        from app.core.config import settings

        unique_call_sid = f"CA{int(time.time() * 1000)}"
        webhook_data = {
            "CallSid": unique_call_sid,
            "From": "+15551234567",
            "To": "+15559876543",
        }

        response = client.post("/webhooks/twilio", data=webhook_data)

        assert response.status_code == 200
        # Response should contain the Dialfire phone number from config
        assert settings.DIALFIRE_PHONE_NUMBER in response.text


class TestPerformance:
    """Test suite for performance requirements."""

    def test_response_time_under_2_seconds(self, client: TestClient, mock_background_task):
        """Test that webhook responds within 2 seconds (SLA requirement)."""
        unique_call_sid = f"CA{int(time.time() * 1000)}"
        webhook_data = {
            "CallSid": unique_call_sid,
            "From": "+15551234567",
            "To": "+15559876543",
        }

        start_time = time.time()
        response = client.post("/webhooks/twilio", data=webhook_data)
        end_time = time.time()

        response_time_ms = (end_time - start_time) * 1000

        assert response.status_code == 200
        assert response_time_ms < 2000, (
            f"Response time {response_time_ms:.2f}ms exceeds 2000ms SLA"
        )
