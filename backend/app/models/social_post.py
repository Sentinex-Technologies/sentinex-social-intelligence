"""
SocialPost model - Core model for social media posts.
Implements NTRO SIH26152 Component A: Continuous Data Collection & Timeline Management.

Requirements:
- Time-stamped chronological database
- Multi-platform support (X, Telegram, Instagram, Facebook, Reddit, YouTube)
- Historical data preservation
- Metadata capture (likes, shares, comments, views)
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class SocialPost(Base):
    """
    Represents a single social media post from any platform.
    
    Supports:
    - X (Twitter): tweets, retweets, replies
    - Telegram: channel/group messages
    - Instagram: posts, stories, reels
    - Facebook: posts, shares
    - Reddit: submissions, comments
    - YouTube: videos, community posts
    """
    
    __tablename__ = "social_posts"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Platform & Identity
    platform = Column(String(50), nullable=False, index=True)
    platform_post_id = Column(String(255), unique=True, nullable=False, index=True)
    
    # Author Information (linked to User model)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    author = relationship("User", back_populates="posts")
    
    # Content
    content_text = Column(Text, nullable=True)
    content_type = Column(String(50), default="text")  # text, image, video, link, poll
    language = Column(String(10), nullable=True)
    
    # Timestamps (Component A requirement)
    created_at = Column(DateTime, nullable=False, index=True)
    collected_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Engagement Metrics (Component A requirement)
    likes_count = Column(Integer, default=0)
    shares_count = Column(Integer, default=0)
    comments_count = Column(Integer, default=0)
    views_count = Column(Integer, default=0)
    
    # Sentiment Analysis Results (Component B - to be populated in Phase 3)
    sentiment_score = Column(Float, nullable=True)  # -1 (negative) to +1 (positive)
    sentiment_label = Column(String(50), nullable=True)  # positive, negative, neutral
    emotions = Column(JSON, nullable=True)  # {"sarcasm": 0.3, "anxiety": 0.1, "excitement": 0.6}
    
    # Topic & Trend Analysis (Component D - to be populated in Phase 3)
    topics = Column(JSON, nullable=True)  # ["topic1", "topic2", ...]
    hashtags = Column(JSON, nullable=True)  # ["#tag1", "#tag2", ...]
    trending_score = Column(Float, default=0.0)
    
    # Geographic & Demographic Context (Component C)
    location = Column(String(255), nullable=True)
    geo_coordinates = Column(JSON, nullable=True)  # {"lat": 28.7041, "lon": 77.1025}
    
    # Network Context (Component E - populated via relationships)
    is_repost = Column(Boolean, default=False)
    parent_post_id = Column(Integer, ForeignKey("social_posts.id"), nullable=True)
    parent_post = relationship("SocialPost", remote_side=[id], backref="replies")
    
    # Metadata & Raw Data
    raw_metadata = Column(JSON, nullable=True)  # Store platform-specific metadata
    
    # Data Source (for legal compliance tracking)
    data_source = Column(String(100), nullable=False)  # "reddit_api", "synthetic", "kaggle_dataset"
    is_synthetic = Column(Boolean, default=False)
    
    # Relationships
    engagements = relationship("Engagement", back_populates="post", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<SocialPost(id={self.id}, platform={self.platform}, author={self.author_id}, created_at={self.created_at})>"
