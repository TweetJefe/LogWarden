from fastapi import FastAPI

from logwarden.api.router import api_router
from logwarden.incidents.exception_handlers import incident_not_found_handler
from logwarden.incidents.exceptions import IncidentNotFoundError

app = FastAPI()

app.add_exception_handler(IncidentNotFoundError, incident_not_found_handler)

app.include_router(api_router)
