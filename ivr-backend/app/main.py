"""FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.health import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    yield


app = FastAPI(
    title="IVR Backend",
    description="IVR Call Routing System Backend",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router, prefix="/api/v1", tags=["health"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
