from typing import Annotated

from fastapi import Depends

from logwarden.incidents.service import IncidentService


def get_incident_service() -> IncidentService:
    return IncidentService()


IncidentServiceDependency = Annotated[
    IncidentService,
    Depends(get_incident_service),
]
