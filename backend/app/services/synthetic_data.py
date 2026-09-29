"""
Synthetic Data Generator - Legal demo data for SIH26152 prototype.

Generates realistic but synthetic social media data for:
- Component A: Multi-platform time-stamped posts
- Component C: Demographic profiles
- Component E: Network relationships

This approach is 100% legal and ethical:
- No ToS violations
- No web scraping
- No real user data
- Perfect for hackathon prototype and NTRO demo
"""

from faker import Faker
from datetime import datetime, timedelta
import random
from typing import List, Dict, Tuple
from sqlalchemy.orm import Session

from app.models.social_post import SocialPost
from app.models.user import User, UserRelationship
from app.models.engagement import Engagement
from app.config import settings


class SyntheticDataGenerator:
    """
    Generates synthetic social media data for demonstration purposes.
    
    Features:
    - Multi-platform support (X, Telegram, Instagram, Facebook, Reddit, YouTube)
    - Realistic temporal patterns
    - Network relationships and influence distribution
    - Diverse demographics and content themes
    """
    
    PLATFORMS = ["twitter", "telegram", "instagram", "facebook", "reddit", "youtube"]
    
    CONTENT_THEMES = [
        "politics", "technology", "sports", "entertainment", "health",
        "education", "business", "environment", "science", "culture"
    ]
    
    SENTIMENT_TYPES = ["positive", "negative", "neutral", "mixed"]
    
    AGE_RANGES = ["18-24", "25-34", "35-44", "45-54", "55+"]
    
    LANGUAGES = ["en", "hi", "ta", "te", "bn", "mr", "gu", "kn", "ml", "pa"]
    
    CITIES = [
        "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai",
        "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
    ]
    
    def __init__(self, seed: int = None):
        """Initialize generator with optional seed for reproducibility."""
        self.seed = seed or settings.synthetic_data_seed
        self.fake = Faker('en_IN')  # Indian locale for realistic data
        Faker.seed(self.seed)
        random.seed(self.seed)
    
    def generate_users(
        self,
        db: Session,
        count: int = 100,
        platforms: List[str] = None
    ) -> List[User]:
        """
        Generate synthetic user profiles.
        
        Args:
            db: Database session
            count: Number of users to generate
            platforms: List of platforms (defaults to all)
        
        Returns:
            List of created User objects
        """
        platforms = platforms or self.PLATFORMS
        users = []
        
        for i in range(count):
            platform = random.choice(platforms)
            
            # Generate demographic profile
            age_range = random.choice(self.AGE_RANGES)
            gender = random.choice(["male", "female", "non-binary"])
            location = random.choice(self.CITIES)
            language = random.choice(self.LANGUAGES)
            
            # Generate interests
            num_interests = random.randint(2, 5)
            interests = random.sample(self.CONTENT_THEMES, num_interests)
            
            # Generate network metrics with realistic distribution
            # Follow power law: few high-influence users, many low-influence
            influence_tier = random.random()
            if influence_tier > 0.95:  # 5% high-influence
                followers = random.randint(10000, 100000)
                following = random.randint(100, 1000)
            elif influence_tier > 0.80:  # 15% medium-influence
                followers = random.randint(1000, 10000)
                following = random.randint(200, 2000)
            else:  # 80% regular users
                followers = random.randint(10, 1000)
                following = random.randint(50, 500)
            
            user = User(
                platform=platform,
                platform_user_id=f"{platform}_{self.fake.uuid4()}",
                username=self.fake.user_name(),
                age_range=age_range,
                gender=gender,
                location_region=location,
                language=language,
                bio_text=self.fake.text(max_nb_chars=160),
                interests=interests,
                profession=self.fake.job(),
                account_created_at=self.fake.date_time_between(
                    start_date="-5y", end_date="-1y"
                ),
                verified=random.random() > 0.95,  # 5% verified accounts
                followers_count=followers,
                following_count=following,
                posts_count=random.randint(10, 1000),
                data_source="synthetic",
                is_synthetic=True
            )
            
            db.add(user)
            users.append(user)
        
        db.commit()
        
        # Refresh to get IDs
        for user in users:
            db.refresh(user)
        
        return users
    
    def generate_relationships(
        self,
        db: Session,
        users: List[User],
        avg_connections: int = 20
    ) -> List[UserRelationship]:
        """
        Generate realistic network relationships between users.
        
        Creates a scale-free network (Component E requirement):
        - High-influence users have many followers
        - Regular users follow influential users more often
        - Some bidirectional relationships (mutual follows)
        
        Args:
            db: Database session
            users: List of User objects
            avg_connections: Average connections per user
        
        Returns:
            List of UserRelationship objects
        """
        relationships = []
        
        # Sort users by followers (influence)
        sorted_users = sorted(users, key=lambda u: u.followers_count, reverse=True)
        influential_users = sorted_users[:int(len(users) * 0.1)]  # Top 10%
        
        for user in users:
            # Number of users this user follows
            num_following = random.randint(
                int(avg_connections * 0.5),
                int(avg_connections * 1.5)
            )
            
            # Preferential attachment: more likely to follow influential users
            follow_targets = []
            
            # 60% chance to follow influential users
            num_influential = int(num_following * 0.6)
            follow_targets.extend(
                random.sample(influential_users, min(num_influential, len(influential_users)))
            )
            
            # 40% chance to follow random users
            num_random = num_following - len(follow_targets)
            available_users = [u for u in users if u.id != user.id and u not in follow_targets]
            if available_users:
                follow_targets.extend(
                    random.sample(available_users, min(num_random, len(available_users)))
                )
            
            # Create relationships
            for target in follow_targets:
                if target.id != user.id:  # No self-follows
                    relationship = UserRelationship(
                        follower_id=user.id,
                        followed_id=target.id,
                        relationship_type="follow",
                        created_at=self.fake.date_time_between(
                            start_date="-2y", end_date="now"
                        ),
                        interaction_score=random.uniform(0.0, 1.0)
                    )
                    relationships.append(relationship)
                    db.add(relationship)
        
        db.commit()
        return relationships
    
    def generate_posts(
        self,
        db: Session,
        users: List[User],
        count: int = 1000,
        days_back: int = 30
    ) -> List[SocialPost]:
        """
        Generate synthetic social media posts with realistic patterns.
        
        Args:
            db: Database session
            users: List of User objects to author posts
            count: Number of posts to generate
            days_back: Generate posts from this many days ago to now
        
        Returns:
            List of SocialPost objects
        """
        posts = []
        start_date = datetime.utcnow() - timedelta(days=days_back)
        
        for i in range(count):
            author = random.choice(users)
            theme = random.choice(self.CONTENT_THEMES)
            
            # Generate content based on platform
            if author.platform in ["twitter", "telegram"]:
                content_text = self.fake.text(max_nb_chars=280)
            elif author.platform == "instagram":
                content_text = self.fake.text(max_nb_chars=150)
            else:
                content_text = self.fake.text(max_nb_chars=500)
            
            # Add relevant hashtags
            hashtags = [f"#{theme}", f"#{random.choice(self.CONTENT_THEMES)}"]
            
            # Generate sentiment (will be refined in Phase 3)
            sentiment_label = random.choice(self.SENTIMENT_TYPES)
            if sentiment_label == "positive":
                sentiment_score = random.uniform(0.3, 1.0)
            elif sentiment_label == "negative":
                sentiment_score = random.uniform(-1.0, -0.3)
            else:
                sentiment_score = random.uniform(-0.3, 0.3)
            
            # Generate 5-dimensional emotions (Component B)
            emotions = {
                "sarcasm": round(random.uniform(0.0, 0.4), 2),
                "anxiety": round(random.uniform(0.0, 0.5) if sentiment_label == "negative" else random.uniform(0.0, 0.2), 2),
                "excitement": round(random.uniform(0.3, 0.8) if sentiment_label == "positive" else random.uniform(0.0, 0.3), 2),
                "supportive": round(random.uniform(0.2, 0.7) if sentiment_label == "positive" else random.uniform(0.0, 0.3), 2),
                "against": round(random.uniform(0.2, 0.7) if sentiment_label == "negative" else random.uniform(0.0, 0.3), 2)
            }
            
            # Engagement metrics (Component A requirement)
            # More influential authors get more engagement
            engagement_multiplier = author.followers_count / 1000
            likes = int(random.randint(0, 100) * max(1, engagement_multiplier))
            shares = int(likes * random.uniform(0.1, 0.3))
            comments = int(likes * random.uniform(0.05, 0.15))
            views = int(likes * random.uniform(5, 20))
            
            post = SocialPost(
                platform=author.platform,
                platform_post_id=f"{author.platform}_{self.fake.uuid4()}",
                author_id=author.id,
                content_text=content_text,
                content_type=random.choice(["text", "text", "text", "image", "video"]),
                language=author.language,
                created_at=self.fake.date_time_between(
                    start_date=start_date, end_date="now"
                ),
                likes_count=likes,
                shares_count=shares,
                comments_count=comments,
                views_count=views,
                sentiment_score=sentiment_score,
                sentiment_label=sentiment_label,
                emotions=emotions,
                topics=[theme],
                hashtags=hashtags,
                trending_score=random.uniform(0.0, 1.0),
                location=author.location_region,
                data_source="synthetic",
                is_synthetic=True
            )
            
            posts.append(post)
            db.add(post)
        
        db.commit()
        
        # Refresh to get IDs
        for post in posts:
            db.refresh(post)
        
        return posts
    
    def generate_engagements(
        self,
        db: Session,
        posts: List[SocialPost],
        users: List[User]
    ) -> List[Engagement]:
        """
        Generate engagement events for posts.
        
        Args:
            db: Database session
            posts: List of SocialPost objects
            users: List of User objects
        
        Returns:
            List of Engagement objects
        """
        engagements = []
        
        for post in posts:
            # Number of engagements based on post's like count
            num_engagements = min(post.likes_count, len(users))
            
            # Select random users to engage
            engaging_users = random.sample(users, num_engagements)
            
            for user in engaging_users:
                engagement_type = random.choice(["like", "like", "like", "share", "comment"])
                
                engagement = Engagement(
                    post_id=post.id,
                    user_id=user.id,
                    engagement_type=engagement_type,
                    engaged_at=post.created_at + timedelta(
                        minutes=random.randint(1, 1440)  # Within 24 hours
                    ),
                    sentiment_score=random.uniform(-1.0, 1.0),
                    data_source="synthetic",
                    is_synthetic=True
                )
                
                engagements.append(engagement)
                db.add(engagement)
        
        db.commit()
        return engagements
    
    def generate_complete_dataset(
        self,
        db: Session,
        num_users: int = 100,
        num_posts: int = 1000,
        days_back: int = 30
    ) -> Dict[str, List]:
        """
        Generate a complete synthetic dataset with users, posts, relationships, and engagements.
        
        This is the main entry point for generating demo data.
        
        Args:
            db: Database session
            num_users: Number of users to generate
            num_posts: Number of posts to generate
            days_back: Historical data timespan
        
        Returns:
            Dictionary with created entities
        """
        print(f"🔄 Generating synthetic dataset...")
        print(f"   Users: {num_users}")
        print(f"   Posts: {num_posts}")
        print(f"   Timespan: {days_back} days")
        
        # Generate users
        print("👥 Generating users...")
        users = self.generate_users(db, count=num_users)
        
        # Generate network relationships
        print("🔗 Generating network relationships...")
        relationships = self.generate_relationships(db, users, avg_connections=20)
        
        # Generate posts
        print("📝 Generating posts...")
        posts = self.generate_posts(db, users, count=num_posts, days_back=days_back)
        
        # Generate engagements
        print("❤️  Generating engagements...")
        engagements = self.generate_engagements(db, posts, users)
        
        print(f"✅ Synthetic data generation complete!")
        print(f"   Created: {len(users)} users, {len(posts)} posts, ")
        print(f"            {len(relationships)} relationships, {len(engagements)} engagements")
        
        return {
            "users": users,
            "posts": posts,
            "relationships": relationships,
            "engagements": engagements
        }
