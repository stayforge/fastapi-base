"""Timing middleware for performance monitoring."""

import logging
import time
from typing import Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class TimingMiddleware(BaseHTTPMiddleware):
    """Middleware to measure request processing time."""

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """Process the request and measure time."""
        start_time = time.time()

        # Process request
        response = await call_next(request)

        # Calculate processing time
        process_time = time.time() - start_time

        # Add timing header
        response.headers["X-Process-Time"] = str(process_time)

        # Log slow requests (> 1 second)
        if process_time > 1.0:
            logger.warning(
                f"Slow request detected",
                extra={
                    "method": request.method,
                    "url": str(request.url),
                    "process_time": process_time,
                },
            )

        return response

