from uuid import UUID


class IncidentNotFoundError(Exception):
    def __init__(self, incident_id: UUID):
        self.incident_id = incident_id
        super().__init__("Incident not found")
