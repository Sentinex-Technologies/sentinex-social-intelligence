"""
Engagement model - Tracks user interactions with posts.
Supports NTRO SIH26152 Component A & E:
- Component A: Engagement metrics (likes, shares, comments)
- Component E: Information propagation tracking

This model helps answer:
- How sentiment spreads through the network?
- Which users amplify certain narratives?
- What are the engagement patterns over time?
"""

from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Engagement(Base):
    """
    Represents a single engagement event (like, share, comment, view).
    
    This granular tracking enables:
    - Temporal engagement pattern analysis
    - User influence computation based on engagement received
    - Sentiment propagation tracking (Component E)
    """
    
    __tablename__ = "engagements"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Post Reference
    post_id = Column(Integer, ForeignKey("social_posts.id"), nullable=False, index=True)
    post = relationship("SocialPost", back_populates="engagements")
    
    # User Reference (who engaged)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    
    # Engagement Type
    engagement_type = Column(String(50), nullable=False)  # like, share, comment, view, retweet
    
    # Timestamp (Component A requirement - chronological tracking)
    engaged_at = Column(DateTime, nullable=False, index=True)
    collected_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Sentiment Context (for propagation analysis)
    sentiment_score = Column(Float, nullable=True)  # Sentiment of the engaging user
    
    # Data Source
    data_source = Column(String(100), nullable=False)
    is_synthetic = Column(Boolean, default=False)
    
    def __repr__(self):
        return f"<Engagement(id={self.id}, post={self.post_id}, type={self.engagement_type}, at={self.engaged_at})>"
