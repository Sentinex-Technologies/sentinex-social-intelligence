"""
Sentinex Social Intelligence API - Main Application

FastAPI application entry point for the Sentinex backend.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router

# Create FastAPI application
app = FastAPI(
    title="Sentinex Social Intelligence API",
    description="AI-powered social media analytics platform for SIH26152",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router, prefix="/api", tags=["Health"])


@app.get("/")
async def root():
    """Root endpoint - API information."""
    return {
        "message": "Sentinex Social Intelligence API",
        "version": "0.1.0",
        "status": "operational",
        "docs": "/api/docs",
    }
