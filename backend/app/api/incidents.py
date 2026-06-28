from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database.database import get_session
from app.database.models import Incident
from app.schemas.incident import IncidentCreate, IncidentUpdate
from app.services.incident_service import (
    calculate_priority,
    assign_team,
)

router = APIRouter(prefix="/incidents", tags=["Incidents"])


@router.post("/")
def create_incident(
    incident: IncidentCreate,
    session: Session = Depends(get_session),
):

    db_incident = Incident(
        **incident.model_dump(),
        priority=calculate_priority(incident.severity),
        owner_team=assign_team(incident.service),
    )

    session.add(db_incident)
    session.commit()
    session.refresh(db_incident)

    return db_incident


@router.get("/")
def list_incidents(
    status: str | None = None,
    severity: str | None = None,
    service: str | None = None,
    priority: str | None = None,
    session: Session = Depends(get_session),
):

    statement = select(Incident)

    if status:
        statement = statement.where(Incident.status == status)

    if severity:
        statement = statement.where(Incident.severity == severity)

    if service:
        statement = statement.where(Incident.service == service)

    if priority:
        statement = statement.where(Incident.priority == priority)

    return session.exec(statement).all()


@router.get("/{incident_id}")
def get_incident(
    incident_id: int,
    session: Session = Depends(get_session),
):

    incident = session.get(Incident, incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    return incident


@router.put("/{incident_id}")
def update_incident(
    incident_id: int,
    update: IncidentUpdate,
    session: Session = Depends(get_session),
):

    incident = session.get(Incident, incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    data = update.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(incident, key, value)

    if "severity" in data:
        incident.priority = calculate_priority(incident.severity)

    if "service" in data:
        incident.owner_team = assign_team(incident.service)

    session.add(incident)
    session.commit()
    session.refresh(incident)

    return incident


@router.put("/{incident_id}/resolve")
def resolve_incident(
    incident_id: int,
    session: Session = Depends(get_session),
):

    incident = session.get(Incident, incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    incident.status = "RESOLVED"

    session.add(incident)
    session.commit()
    session.refresh(incident)

    return incident

@router.delete("/{incident_id}")
def delete_incident(
    incident_id: int,
    session: Session = Depends(get_session),
):

    incident = session.get(Incident, incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    session.delete(incident)
    session.commit()

    return {
        "message": "Incident deleted successfully"
    }