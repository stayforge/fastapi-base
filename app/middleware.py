import os

from dotenv import load_dotenv
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

load_dotenv()


class APIKeyMiddleware(BaseHTTPMiddleware):
    """
    Middleware to validate API Key for all routes except /health
    API Key should be provided in the request header as 'X-API-Key'
    """

    def __init__(self, app, excluded_paths: list[str] = None):
        super().__init__(app)
        # Paths that don't require API Key authentication
        self.excluded_paths = excluded_paths or ["/health"]
        # Get API Key from environment variable
        self.authorization = os.getenv("AUTHORIZATION")

        if not self.authorization:
            raise ValueError("AUTHORIZATION environment variable is not set")

    async def dispatch(self, request: Request, call_next):
        # Check if the path should be excluded from AUTHORIZATION validation
        if request.url.path in self.excluded_paths:
            return await call_next(request)

        # Get AUTHORIZATION from request header
        request_authorization = request.headers.get("Authorization")

        # Validate AUTHORIZATION
        if not request_authorization:
            return JSONResponse(
                status_code=444,
                content={"detail": "444"}
            )

        if request_authorization != self.authorization:
            return JSONResponse(
                status_code=403,
                content={"detail": "Invalid AUTHORIZATION"}
            )

        # AUTHORIZATION is valid, proceed with the request
        response = await call_next(request)
        return response
