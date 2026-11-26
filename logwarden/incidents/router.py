from uuid import UUID
from fastapi import APIRouter, Query, Response
from starlette.status import HTTP_201_CREATED
from logwarden.incidents.dependencies import IncidentServiceDependency

from logwarden.incidents.schemas import IncidentCreate, IncidentResponse, IncidentUpdate

router = APIRouter(prefix="/incidents", tags=["incidents"])

@router.post("",
             response_model=IncidentResponse,
             status_code=HTTP_201_CREATED)
async def create_incident(
        incident: IncidentCreate,
        service: IncidentServiceDependency,
):
    return await service.create(incident)

@router.get("/{incident_id}",
            response_model=IncidentResponse)
async def get_incident(
        incident_id: UUID,
        service: IncidentServiceDependency,
):
    return await service.get_by_id(incident_id)

@router.get("",
            response_model=list[IncidentResponse])
async def get_incidents(
        service: IncidentServiceDependency,
        limit: int = Query(default=20, ge=1, le=100),
        offset: int = Query(default=0, ge=0),
):
    return await service.get_incidents(
        limit=limit,
        offset=offset)


@router.patch("/{incident_id}",
              response_model=IncidentResponse)
async def update_incident(
        incident_id: UUID,
        data: IncidentUpdate,
        service: IncidentServiceDependency):
    return await service.update(
        incident_id = incident_id,
        data = data,
    )

@router.delete("/{incident_id}",
               status_code=204,
               response_class=Response)
async def delete_incident(
        incident_id: UUID,
        service: IncidentServiceDependency
) -> Response:
    await service.delete_incident(incident_id)

    return Response (
        status_code=204,
    )
