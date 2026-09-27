"""
Tests for synthetic data generation (Component A).
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.services.synthetic_data import SyntheticDataGenerator
from app.models.user import User
from app.models.social_post import SocialPost


@pytest.fixture
def test_db():
    """Create a temporary in-memory database for testing."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    yield db
    db.close()


def test_generate_users(test_db):
    """Test user generation."""
    generator = SyntheticDataGenerator(seed=42)
    users = generator.generate_users(test_db, count=10)
    
    assert len(users) == 10
    assert all(isinstance(u, User) for u in users)
    assert all(u.id is not None for u in users)
    assert all(u.platform in SyntheticDataGenerator.PLATFORMS for u in users)


def test_generate_posts(test_db):
    """Test post generation."""
    generator = SyntheticDataGenerator(seed=42)
    users = generator.generate_users(test_db, count=5)
    posts = generator.generate_posts(test_db, users, count=20, days_back=7)
    
    assert len(posts) == 20
    assert all(isinstance(p, SocialPost) for p in posts)
    assert all(p.id is not None for p in posts)
    assert all(p.author_id in [u.id for u in users] for p in posts)
    assert all(p.is_synthetic is True for p in posts)


def test_generate_complete_dataset(test_db):
    """Test complete dataset generation."""
    generator = SyntheticDataGenerator(seed=42)
    result = generator.generate_complete_dataset(
        test_db,
        num_users=10,
        num_posts=30,
        days_back=7
    )
    
    assert "users" in result
    assert "posts" in result
    assert "relationships" in result
    assert "engagements" in result
    
    assert len(result["users"]) == 10
    assert len(result["posts"]) == 30
    assert len(result["relationships"]) > 0
    assert len(result["engagements"]) > 0


def test_user_demographics(test_db):
    """Test that users have proper demographic data."""
    generator = SyntheticDataGenerator(seed=42)
    users = generator.generate_users(test_db, count=10)
    
    for user in users:
        assert user.age_range in SyntheticDataGenerator.AGE_RANGES
        assert user.gender in ["male", "female", "non-binary"]
        assert user.location_region in SyntheticDataGenerator.CITIES
        assert user.language in SyntheticDataGenerator.LANGUAGES
        assert len(user.interests) >= 2


def test_post_sentiment(test_db):
    """Test that posts have sentiment data."""
    generator = SyntheticDataGenerator(seed=42)
    users = generator.generate_users(test_db, count=5)
    posts = generator.generate_posts(test_db, users, count=20)
    
    for post in posts:
        assert post.sentiment_label in SyntheticDataGenerator.SENTIMENT_TYPES
        assert -1.0 <= post.sentiment_score <= 1.0
        assert post.topics is not None
        assert post.hashtags is not None
