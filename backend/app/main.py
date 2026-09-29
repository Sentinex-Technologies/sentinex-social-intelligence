"""
Sentinex Social Intelligence API - Main Application

FastAPI application entry point for the Sentinex backend.
Implements NTRO SIH26152 Problem Statement requirements.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.health import router as health_router
from app.api.data import router as data_router
from app.api.network import router as network_router
from app.api.posts import router as posts_router
from app.api.sentiment import router as sentiment_router
from app.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler - runs on startup and shutdown.
    """
    # Startup: Initialize database
    print("🚀 Initializing database...")
    init_db()
    print("✅ Database initialized successfully")
    
    yield
    
    # Shutdown: Cleanup if needed
    print("👋 Shutting down...")


# Create FastAPI application
app = FastAPI(
    title="Sentinex Social Intelligence API",
    description=(
        "AI-powered social media analytics platform for SIH26152 (NTRO)\n\n"
        "**Components Implemented:**\n"
        "- Component A: Multi-platform data collection with timeline management\n"
        "- Component B: Multi-dimensional sentiment analysis (Phase 3)\n"
        "- Component C: Demographic profiling and aggregation\n"
        "- Component D: Real-time trend and topic detection\n"
        "- Component E: Network topology and link analysis\n\n"
        "**Legal & Ethical:**\n"
        "- 100% synthetic demo data\n"
        "- No ToS violations\n"
        "- Privacy-compliant\n"
        "- Hackathon-ready prototype"
    ),
    version="0.3.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan
)

# Configure CORS
# Allow both local development and production GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "https://sentinex-technologies.github.io",  # GitHub Pages
        "https://*.onrender.com",  # Render preview deployments
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router, prefix="/api", tags=["Health"])
app.include_router(data_router, prefix="/api/data", tags=["Data Management"])
app.include_router(network_router, prefix="/api/network", tags=["Network Analysis (Component E)"])
app.include_router(posts_router, prefix="/api/posts", tags=["Posts & Analytics (Components A, D)"])
app.include_router(sentiment_router, prefix="/api/sentiment", tags=["Sentiment Analysis (Component B)"])


@app.get("/")
async def root():
    """Root endpoint - API information."""
    return {
        "message": "Sentinex Social Intelligence API",
        "version": "0.2.0",
        "status": "operational",
        "docs": "/api/docs",
        "components": {
            "A": "Multi-platform Data Collection",
            "B": "Multi-Dimensional Sentiment (Phase 3)",
            "C": "Demographic Profiling",
            "D": "Trend & Topic Detection",
            "E": "Network Topology Analysis"
        }
    }
