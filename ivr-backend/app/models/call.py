"""Call database model."""

from sqlalchemy import Column, DateTime, Integer, String, func

from app.db.base import Base


class Call(Base):
    """SQLAlchemy model for call records."""

    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True)
    call_sid = Column(String(34), unique=True, index=True, nullable=False)
    caller_number = Column(String(15), nullable=False)
    to_number = Column(String(15), nullable=False)
    status = Column(String(20), nullable=False, default="received")
    routed_dialer = Column(String(50), nullable=True)
    routed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
