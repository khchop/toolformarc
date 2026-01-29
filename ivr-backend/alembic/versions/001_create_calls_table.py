"""Create calls table for tracking inbound calls.

Revision ID: 001
Revises:
Create Date: 2026-01-29
"""


import sqlalchemy as sa

from alembic import op


def upgrade() -> None:
    """Create calls table."""
    op.create_table(
        "calls",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("call_sid", sa.String(34), nullable=False),
        sa.Column("caller_number", sa.String(15), nullable=False),
        sa.Column("to_number", sa.String(15), nullable=False),
        sa.Column("status", sa.String(20), nullable=False, default="received"),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("NOW()"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_calls_id"), "calls", ["id"], unique=False)
    op.create_index(
        op.f("ix_calls_call_sid"), "calls", ["call_sid"], unique=True
    )


def downgrade() -> None:
    """Drop calls table."""
    op.drop_index(op.f("ix_calls_call_sid"), table_name="calls")
    op.drop_index(op.f("ix_calls_id"), table_name="calls")
    op.drop_table("calls")
