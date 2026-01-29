"""Health check endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    """Health check endpoint.

    Returns:
        dict: Health status indicating the application is running.
    """
    return {"status": "healthy"}
