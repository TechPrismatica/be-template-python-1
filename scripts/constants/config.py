from pydantic import Field
from pydantic_settings import BaseSettings

PROJECT_NAME = "example"


class _Services(BaseSettings):
    MODULE_NAME: str = Field(default=PROJECT_NAME)
    POST: int = Field(default=7999, validation_alias="service_port")
    HOST: str = Field(default="0.0.0.0", validation_alias="service_host")


Services = _Services()

__all__ = ["Services"]
