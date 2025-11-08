from datetime import datetime
from enum import Enum
from typing import Optional

from dotenv import load_dotenv
from fastapi import APIRouter
from pydantic import BaseModel, Field

load_dotenv()

router = APIRouter(prefix="/apikey", tags=["analytics"])


class EnvironmentEnum(str, Enum):
    development = "development"
    staging = "staging"
    production = "production"


class RoleEnum(str, Enum):
    read = "read"
    write = "write"
    readwrite = "readwrite"
    admin = "admin"


class Tenant(BaseModel):
    name: str = Field(
        ...,
        example="My tenant",
        description="Name of the tenant",
        pattern=r"^[A-Za-z0-9\u3000 _-]+$",
        min_length=4,
        max_length=64
    )
    description: Optional[str] = Field(
        None,
        description="Description of the tenant",
        max_length=1024
    )
    environment: EnvironmentEnum = Field(
        default=EnvironmentEnum.development,
        description="Environments of the tenant",
        examples=[e.value for e in EnvironmentEnum]
    )
    stripe_customer_id: Optional[str] = Field(
        None,
        example=None,
        description="Stripe customer ID. Paying individuals in Stayforge follows Tenants."
    )
    metadata: Optional[dict] = Field(
        {}, description="Metadata of the tenant"
    )


class TenantMembership(BaseModel):
    member_sub: str = Field(
        ...,
        description="Member sub from auth0"
    )
    tenant_id: str = Field(
        ...,
        description="Tenant ID"
    )
    role: RoleEnum = Field(
        ...,
        description="Role of the member",
        examples=[e.value for e in RoleEnum]

    )
    owner: bool = Field(
        False,
        description="Whether the member is the owner of the tenant"
    )
