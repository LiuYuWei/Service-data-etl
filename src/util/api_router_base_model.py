"""Define fastapi input variable type."""
# import relation package.
from pydantic import BaseModel

# import project package.


class HealthCheckBaseModel(BaseModel):
    """The input of change direction"""
    service: str
    status: str
    version: str
