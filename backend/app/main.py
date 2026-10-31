"""
SignSetu FastAPI Main Entrypoint.
SHARED INTEGRATION FILE: Aggregates routers and middleware for all modules.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

# Router imports
from app.routers import doctor
from app.routers import patient
from app.routers import motion
from app.routers import isl

app = FastAPI(
    title="SignSetu Backend",
    description="Offline-first healthcare communication assistant for deaf and non-speaking patients.",
    version="0.1.0"
)

# CORS configuration for offline local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Shared Healthcheck
@app.get("/api/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "offline_mode": True,
        "ollama_target": settings.OLLAMA_BASE_URL,
        "model": settings.OLLAMA_MODEL
    }

# Router Aggregation
app.include_router(doctor.router)
app.include_router(patient.router)
app.include_router(motion.router)
app.include_router(isl.router)
