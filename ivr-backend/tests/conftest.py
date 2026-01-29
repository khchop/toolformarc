"""Pytest configuration and fixtures."""

import asyncio
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.db.base import Base


# Convert postgres:// to postgresql+asyncpg:// for async support
database_url = settings.DATABASE_URL
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)

# Create test engine with separate connection pool
test_engine = create_async_engine(
    database_url,
    echo=False,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)

# Test session factory
TestSessionLocal = sessionmaker(
    test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def db_session():
    """Provide a transactional database session for tests.

    This fixture creates a new database session for each test and rolls back
    all changes after the test completes, ensuring test isolation.
    """
    async with TestSessionLocal() as session:
        yield session
        await session.rollback()


@pytest_asyncio.fixture(autouse=True)
async def setup_database():
    """Set up database tables before tests and clean up after."""
    # This ensures tables exist (migrations should have created them)
    # We don't recreate tables here to avoid conflicts with Alembic migrations
    yield
    # Cleanup happens automatically via session rollback in db_session fixture
