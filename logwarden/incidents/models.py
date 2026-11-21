from uuid import UUID

from sqlalchemy import Uuid, text, String, Integer, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from logwarden.db.base import Base


class Incident(Base):
    __tablename__ = 'incidents'

    __table_args__ = (
        CheckConstraint(
            "error_code >= 400 AND error_code <= 599",
            name = "ck_incidents_error_code_range",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=text("uuidv7()"),
    )

    service_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(2000),
        nullable=False,
    )

    error_code: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

