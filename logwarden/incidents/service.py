
from logwarden.incidents.repository import IncidentRepository
from logwarden.incidents.schemas import IncidentCreate, IncidentResponse

class IncidentService:

    def __init__(self, repository: IncidentRepository):
        self.repository = repository

    def create(self,incident: IncidentCreate) -> IncidentResponse:
        return self.repository.create(incident)
