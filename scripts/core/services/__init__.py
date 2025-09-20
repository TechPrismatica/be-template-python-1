from fastapi import APIRouter

from scripts.core.services import v1

base_router = APIRouter(prefix="/api")

base_router.include_router(v1.v1_router)
