from typing import Any
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from logwarden.incidents.models import Incident


class IncidentRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, incident: Incident) -> Incident:
        self.session.add(incident)
        await self.session.flush()
        return incident

    async def delete(self, incident: Incident) -> None:
        await self.session.delete(incident)
        await self.session.flush()

    async def get_incident_by_id(self, incident_id: UUID) -> Incident | None:
        return await self.session.get(Incident, incident_id)

    async def get_incidents(self, offset: int, limit: int) -> list[Incident]:
        statement = (
            select(Incident)
            .order_by(
                Incident.created_at.desc(),
                Incident.id.desc())
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(statement)
        return list(result.scalars().all())

    async def update(
            self,
            incident: Incident,
            changes: dict[str, Any]
    ) -> Incident:
        for field_name, value in changes.items():
            setattr(incident, field_name, value)

        await self.session.flush()
        await self.session.refresh(incident)
        return incident
