from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import create_db
from app.api.incidents import router as incident_router
from app.api.dashboard import router as dashboard_router

app = FastAPI(
    title="IncidentOps API",
    version="1.0.0",
    description="Internal Incident Management Platform for SRE Teams",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
def startup():
    create_db()


app.include_router(incident_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {
        "application": "IncidentOps",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}    