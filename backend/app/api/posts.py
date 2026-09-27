"""
Posts API endpoints - Social media post retrieval and analysis.
Implements Component A, B, D requirements.
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from typing import Optional, List
from datetime import datetime, timedelta

from app.database import get_db
from app.models.social_post import SocialPost
from app.models.user import User

router = APIRouter()


@router.get("/")
async def get_posts(
    platform: Optional[str] = None,
    sentiment: Optional[str] = None,
    limit: int = Query(default=50, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
    order_by: str = Query(default="created_at", regex="^(created_at|likes_count|trending_score)$"),
    db: Session = Depends(get_db)
):
    """
    Retrieve social media posts with filtering and pagination.
    
    **Component A:** Time-stamped chronological database retrieval.
    
    **Query Parameters:**
    - platform: Filter by platform (twitter, telegram, instagram, etc.)
    - sentiment: Filter by sentiment (positive, negative, neutral, mixed)
    - limit: Number of posts to return (1-500)
    - offset: Pagination offset
    - order_by: Sort field (created_at, likes_count, trending_score)
    """
    query = db.query(SocialPost)
    
    # Apply filters
    if platform:
        query = query.filter(SocialPost.platform == platform)
    if sentiment:
        query = query.filter(SocialPost.sentiment_label == sentiment)
    
    # Apply ordering
    if order_by == "created_at":
        query = query.order_by(desc(SocialPost.created_at))
    elif order_by == "likes_count":
        query = query.order_by(desc(SocialPost.likes_count))
    elif order_by == "trending_score":
        query = query.order_by(desc(SocialPost.trending_score))
    
    # Apply pagination
    total_count = query.count()
    posts = query.offset(offset).limit(limit).all()
    
    # Format response
    posts_data = []
    for post in posts:
        posts_data.append({
            "id": post.id,
            "platform": post.platform,
            "author_id": post.author_id,
            "content_text": post.content_text[:200] + "..." if len(post.content_text or "") > 200 else post.content_text,
            "created_at": post.created_at.isoformat(),
            "likes_count": post.likes_count,
            "shares_count": post.shares_count,
            "comments_count": post.comments_count,
            "views_count": post.views_count,
            "sentiment_score": post.sentiment_score,
            "sentiment_label": post.sentiment_label,
            "topics": post.topics,
            "hashtags": post.hashtags,
            "trending_score": post.trending_score,
            "location": post.location
        })
    
    return {
        "status": "success",
        "total_count": total_count,
        "returned_count": len(posts_data),
        "offset": offset,
        "limit": limit,
        "posts": posts_data
    }


# NOTE: This route is commented out to avoid conflicts with specific routes below.
# In production, move this to the END of the file, after all specific routes.
# @router.get("/{post_id}")
# async def get_post_detail(
#     post_id: int,
#     db: Session = Depends(get_db)
# ):
#     """
#     Get detailed information about a specific post.
#     
#     Includes full content, author details, and engagement data.
#     """
#     post = db.query(SocialPost).filter(SocialPost.id == post_id).first()
#     
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#     
#     # Get author details
#     author = db.query(User).filter(User.id == post.author_id).first()
#     
#     return {
#         "status": "success",
#         "post": {
#             "id": post.id,
#             "platform": post.platform,
#             "platform_post_id": post.platform_post_id,
#             "author": {
#                 "id": author.id,
#                 "username": author.username,
#                 "followers_count": author.followers_count,
#                 "influence_score": author.influence_score
#             } if author else None,
#             "content_text": post.content_text,
#             "content_type": post.content_type,
#             "language": post.language,
#             "created_at": post.created_at.isoformat(),
#             "likes_count": post.likes_count,
#             "shares_count": post.shares_count,
#             "comments_count": post.comments_count,
#             "views_count": post.views_count,
#             "sentiment_score": post.sentiment_score,
#             "sentiment_label": post.sentiment_label,
#             "emotions": post.emotions,
#             "topics": post.topics,
#             "hashtags": post.hashtags,
#             "trending_score": post.trending_score,
#             "location": post.location,
#             "geo_coordinates": post.geo_coordinates,
#             "is_repost": post.is_repost,
#             "data_source": post.data_source
#         }
#     }


@router.get("/timeline/distribution")
async def get_timeline_distribution(
    platform: Optional[str] = None,
    days_back: int = Query(default=30, ge=1, le=365),
    interval: str = Query(default="day", regex="^(hour|day|week)$"),
    db: Session = Depends(get_db)
):
    """
    Get post distribution over time (Component A: Timeline Management).
    
    Shows how post volume changes over time, useful for:
    - Identifying viral moments
    - Detecting trend emergence
    - Understanding posting patterns
    
    **Query Parameters:**
    - platform: Filter by platform
    - days_back: Historical period to analyze (1-365 days)
    - interval: Time granularity (hour, day, week)
    """
    from sqlalchemy import extract, cast, Date
    
    start_date = datetime.utcnow() - timedelta(days=days_back)
    query = db.query(SocialPost).filter(SocialPost.created_at >= start_date)
    
    if platform:
        query = query.filter(SocialPost.platform == platform)
    
    # Group by time interval
    if interval == "day":
        results = query.with_entities(
            cast(SocialPost.created_at, Date).label('date'),
            func.count(SocialPost.id).label('count')
        ).group_by(cast(SocialPost.created_at, Date)).all()
        
        timeline = [{"date": str(date), "count": count} for date, count in results]
    
    elif interval == "hour":
        results = query.with_entities(
            func.date_trunc('hour', SocialPost.created_at).label('hour'),
            func.count(SocialPost.id).label('count')
        ).group_by(func.date_trunc('hour', SocialPost.created_at)).all()
        
        timeline = [{"hour": hour.isoformat(), "count": count} for hour, count in results]
    
    else:  # week
        results = query.with_entities(
            func.date_trunc('week', SocialPost.created_at).label('week'),
            func.count(SocialPost.id).label('count')
        ).group_by(func.date_trunc('week', SocialPost.created_at)).all()
        
        timeline = [{"week": week.isoformat(), "count": count} for week, count in results]
    
    return {
        "status": "success",
        "interval": interval,
        "days_back": days_back,
        "timeline": timeline
    }


@router.get("/sentiment/distribution")
async def get_sentiment_distribution(
    platform: Optional[str] = None,
    days_back: int = Query(default=30, ge=1, le=365),
    db: Session = Depends(get_db)
):
    """
    Get sentiment distribution over time (Component B: Multi-Dimensional Sentiment).
    
    Shows how sentiment fluctuates over time, identifying:
    - Sentiment shifts
    - Positive/negative trends
    - Emotional patterns
    
    **Query Parameters:**
    - platform: Filter by platform
    - days_back: Historical period (1-365 days)
    """
    from sqlalchemy import cast, Date
    
    start_date = datetime.utcnow() - timedelta(days=days_back)
    query = db.query(SocialPost).filter(SocialPost.created_at >= start_date)
    
    if platform:
        query = query.filter(SocialPost.platform == platform)
    
    # Overall sentiment distribution
    sentiment_counts = query.with_entities(
        SocialPost.sentiment_label,
        func.count(SocialPost.id)
    ).group_by(SocialPost.sentiment_label).all()
    
    # Sentiment over time (daily)
    sentiment_timeline = query.with_entities(
        cast(SocialPost.created_at, Date).label('date'),
        SocialPost.sentiment_label,
        func.count(SocialPost.id).label('count')
    ).group_by(
        cast(SocialPost.created_at, Date),
        SocialPost.sentiment_label
    ).all()
    
    # Average sentiment score over time
    avg_sentiment_timeline = query.with_entities(
        cast(SocialPost.created_at, Date).label('date'),
        func.avg(SocialPost.sentiment_score).label('avg_sentiment')
    ).group_by(cast(SocialPost.created_at, Date)).all()
    
    return {
        "status": "success",
        "sentiment_distribution": dict(sentiment_counts),
        "sentiment_timeline": [
            {"date": str(date), "sentiment": sentiment, "count": count}
            for date, sentiment, count in sentiment_timeline
        ],
        "average_sentiment_timeline": [
            {"date": str(date), "avg_sentiment": float(avg_sentiment or 0)}
            for date, avg_sentiment in avg_sentiment_timeline
        ]
    }


@router.get("/trending")
async def get_trending_posts(
    platform: Optional[str] = None,
    hours_back: int = Query(default=24, ge=1, le=168),
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Get trending posts (Component D: Trend & Topic Detection).
    
    Identifies viral content based on:
    - Engagement rate
    - Trending score
    - Recency
    
    **Query Parameters:**
    - platform: Filter by platform
    - hours_back: Time window (1-168 hours = 1 week)
    - limit: Number of trending posts (1-100)
    """
    start_time = datetime.utcnow() - timedelta(hours=hours_back)
    query = db.query(SocialPost).filter(SocialPost.created_at >= start_time)
    
    if platform:
        query = query.filter(SocialPost.platform == platform)
    
    # Order by trending score and engagement
    trending_posts = query.order_by(
        desc(SocialPost.trending_score),
        desc(SocialPost.likes_count)
    ).limit(limit).all()
    
    posts_data = []
    for post in trending_posts:
        author = db.query(User).filter(User.id == post.author_id).first()
        posts_data.append({
            "id": post.id,
            "platform": post.platform,
            "author_username": author.username if author else None,
            "content_text": post.content_text[:200] + "..." if len(post.content_text or "") > 200 else post.content_text,
            "created_at": post.created_at.isoformat(),
            "likes_count": post.likes_count,
            "shares_count": post.shares_count,
            "comments_count": post.comments_count,
            "trending_score": post.trending_score,
            "topics": post.topics,
            "hashtags": post.hashtags
        })
    
    return {
        "status": "success",
        "hours_back": hours_back,
        "trending_posts": posts_data
    }


@router.get("/topics")
async def get_trending_topics(
    platform: Optional[str] = None,
    days_back: int = Query(default=7, ge=1, le=30),
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Get trending topics and hashtags (Component D: Topic Detection).
    
    Analyzes:
    - Most frequent topics
    - Emerging hashtags
    - Topic popularity trends
    
    **Query Parameters:**
    - platform: Filter by platform
    - days_back: Time window (1-30 days)
    - limit: Number of topics to return (1-100)
    """
    from collections import Counter
    
    start_date = datetime.utcnow() - timedelta(days=days_back)
    query = db.query(SocialPost).filter(SocialPost.created_at >= start_date)
    
    if platform:
        query = query.filter(SocialPost.platform == platform)
    
    posts = query.all()
    
    # Count topics
    all_topics = []
    all_hashtags = []
    
    for post in posts:
        if post.topics:
            all_topics.extend(post.topics)
        if post.hashtags:
            all_hashtags.extend(post.hashtags)
    
    topic_counts = Counter(all_topics).most_common(limit)
    hashtag_counts = Counter(all_hashtags).most_common(limit)
    
    return {
        "status": "success",
        "days_back": days_back,
        "trending_topics": [
            {"topic": topic, "count": count}
            for topic, count in topic_counts
        ],
        "trending_hashtags": [
            {"hashtag": hashtag, "count": count}
            for hashtag, count in hashtag_counts
        ]
    }
