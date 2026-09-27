"""
User model - Represents social media users and their relationships.
Implements NTRO SIH26152 Component C & E:
- Component C: Automated Demographic Profiling
- Component E: Link Analysis & Network Topology

Requirements:
- Aggregate/anonymized demographic data
- User relationships (followers, following)
- Influence metrics
- Network centrality measures
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class User(Base):
    """
    Represents a social media user/account across platforms.
    
    Privacy Note:
    - Stores only aggregate/anonymized demographic data
    - No PII (Personally Identifiable Information) stored
    - Complies with ethical data handling requirements
    """
    
    __tablename__ = "users"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Platform Identity
    platform = Column(String(50), nullable=False, index=True)
    platform_user_id = Column(String(255), nullable=False, index=True)
    username = Column(String(255), nullable=True)
    
    # Demographic Profile (Component C - Aggregated/Anonymized)
    age_range = Column(String(20), nullable=True)  # "18-24", "25-34", "35-44", "45+"
    gender = Column(String(20), nullable=True)  # "male", "female", "non-binary", "unknown"
    location_region = Column(String(255), nullable=True)  # City/State/Country
    language = Column(String(10), nullable=True)  # ISO language code
    
    # Professional & Interest Profile (Component C)
    bio_text = Column(Text, nullable=True)
    interests = Column(JSON, nullable=True)  # ["technology", "politics", "sports"]
    profession = Column(String(255), nullable=True)
    
    # Account Metadata
    account_created_at = Column(DateTime, nullable=True)
    verified = Column(Boolean, default=False)
    
    # Network Metrics (Component E - Influence Analysis)
    followers_count = Column(Integer, default=0)
    following_count = Column(Integer, default=0)
    posts_count = Column(Integer, default=0)
    
    # Influence Scores (Component E - computed from network analysis)
    influence_score = Column(Float, default=0.0)  # 0.0 to 1.0
    centrality_score = Column(Float, default=0.0)  # Network centrality measure
    reach_score = Column(Float, default=0.0)  # Potential reach based on followers
    
    # Activity Patterns
    avg_post_frequency = Column(Float, default=0.0)  # Posts per day
    avg_engagement_rate = Column(Float, default=0.0)  # Engagement per post
    
    # Timestamps
    first_seen_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_seen_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Data Source (for legal compliance tracking)
    data_source = Column(String(100), nullable=False)
    is_synthetic = Column(Boolean, default=False)
    
    # Metadata
    raw_metadata = Column(JSON, nullable=True)
    
    # Relationships
    posts = relationship("SocialPost", back_populates="author", cascade="all, delete-orphan")
    
    # Network relationships (followers/following)
    following = relationship(
        "UserRelationship",
        foreign_keys="UserRelationship.follower_id",
        back_populates="follower",
        cascade="all, delete-orphan"
    )
    followers = relationship(
        "UserRelationship",
        foreign_keys="UserRelationship.followed_id",
        back_populates="followed",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<User(id={self.id}, platform={self.platform}, username={self.username})>"


class UserRelationship(Base):
    """
    Represents follower/following relationships between users.
    Used for Component E: Network Topology & Link Analysis.
    
    This enables:
    - Building social network graphs
    - Computing influence propagation paths
    - Identifying opinion leaders and central nodes
    """
    
    __tablename__ = "user_relationships"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Relationship Definition
    follower_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    followed_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    
    # Relationship Type
    relationship_type = Column(String(50), default="follow")  # follow, friend, mutual
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Interaction Strength (for weighted network analysis)
    interaction_score = Column(Float, default=0.0)  # Based on likes, comments, shares
    
    # Relationships
    follower = relationship("User", foreign_keys=[follower_id], back_populates="following")
    followed = relationship("User", foreign_keys=[followed_id], back_populates="followers")
    
    def __repr__(self):
        return f"<UserRelationship(follower={self.follower_id}, followed={self.followed_id})>"
