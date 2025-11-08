import os

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from uvicorn.server import logger

from app.middleware import APIKeyMiddleware
from app.routes import router
from src.db.mongodb import MongoDBConnector
from src.get_public_ip import get_public_ip

load_dotenv()
# Initialize FastAPI app
app = FastAPI(
    title="Stayforge Auth Server",
    description="Stayforge Auth Server",
    docs_url="/swagger",
    redoc_url="/docs",
)

# Add AUTHORIZATION middleware
app.add_middleware(APIKeyMiddleware, excluded_paths=["/health"])


@app.get("/")
async def root():
    # Root endpoint returns basic service information
    return RedirectResponse("./docs")


@app.get("/health")
async def health_check():
    # Health check endpoint for monitoring
    db = MongoDBConnector(uri=os.getenv("MONGODB_URI"), database="api_analytics")
    did_ping = db.ping()
    return {"status": "healthy", "mongodb": did_ping}


app.include_router(router)

try:
    logger.info(f"Public IP address: {get_public_ip()}")
except TimeoutError:
    logger.error("Failed to get public IP address")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
