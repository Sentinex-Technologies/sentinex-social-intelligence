"""
Sentiment Analysis API endpoints - Component B
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.services.sentiment_analyzer import SentimentAnalyzer

router = APIRouter()


@router.post("/analyze-text")
async def analyze_text(text: str):
    """
    Analyze sentiment and emotions in arbitrary text.
    
    **Component B:** Multi-dimensional sentiment inference.
    
    Returns:
    - sentiment_score: -1 (negative) to +1 (positive)
    - sentiment_label: positive/negative/neutral
    - emotions: sarcasm, anxiety, excitement, supportive, against
    - subjectivity: 0 (objective) to 1 (subjective)
    """
    analyzer = SentimentAnalyzer()
    result = analyzer.analyze_text(text)
    
    return {
        "status": "success",
        "analysis": result
    }


@router.post("/analyze-posts")
async def analyze_posts(
    limit: Optional[int] = Query(default=None, description="Max posts to analyze"),
    db: Session = Depends(get_db)
):
    """
    Analyze sentiment for all posts without sentiment data.
    
    This updates the database with sentiment scores and emotions.
    """
    analyzer = SentimentAnalyzer()
    count = analyzer.analyze_all_posts(db, limit=limit)
    
    return {
        "status": "success",
        "posts_analyzed": count,
        "message": f"Analyzed {count} posts successfully"
    }


@router.get("/trends")
async def get_sentiment_trends(
    days_back: int = Query(default=30, ge=1, le=365),
    platform: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Get sentiment trends over time.
    
    **Component B:** Track sentiment fluctuations over time.
    
    Shows how public sentiment changes day by day.
    """
    analyzer = SentimentAnalyzer()
    trends = analyzer.get_sentiment_trends(db, days_back=days_back, platform=platform)
    
    return {
        "status": "success",
        "days_back": days_back,
        "platform": platform or "all",
        "trends": trends
    }


@router.get("/emotions")
async def get_emotion_distribution(
    days_back: int = Query(default=7, ge=1, le=365),
    platform: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Get emotion distribution across posts.
    
    **Component B:** Multi-dimensional emotion detection.
    
    Returns average scores for:
    - Sarcasm
    - Anxiety
    - Excitement
    - Supportive
    - Against
    """
    analyzer = SentimentAnalyzer()
    emotions = analyzer.get_emotion_distribution(db, days_back=days_back, platform=platform)
    
    return {
        "status": "success",
        "days_back": days_back,
        "platform": platform or "all",
        "emotion_distribution": emotions
    }
