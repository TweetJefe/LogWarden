from typing import Annotated
from fastapi import Depends

from logwarden.db.dependencies import SessionDependency
from logwarden.incidents.repository import IncidentRepository
from logwarden.incidents.service import IncidentService


def get_incident_repository(
        session: SessionDependency
) -> IncidentRepository:
    return IncidentRepository(session=session)


IncidentRepositoryDependency = Annotated[
    IncidentRepository,
    Depends(get_incident_repository),
]


def get_incident_service(
    repository: IncidentRepositoryDependency,
) -> IncidentService:
    return IncidentService(repository=repository)


IncidentServiceDependency = Annotated[
    IncidentService,
    Depends(get_incident_service),
]
