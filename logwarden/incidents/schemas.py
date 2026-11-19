from pydantic import BaseModel

class IncidentCreate(BaseModel):
    service_name: str
    description: str
    error_code: int


class IncidentResponse(BaseModel):
    id: int
    service_name: str
    description: str
    error_code: int

