from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict, model_validator


class IncidentCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    service_name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=2000)
    error_code: int = Field(ge=400, le=599)


class IncidentResponse(BaseModel):
    id: UUID
    service_name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=2000)
    error_code: int = Field(ge=400, le=599)
    created_at: datetime
    updated_at: datetime



class IncidentUpdate(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    service_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    description: str | None = Field(
        default=None,
        min_length=1,
        max_length=2000,
    )
    error_code: int | None = Field(
        default=None,
        ge=400,
        le=599,
    )

    @model_validator(mode="after")
    def reject_explicit_nulls(self) -> "IncidentUpdate":
        for field_name in self.model_fields_set:
            if getattr(self, field_name) is None:
                raise ValueError(
                    f"Field '{field_name}' cannot be null"
                )

        return self
