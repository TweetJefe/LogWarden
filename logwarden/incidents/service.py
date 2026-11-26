from uuid import UUID

from logwarden.incidents.exceptions import IncidentNotFoundError
from logwarden.incidents.models import Incident
from logwarden.incidents.repository import IncidentRepository
from logwarden.incidents.schemas import IncidentCreate, IncidentResponse, IncidentUpdate


class IncidentService:

    def __init__(self, repository: IncidentRepository):
        self.repository = repository

    async def create(self, incident: IncidentCreate) -> IncidentResponse:
        entity = Incident(
            service_name = incident.service_name,
            description = incident.description,
            error_code = incident.error_code
        )

        async with self.repository.session.begin():
            created = await self.repository.create(entity)

        return IncidentResponse.model_validate(
            created,
            from_attributes=True
        )

    async def get_by_id(self, incident_id: UUID) -> IncidentResponse:
        async with self.repository.session.begin():
            entity = await self.repository.get_incident_by_id(incident_id)
            if entity is None:
                raise IncidentNotFoundError(incident_id)
            return IncidentResponse.model_validate(
                entity,
                from_attributes=True
            )

    async def get_incidents(
            self,
            limit: int,
            offset: int,
    ) -> list[IncidentResponse]:
        entities = await self.repository.get_incidents(
            limit=limit,
            offset=offset,
        )

        return [
            IncidentResponse.model_validate(
                entity,
                from_attributes=True
            )
            for entity in entities
        ]

    async def update(
            self,
            data: IncidentUpdate,
            incident_id: UUID,
    ) -> IncidentResponse:
        async with self.repository.session.begin():
            entity = await self.repository.get_incident_by_id(incident_id)

            if entity is None:
                raise IncidentNotFoundError(incident_id)

            changes = data.model_dump(exclude_unset=True)

            updated = await self.repository.update(
                incident = entity,
                changes = changes
            )

            response = IncidentResponse.model_validate(
                updated,
                from_attributes=True
            )
            return response

    async def delete_incident(self, incident_id: UUID) -> None:
        async with self.repository.session.begin():
            entity = await self.repository.get_incident_by_id(incident_id)
            if entity is None:
                raise IncidentNotFoundError(incident_id)
            await self.repository.delete(entity)
