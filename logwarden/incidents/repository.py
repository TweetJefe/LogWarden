from logwarden.incidents.schemas import IncidentCreate, IncidentResponse


class IncidentRepository:
    def create(self, incident: IncidentCreate) -> IncidentResponse:
        return IncidentResponse(
            service_name=incident.service_name,
            description=incident.description,
            error_code=incident.error_code,
            id=1
        )
