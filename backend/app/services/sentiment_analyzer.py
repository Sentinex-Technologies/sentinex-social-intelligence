"""
Sentiment Analyzer - Component B: Multi-Dimensional Sentiment Inference

Implements NTRO SIH26152 Component B requirements:
- Nuanced emotion detection (sarcasm, anxiety, excitement, supportive, against)
- Sentiment fluctuation tracking over time
- Multi-dimensional sentiment scoring

Uses VADER (Valence Aware Dictionary and sEntiment Reasoner) for social media text.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from typing import Dict, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta

from app.models.social_post import SocialPost


class SentimentAnalyzer:
    """
    Multi-dimensional sentiment analyzer for social media posts.
    
    Detects:
    - Basic sentiment (positive, negative, neutral)
    - Emotions (sarcasm, anxiety, excitement, supportive, against)
    - Sentiment trends over time
    """
    
    # Keywords for emotion detection
    EMOTION_KEYWORDS = {
        "sarcasm": ["yeah right", "sure", "totally", "obviously", "of course", "great job", "wonderful"],
        "anxiety": ["worried", "anxious", "concerned", "nervous", "scared", "afraid", "fear"],
        "excitement": ["amazing", "awesome", "excited", "can't wait", "wow", "incredible", "fantastic"],
        "supportive": ["support", "agree", "love", "like", "awesome", "great", "excellent", "proud"],
        "against": ["disagree", "hate", "dislike", "wrong", "bad", "terrible", "awful", "oppose"]
    }
    
    def __init__(self):
        """Initialize sentiment analyzers."""
        self.vader = SentimentIntensityAnalyzer()
    
    def analyze_text(self, text: str) -> Dict[str, any]:
        """
        Analyze sentiment and emotions in text.
        
        Args:
            text: Text to analyze
        
        Returns:
            Dictionary with sentiment scores and emotions
        """
        if not text or len(text.strip()) == 0:
            return self._empty_result()
        
        # VADER sentiment analysis (optimized for social media)
        vader_scores = self.vader.polarity_scores(text)
        
        # TextBlob for additional analysis
        blob = TextBlob(text)
        
        # Determine primary sentiment
        compound = vader_scores['compound']
        if compound >= 0.05:
            sentiment_label = "positive"
        elif compound <= -0.05:
            sentiment_label = "negative"
        else:
            sentiment_label = "neutral"
        
        # Detect emotions
        emotions = self._detect_emotions(text.lower())
        
        return {
            "sentiment_score": compound,  # -1 to +1
            "sentiment_label": sentiment_label,
            "emotions": emotions,
            "vader_breakdown": {
                "positive": vader_scores['pos'],
                "negative": vader_scores['neg'],
                "neutral": vader_scores['neu']
            },
            "subjectivity": blob.sentiment.subjectivity,  # 0 to 1 (objective to subjective)
            "polarity": blob.sentiment.polarity  # -1 to +1
        }
    
    def _detect_emotions(self, text: str) -> Dict[str, float]:
        """
        Detect specific emotions using keyword matching.
        
        Args:
            text: Lowercase text to analyze
        
        Returns:
            Dictionary of emotion scores (0.0 to 1.0)
        """
        emotions = {}
        
        for emotion, keywords in self.EMOTION_KEYWORDS.items():
            # Count keyword matches
            matches = sum(1 for keyword in keywords if keyword in text)
            
            # Normalize to 0-1 scale (cap at 3 matches = 1.0)
            score = min(matches / 3.0, 1.0)
            emotions[emotion] = round(score, 2)
        
        return emotions
    
    def _empty_result(self) -> Dict[str, any]:
        """Return empty result for invalid input."""
        return {
            "sentiment_score": 0.0,
            "sentiment_label": "neutral",
            "emotions": {k: 0.0 for k in self.EMOTION_KEYWORDS.keys()},
            "vader_breakdown": {"positive": 0.0, "negative": 0.0, "neutral": 1.0},
            "subjectivity": 0.0,
            "polarity": 0.0
        }
    
    def analyze_posts_batch(self, db: Session, post_ids: List[int]) -> Dict[int, Dict]:
        """
        Analyze sentiment for multiple posts.
        
        Args:
            db: Database session
            post_ids: List of post IDs to analyze
        
        Returns:
            Dictionary mapping post_id to sentiment results
        """
        results = {}
        
        posts = db.query(SocialPost).filter(SocialPost.id.in_(post_ids)).all()
        
        for post in posts:
            if post.content_text:
                analysis = self.analyze_text(post.content_text)
                results[post.id] = analysis
                
                # Update post with sentiment data
                post.sentiment_score = analysis["sentiment_score"]
                post.sentiment_label = analysis["sentiment_label"]
                post.emotions = analysis["emotions"]
        
        db.commit()
        return results
    
    def analyze_all_posts(self, db: Session, limit: Optional[int] = None) -> int:
        """
        Analyze sentiment for all posts without sentiment data.
        
        Args:
            db: Database session
            limit: Maximum number of posts to process
        
        Returns:
            Number of posts analyzed
        """
        query = db.query(SocialPost).filter(
            (SocialPost.sentiment_score == None) | (SocialPost.emotions == None)
        )
        
        if limit:
            query = query.limit(limit)
        
        posts = query.all()
        count = 0
        
        for post in posts:
            if post.content_text:
                analysis = self.analyze_text(post.content_text)
                post.sentiment_score = analysis["sentiment_score"]
                post.sentiment_label = analysis["sentiment_label"]
                post.emotions = analysis["emotions"]
                count += 1
        
        db.commit()
        return count
    
    def get_sentiment_trends(
        self,
        db: Session,
        days_back: int = 30,
        platform: Optional[str] = None
    ) -> List[Dict]:
        """
        Get sentiment trends over time (Component B requirement).
        
        Args:
            db: Database session
            days_back: Number of days to analyze
            platform: Filter by platform
        
        Returns:
            List of daily sentiment averages
        """
        from sqlalchemy import cast, Date
        
        start_date = datetime.utcnow() - timedelta(days=days_back)
        query = db.query(SocialPost).filter(SocialPost.created_at >= start_date)
        
        if platform:
            query = query.filter(SocialPost.platform == platform)
        
        # Group by date and calculate average sentiment
        results = query.with_entities(
            cast(SocialPost.created_at, Date).label('date'),
            func.avg(SocialPost.sentiment_score).label('avg_sentiment'),
            func.count(SocialPost.id).label('post_count')
        ).group_by(cast(SocialPost.created_at, Date)).all()
        
        return [
            {
                "date": str(date),
                "avg_sentiment": float(avg_sentiment or 0),
                "post_count": post_count
            }
            for date, avg_sentiment, post_count in results
        ]
    
    def get_emotion_distribution(
        self,
        db: Session,
        days_back: int = 7,
        platform: Optional[str] = None
    ) -> Dict[str, float]:
        """
        Get distribution of emotions across posts.
        
        Args:
            db: Database session
            days_back: Number of days to analyze
            platform: Filter by platform
        
        Returns:
            Dictionary of emotion averages
        """
        start_date = datetime.utcnow() - timedelta(days=days_back)
        query = db.query(SocialPost).filter(
            SocialPost.created_at >= start_date,
            SocialPost.emotions != None
        )
        
        if platform:
            query = query.filter(SocialPost.platform == platform)
        
        posts = query.all()
        
        if not posts:
            return {k: 0.0 for k in self.EMOTION_KEYWORDS.keys()}
        
        # Aggregate emotions
        emotion_sums = {k: 0.0 for k in self.EMOTION_KEYWORDS.keys()}
        
        for post in posts:
            if post.emotions:
                for emotion, score in post.emotions.items():
                    if emotion in emotion_sums:
                        emotion_sums[emotion] += score
        
        # Calculate averages
        num_posts = len(posts)
        return {k: round(v / num_posts, 3) for k, v in emotion_sums.items()}
