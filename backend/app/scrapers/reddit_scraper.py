"""
Reddit API Scraper using PRAW

Setup Instructions:
1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" → Select "script"
3. Fill in:
   - name: Sentinex Social Intelligence
   - redirect uri: http://localhost:8002
4. Get client_id (under app name) and client_secret
5. Add to .env:
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT=Sentinex/1.0

Usage:
    from app.scrapers.reddit_scraper import RedditScraper
    
    scraper = RedditScraper()
    posts = scraper.fetch_posts(subreddit='india', limit=100)
"""

from datetime import datetime
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

try:
    import praw
    PRAW_AVAILABLE = True
except ImportError:
    PRAW_AVAILABLE = False
    logger.warning("PRAW not installed. Run: pip install praw")


class RedditScraper:
    """
    Fetch live posts from Reddit using official API (FREE)
    
    Features:
    - ✅ FREE (no cost)
    - ✅ Legal (official API)
    - ✅ Easy setup (15 minutes)
    - ✅ Good data quality
    - ✅ No rate limit issues (600 requests/10 min)
    """
    
    def __init__(
        self, 
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        user_agent: Optional[str] = None
    ):
        """
        Initialize Reddit scraper
        
        Args:
            client_id: Reddit app client ID (from .env if not provided)
            client_secret: Reddit app client secret (from .env if not provided)
            user_agent: User agent string (default: Sentinex/1.0)
        """
        if not PRAW_AVAILABLE:
            raise ImportError(
                "PRAW library required. Install with: pip install praw"
            )
        
        # Get credentials from config if not provided
        if not client_id or not client_secret:
            try:
                from app.config import settings
                client_id = client_id or settings.reddit_client_id
                client_secret = client_secret or settings.reddit_client_secret
                user_agent = user_agent or getattr(settings, 'reddit_user_agent', 'Sentinex/1.0')
            except:
                raise ValueError(
                    "Reddit credentials not found. "
                    "Please provide client_id and client_secret, "
                    "or add to .env file."
                )
        
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        
        logger.info("Reddit scraper initialized successfully")
    
    def fetch_posts(
        self, 
        subreddit: str = 'india',
        limit: int = 100,
        sort: str = 'hot',
        time_filter: str = 'day'
    ) -> List[Dict]:
        """
        Fetch live posts from a subreddit
        
        Args:
            subreddit: Subreddit name (e.g. 'india', 'worldnews', 'technology')
            limit: Maximum number of posts to fetch (1-1000)
            sort: Sort method ('hot', 'new', 'top', 'rising')
            time_filter: Time filter for 'top' sort ('hour', 'day', 'week', 'month', 'year', 'all')
        
        Returns:
            List of post dictionaries compatible with SocialPost model
        
        Example:
            scraper = RedditScraper()
            posts = scraper.fetch_posts('india', limit=50, sort='hot')
        """
        try:
            subreddit_obj = self.reddit.subreddit(subreddit)
            posts = []
            
            # Get submissions based on sort method
            if sort == 'hot':
                submissions = subreddit_obj.hot(limit=limit)
            elif sort == 'new':
                submissions = subreddit_obj.new(limit=limit)
            elif sort == 'top':
                submissions = subreddit_obj.top(limit=limit, time_filter=time_filter)
            elif sort == 'rising':
                submissions = subreddit_obj.rising(limit=limit)
            else:
                raise ValueError(f"Invalid sort method: {sort}. Use 'hot', 'new', 'top', or 'rising'")
            
            # Process submissions
            for post in submissions:
                try:
                    # Combine title and self text
                    content = post.title
                    if post.selftext:
                        content += f"\n\n{post.selftext}"
                    
                    # Extract hashtags from title and text
                    import re
                    hashtags = re.findall(r'#(\w+)', content)
                    
                    posts.append({
                        'platform': 'reddit',
                        'platform_post_id': post.id,
                        'author_username': post.author.name if post.author else '[deleted]',
                        'content_text': content,
                        'content_type': 'text' if not post.url.endswith(('.jpg', '.png', '.gif')) else 'image',
                        'language': 'en',  # Reddit is primarily English
                        'created_at': datetime.fromtimestamp(post.created_utc),
                        'likes_count': post.score,
                        'comments_count': post.num_comments,
                        'shares_count': 0,  # Reddit doesn't expose share count
                        'views_count': 0,  # Reddit doesn't expose view count
                        'url': f"https://reddit.com{post.permalink}",
                        'hashtags': hashtags,
                        'topics': [subreddit],  # Subreddit as topic
                        'location': None,  # Reddit doesn't have location data
                        'data_source': 'reddit_api',
                        'is_synthetic': False  # ✅ Real live data!
                    })
                
                except Exception as e:
                    logger.error(f"Error processing post {post.id}: {e}")
                    continue
            
            logger.info(f"Fetched {len(posts)} posts from r/{subreddit}")
            return posts
        
        except Exception as e:
            logger.error(f"Error fetching Reddit posts: {e}")
            return []
    
    def fetch_comments(
        self, 
        post_id: str, 
        limit: int = 100
    ) -> List[Dict]:
        """
        Fetch comments from a specific Reddit post
        
        Args:
            post_id: Reddit post ID
            limit: Maximum number of comments
        
        Returns:
            List of comment dictionaries
        """
        try:
            submission = self.reddit.submission(id=post_id)
            submission.comments.replace_more(limit=0)  # Remove "load more" placeholders
            
            comments = []
            for comment in submission.comments.list()[:limit]:
                if hasattr(comment, 'body'):
                    comments.append({
                        'post_id': post_id,
                        'author': comment.author.name if comment.author else '[deleted]',
                        'text': comment.body,
                        'score': comment.score,
                        'created_at': datetime.fromtimestamp(comment.created_utc)
                    })
            
            logger.info(f"Fetched {len(comments)} comments from post {post_id}")
            return comments
        
        except Exception as e:
            logger.error(f"Error fetching comments: {e}")
            return []
    
    def fetch_multiple_subreddits(
        self,
        subreddits: List[str],
        limit_per_sub: int = 50,
        sort: str = 'hot'
    ) -> List[Dict]:
        """
        Fetch posts from multiple subreddits
        
        Args:
            subreddits: List of subreddit names
            limit_per_sub: Posts per subreddit
            sort: Sort method
        
        Returns:
            Combined list of posts from all subreddits
        """
        all_posts = []
        for subreddit in subreddits:
            try:
                posts = self.fetch_posts(subreddit, limit=limit_per_sub, sort=sort)
                all_posts.extend(posts)
            except Exception as e:
                logger.error(f"Error fetching r/{subreddit}: {e}")
        
        return all_posts


# Example usage
if __name__ == '__main__':
    # Test the scraper
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    try:
        scraper = RedditScraper(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET')
        )
        
        # Fetch hot posts from r/india
        posts = scraper.fetch_posts('india', limit=10, sort='hot')
        
        print(f"\nFetched {len(posts)} posts from r/india:")
        for i, post in enumerate(posts[:5], 1):
            print(f"\n{i}. {post['content_text'][:100]}...")
            print(f"   Likes: {post['likes_count']}, Comments: {post['comments_count']}")
    
    except Exception as e:
        print(f"Error: {e}")
        print("\nSetup Instructions:")
        print("1. Go to https://www.reddit.com/prefs/apps")
        print("2. Create an app (type: script)")
        print("3. Add credentials to .env file")
