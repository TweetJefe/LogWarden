from fastapi import Request
from fastapi.responses import JSONResponse

from logwarden.incidents.exceptions import IncidentNotFoundError


async def incident_not_found_handler(
    request: Request,
    exc: IncidentNotFoundError,
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )
