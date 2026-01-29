"""Tests for call repository database operations."""

from datetime import datetime, timezone

import pytest

from app.repositories.call_repository import (
    create_call,
    get_call_by_sid,
    update_call_routing,
)


@pytest.mark.asyncio
async def test_create_call():
    """Test creating a new call record."""
    call_sid = f"CA_test_{int(datetime.now(timezone.utc).timestamp() * 1000)}"
    caller_number = "+15551234567"
    to_number = "+15559876543"

    call = await create_call(
        call_sid=call_sid,
        caller_number=caller_number,
        to_number=to_number
    )

    assert call is not None
    assert call.call_sid == call_sid
    assert call.caller_number == caller_number
    assert call.to_number == to_number
    assert call.status == "received"
    assert call.routed_dialer is None
    assert call.routed_at is None


@pytest.mark.asyncio
async def test_get_call_by_sid():
    """Test retrieving a call by SID."""
    call_sid = f"CA_test_{int(datetime.now(timezone.utc).timestamp() * 1000)}"

    # Create a call
    await create_call(
        call_sid=call_sid,
        caller_number="+15551234567",
        to_number="+15559876543"
    )

    # Retrieve it
    call = await get_call_by_sid(call_sid)

    assert call is not None
    assert call.call_sid == call_sid


@pytest.mark.asyncio
async def test_get_call_by_sid_not_found():
    """Test retrieving a non-existent call returns None."""
    call = await get_call_by_sid("CA_nonexistent")
    assert call is None


@pytest.mark.asyncio
async def test_update_call_routing():
    """Test updating call record with routing decision."""
    call_sid = f"CA_test_{int(datetime.now(timezone.utc).timestamp() * 1000)}"

    # Create a call first
    await create_call(
        call_sid=call_sid,
        caller_number="+15551234567",
        to_number="+15559876543"
    )

    # Update with routing decision
    updated_call = await update_call_routing(
        call_sid=call_sid,
        routed_dialer="dialfire"
    )

    assert updated_call is not None
    assert updated_call.routed_dialer == "dialfire"
    assert updated_call.status == "routed"
    assert updated_call.routed_at is not None
    assert isinstance(updated_call.routed_at, datetime)


@pytest.mark.asyncio
async def test_update_call_routing_not_found():
    """Test updating non-existent call returns None and logs warning."""
    result = await update_call_routing(
        call_sid="CA_nonexistent",
        routed_dialer="dialfire"
    )

    assert result is None


@pytest.mark.asyncio
async def test_update_call_routing_changes_status():
    """Test that routing update changes status from received to routed."""
    call_sid = f"CA_test_{int(datetime.now(timezone.utc).timestamp() * 1000)}"

    # Create call with default status
    call = await create_call(
        call_sid=call_sid,
        caller_number="+15551234567",
        to_number="+15559876543"
    )
    assert call.status == "received"

    # Update routing
    updated_call = await update_call_routing(
        call_sid=call_sid,
        routed_dialer="dialfire"
    )

    assert updated_call.status == "routed"
    assert updated_call.status != call.status
