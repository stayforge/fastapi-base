import logging

from bson import ObjectId
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Query, Form

from src.db import tenant_membership_collection, tenant_collection
from src.models.tenant import Tenant, TenantMembership, RoleEnum, EnvironmentEnum

load_dotenv()

router = APIRouter(prefix="/tenant", tags=["tenants"])
logger = logging.getLogger(__name__)


@router.get("/data/environment")
def get_environment_enum():
    return [e.value for e in EnvironmentEnum]


@router.get("/data/role")
def get_role_enum():
    return [e.value for e in RoleEnum]


@router.get("/list")
async def list_tenants(
        member_sub: str = Query(..., description="member_sub"),
):
    result = []
    try:
        # 查詢與 member_sub 關聯的所有記錄
        members = list(tenant_membership_collection.find({"member_sub": member_sub}))

        if not members:
            # 日誌打印給開發者調試
            print(f"[ERROR] No members found for member_sub: {member_sub}")
            # 返回提供給前端或用戶的錯誤信息
            raise HTTPException(status_code=404, detail=f"No tenants found for member_sub: {member_sub}")

        # 處理記錄
        for member in members:
            try:
                tenant_id = member.get("tenant_id")
                if not tenant_id:
                    continue

                tenant_id = ObjectId(tenant_id)
                tenant = tenant_collection.find_one({"_id": tenant_id})
                tenant["_id"] = str(tenant["_id"])

                members_cursor = tenant_membership_collection.find({"tenant_id": str(tenant_id)})
                members = []

                for _member in members_cursor:
                    _member["_id"] = str(_member["_id"]) if "_id" in _member else None
                    _member["tenant_id"] = str(_member["tenant_id"])
                    members.append(_member)

                result.append({
                    "id": str(tenant_id),
                    "tenant": tenant,
                    "members": members
                })

            except Exception as e:
                logger.error(f"[ERROR] Failed to process member document: {member}. Error: {e}")

        return result

    except Exception as e:
        # 捕捉整個方法執行中的未知錯誤
        print(f"[CRITICAL] Unexpected error during tenant listing for member_sub {member_sub}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error occurred while listing tenants.")


@router.post("/create")
async def create_tenant(
        current_user_sub: str,
        tenant: Tenant,
):
    new_tenant = tenant_collection.insert_one(tenant.model_dump())
    tenant_id = str(new_tenant.inserted_id)

    tenant_membership_collection.insert_one(
        TenantMembership(
            tenant_id=tenant_id,
            member_sub=current_user_sub,
            role=RoleEnum.admin,
            owner=True,
        ).model_dump()  # 轉換為字典
    )

    result: dict = Tenant(**tenant_collection.find_one({"_id": new_tenant.inserted_id})).model_dump()
    result["_id"] = tenant_id
    return result


@router.get("/{tenant_id}")
async def get_tenant(
        tenant_id: str,
        member_sub: str
):
    # Check if user is a member of this tenant
    membership = tenant_membership_collection.find_one({
        "member_sub": member_sub,
        "tenant_id": tenant_id
    })

    # If user is not a member, deny access
    if not membership:
        raise HTTPException(
            status_code=403,
            detail="You are not authorized to view this tenant"
        )

    # Execute query
    try:
        # Fetch tenant document
        tenant = tenant_collection.find_one({"_id": ObjectId(tenant_id)})

        if not tenant:
            raise HTTPException(
                status_code=404,
                detail=f"Tenant with id {tenant_id} not found."
            )

        # Convert ObjectId to string for JSON compatibility
        tenant["_id"] = str(tenant["_id"])

        # Fetch members and serialize their ObjectId values
        members = []
        for member in tenant_membership_collection.find({"tenant_id": tenant_id}):
            member["_id"] = str(member.get("_id"))  # Serialize member ObjectId
            member["tenant_id"] = str(member.get("tenant_id"))  # Serialize tenant_id
            members.append(TenantMembership(**member))

        return {
            "id": tenant_id,
            "tenant": tenant,
            "members": members,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database query failed: {str(e)}"
        )


@router.delete("/{tenant_id}")
async def delete_tenant(
        tenant_id: str,
        member_sub: str
):
    # Check if user is a member of this tenant
    membership = tenant_membership_collection.find_one({
        "member_sub": member_sub,
        "tenant_id": tenant_id
    })
    if not membership:
        raise HTTPException(
            status_code=403,
            detail="You are not authorized to delete this tenant, or it does not exist."
        )
    tenant_collection.delete_one({"_id": ObjectId(tenant_id)})
    tenant_membership_collection.delete_many({"tenant_id": tenant_id})

    return {
        "id": tenant_id,
        "deleted": True,
    }


@router.get("/{tenant_id}/members")
async def get_tenant_members(
        tenant_id: str,
        member_sub: str
):
    # Check if user is a member of this tenant
    membership = tenant_membership_collection.find_one({
        "member_sub": member_sub,
        "tenant_id": tenant_id
    })

    # If user is not a member, deny access
    if not membership:
        raise HTTPException(
            status_code=403,
            detail="You are not authorized to view this tenant's members"
        )

    # Get all members
    try:
        members = []
        for member in tenant_membership_collection.find({"tenant_id": tenant_id}):
            members.append(TenantMembership(**member))

        return members
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database query failed: {str(e)}"
        )


@router.post("/{tenant_id}/invite/member")
async def add_member(
        tenant_id: str,
        email: str = Form(..., description="Email address of the member"),
):
    return email
