from typing import Optional

from pydantic import BaseModel


class IncidentCreate(BaseModel):

    title: str
    description: str
    severity: str
    service: str


class IncidentUpdate(BaseModel):

    title: Optional[str] = None
    description: Optional[str] = None
    severity: Optional[str] = None
    service: Optional[str] = None
    status: Optional[str] = None