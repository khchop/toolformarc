"""Add routing fields to calls table.

Revision ID: 002
Revises: 001_create_calls_table
Create Date: 2026-01-29 13:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001_create_calls_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add routed_dialer and routed_at columns to calls table."""
    op.add_column('calls', sa.Column('routed_dialer', sa.String(50), nullable=True))
    op.add_column('calls', sa.Column('routed_at', sa.DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    """Remove routed_dialer and routed_at columns from calls table."""
    op.drop_column('calls', 'routed_at')
    op.drop_column('calls', 'routed_dialer')
