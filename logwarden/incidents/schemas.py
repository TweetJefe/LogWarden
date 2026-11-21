from pydantic import BaseModel, Field, ConfigDict

class IncidentCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    service_name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=2000)
    error_code: int = Field(ge=400, le=599)


class IncidentResponse(BaseModel):
    id: int
    service_name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=2000)
    error_code: int = Field(ge=400, le=599)

