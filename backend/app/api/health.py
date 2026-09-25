"""
Health Check Endpoint

Provides a simple health check endpoint for monitoring service availability.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        dict: Status of the API service
        
    Example:
        GET /api/health
        
        Response:
        {
            "status": "ok"
        }
    """
    return {"status": "ok"}
