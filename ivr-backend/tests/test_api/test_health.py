"""Tests for the health check endpoint."""

from fastapi.testclient import TestClient

from app.main import app


def test_import_app():
    """Test that the main app module can be imported."""
    assert app is not None


def test_app_has_title():
    """Test that the app has a title."""
    assert app.title == "IVR Backend"


def test_health_endpoint_exists():
    """Test that health endpoint returns 200 OK."""
    client = TestClient(app)
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
