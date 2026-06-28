from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Incident(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)

    title: str

    description: str

    severity: str

    service: str

    status: str = "OPEN"

    priority: str = "P3"

    owner_team: str = "Platform Team"

    created_at: datetime = Field(default_factory=datetime.utcnow)