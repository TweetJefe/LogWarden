from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED
from logwarden.incidents.dependencies import IncidentServiceDependency

from logwarden.incidents.schemas import IncidentCreate, IncidentResponse

router = APIRouter(prefix="/incidents", tags=["incidents"])

@router.post("",
             response_model=IncidentResponse,
             status_code=HTTP_201_CREATED)
def create_incident(
        incident: IncidentCreate,
        service: IncidentServiceDependency,
):
    return service.create(incident)

@router.get("/{incident_id}")
def get_incident(incident_id: int):
    return {"incidents": incident_id}

