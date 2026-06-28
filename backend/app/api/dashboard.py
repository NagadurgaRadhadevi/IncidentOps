from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.database.database import get_session
from app.database.models import Incident

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/")
def dashboard(session: Session = Depends(get_session)):

    incidents = session.exec(select(Incident)).all()

    return {
        "total_incidents": len(incidents),
        "open": sum(1 for i in incidents if i.status == "OPEN"),
        "resolved": sum(1 for i in incidents if i.status == "RESOLVED"),
        "critical": sum(1 for i in incidents if i.severity.lower() == "critical"),
        "high": sum(1 for i in incidents if i.severity.lower() == "high"),
        "medium": sum(1 for i in incidents if i.severity.lower() == "medium"),
        "low": sum(1 for i in incidents if i.severity.lower() == "low"),
    }