import random
import string
from datetime import datetime, timezone

from pydantic import BaseModel, Field


def generate_apikey() -> str:
    characters = string.ascii_letters + string.digits
    return f"sf_key_{''.join(random.choice(characters) for _ in range(48))}"


class APIKeyInput(BaseModel):
    name: str = Field(f"Create at {datetime.now().date().isoformat()}", description="Name of the API key")
    tenant_id: str = Field(..., description="Tenant ID")


class APIKeyInDB(APIKeyInput):
    api_key_hash: str = Field(..., description="Hashed API key")
    created_at: datetime = Field(datetime.now(timezone.utc), description="Creation time")
