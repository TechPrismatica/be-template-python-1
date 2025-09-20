from jetpack.errors.exception_handlers import get_exception_handlers

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from scripts.core.services import base_router

app = FastAPI(
    title="Data Services: PG",
    description="PG Data Services API",
    version="0.1.0",
    root_path="/data-services-pg",
    exception_handlers=get_exception_handlers(),
    default_response_class=ORJSONResponse,
)

app.include_router(base_router)
