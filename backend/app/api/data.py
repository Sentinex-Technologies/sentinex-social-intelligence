"""
Data API endpoints - Synthetic data generation and management.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.services.synthetic_data import SyntheticDataGenerator
from app.models.social_post import SocialPost
from app.models.user import User

router = APIRouter()


@router.post("/generate")
async def generate_synthetic_data(
    num_users: int = 100,
    num_posts: int = 1000,
    days_back: int = 30,
    seed: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """
    Generate synthetic social media data for demonstration.
    
    This endpoint creates:
    - Synthetic user profiles with demographics
    - Network relationships (followers/following)
    - Social media posts across platforms
    - Engagement events
    
    **Legal & Ethical:**
    - 100% synthetic data
    - No real user information
    - No ToS violations
    - Perfect for hackathon demo
    
    **Query Parameters:**
    - num_users: Number of users to generate (default: 100)
    - num_posts: Number of posts to generate (default: 1000)
    - days_back: Historical timespan in days (default: 30)
    - seed: Random seed for reproducibility (optional)
    """
    try:
        generator = SyntheticDataGenerator(seed=seed)
        result = generator.generate_complete_dataset(
            db=db,
            num_users=num_users,
            num_posts=num_posts,
            days_back=days_back
        )
        
        return {
            "status": "success",
            "message": "Synthetic data generated successfully",
            "data": {
                "users_created": len(result["users"]),
                "posts_created": len(result["posts"]),
                "relationships_created": len(result["relationships"]),
                "engagements_created": len(result["engagements"])
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Data generation failed: {str(e)}")


@router.get("/stats")
async def get_data_statistics(db: Session = Depends(get_db)):
    """
    Get overall data statistics.
    
    Returns counts and distributions across the dataset.
    """
    from sqlalchemy import func
    
    # Query statistics
    total_users = db.query(User).count()
    total_posts = db.query(SocialPost).count()
    
    # Platform distribution
    platform_dist = db.query(
        SocialPost.platform,
        func.count(SocialPost.id)
    ).group_by(SocialPost.platform).all()
    
    # Sentiment distribution
    sentiment_dist = db.query(
        SocialPost.sentiment_label,
        func.count(SocialPost.id)
    ).group_by(SocialPost.sentiment_label).all()
    
    # Average engagement
    avg_engagement = db.query(
        func.avg(SocialPost.likes_count).label('avg_likes'),
        func.avg(SocialPost.shares_count).label('avg_shares'),
        func.avg(SocialPost.comments_count).label('avg_comments')
    ).first()
    
    return {
        "total_users": total_users,
        "total_posts": total_posts,
        "platform_distribution": dict(platform_dist),
        "sentiment_distribution": dict(sentiment_dist),
        "average_engagement": {
            "likes": float(avg_engagement.avg_likes or 0),
            "shares": float(avg_engagement.avg_shares or 0),
            "comments": float(avg_engagement.avg_comments or 0)
        }
    }


@router.delete("/clear")
async def clear_all_data(
    confirm: str = None,
    db: Session = Depends(get_db)
):
    """
    Clear all data from the database.
    
    **WARNING:** This is destructive and cannot be undone.
    
    **Query Parameters:**
    - confirm: Must be "YES_DELETE_ALL" to proceed
    """
    if confirm != "YES_DELETE_ALL":
        raise HTTPException(
            status_code=400,
            detail="Confirmation required. Set confirm=YES_DELETE_ALL"
        )
    
    try:
        # Delete in correct order (due to foreign key constraints)
        from app.models.engagement import Engagement
        from app.models.user import UserRelationship
        
        db.query(Engagement).delete()
        db.query(SocialPost).delete()
        db.query(UserRelationship).delete()
        db.query(User).delete()
        db.commit()
        
        return {
            "status": "success",
            "message": "All data cleared successfully"
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to clear data: {str(e)}")
