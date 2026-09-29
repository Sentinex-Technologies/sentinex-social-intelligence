"""
RSS/Atom Feed Scraper

EASIEST scraper - no API keys required!

Setup Instructions:
1. pip install feedparser
2. That's it! No API keys needed.

Usage:
    from app.scrapers.rss_scraper import RSSFeedScraper
    
    scraper = RSSFeedScraper()
    posts = scraper.fetch_feed('bbc', limit=100)
    # or fetch all feeds
    posts = scraper.fetch_all_feeds(limit_per_feed=50)
"""

from datetime import datetime
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

try:
    import feedparser
    FEEDPARSER_AVAILABLE = True
except ImportError:
    FEEDPARSER_AVAILABLE = False
    logger.warning("feedparser not installed. Run: pip install feedparser")


class RSSFeedScraper:
    """
    Fetch posts from RSS/Atom feeds
    
    Features:
    - ✅ 100% FREE (no API keys)
    - ✅ 100% Legal (public feeds)
    - ✅ Super easy (5 minute setup)
    - ✅ No rate limits
    - ✅ Works for news, blogs, Reddit, etc.
    
    Best for:
    - News websites (BBC, NYT, Guardian, etc.)
    - Tech blogs (TechCrunch, Hacker News, etc.)
    - Reddit subreddit feeds
    """
    
    # Curated list of high-quality public RSS feeds
    FEEDS = {
        # News
        'bbc': {
            'url': 'http://feeds.bbci.co.uk/news/rss.xml',
            'name': 'BBC News',
            'category': 'news'
        },
        'nyt': {
            'url': 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
            'name': 'New York Times',
            'category': 'news'
        },
        'guardian': {
            'url': 'https://www.theguardian.com/world/rss',
            'name': 'The Guardian',
            'category': 'news'
        },
        'reuters': {
            'url': 'https://www.reutersagency.com/feed/',
            'name': 'Reuters',
            'category': 'news'
        },
        
        # Tech
        'techcrunch': {
            'url': 'https://techcrunch.com/feed/',
            'name': 'TechCrunch',
            'category': 'technology'
        },
        'hn': {
            'url': 'https://news.ycombinator.com/rss',
            'name': 'Hacker News',
            'category': 'technology'
        },
        'verge': {
            'url': 'https://www.theverge.com/rss/index.xml',
            'name': 'The Verge',
            'category': 'technology'
        },
        
        # Reddit (yes, Reddit has RSS!)
        'reddit_india': {
            'url': 'https://www.reddit.com/r/india/.rss',
            'name': 'Reddit: India',
            'category': 'social'
        },
        'reddit_technology': {
            'url': 'https://www.reddit.com/r/technology/.rss',
            'name': 'Reddit: Technology',
            'category': 'technology'
        },
        'reddit_worldnews': {
            'url': 'https://www.reddit.com/r/worldnews/.rss',
            'name': 'Reddit: World News',
            'category': 'news'
        }
    }
    
    def __init__(self):
        """Initialize RSS feed scraper"""
        if not FEEDPARSER_AVAILABLE:
            raise ImportError(
                "feedparser library required. Install with: pip install feedparser"
            )
        logger.info("RSS feed scraper initialized")
    
    def fetch_feed(
        self, 
        feed_name: str, 
        limit: int = 100
    ) -> List[Dict]:
        """
        Fetch posts from a single RSS feed
        
        Args:
            feed_name: Feed identifier (e.g. 'bbc', 'techcrunch', 'hn')
            limit: Maximum number of items to fetch
        
        Returns:
            List of post dictionaries compatible with SocialPost model
        
        Example:
            scraper = RSSFeedScraper()
            posts = scraper.fetch_feed('bbc', limit=50)
        """
        if feed_name not in self.FEEDS:
            raise ValueError(
                f"Unknown feed: {feed_name}. "
                f"Available feeds: {', '.join(self.FEEDS.keys())}"
            )
        
        feed_info = self.FEEDS[feed_name]
        
        try:
            # Parse RSS feed
            feed = feedparser.parse(feed_info['url'])
            posts = []
            
            for entry in feed.entries[:limit]:
                try:
                    # Parse published date
                    published = None
                    if hasattr(entry, 'published_parsed') and entry.published_parsed:
                        published = datetime(*entry.published_parsed[:6])
                    elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                        published = datetime(*entry.updated_parsed[:6])
                    
                    # Get content (some feeds use 'summary', some use 'description')
                    content = ''
                    if hasattr(entry, 'title'):
                        content = entry.title
                    if hasattr(entry, 'summary'):
                        content += f"\n\n{entry.summary}"
                    elif hasattr(entry, 'description'):
                        content += f"\n\n{entry.description}"
                    
                    # Extract hashtags from content
                    import re
                    hashtags = re.findall(r'#(\w+)', content)
                    
                    posts.append({
                        'platform': 'rss',
                        'platform_post_id': entry.get('id', entry.get('link', '')),
                        'author_username': feed_info['name'],
                        'content_text': content.strip(),
                        'content_type': 'text',
                        'language': 'en',  # Most feeds are English
                        'created_at': published or datetime.utcnow(),
                        'likes_count': 0,  # RSS doesn't have engagement metrics
                        'comments_count': 0,
                        'shares_count': 0,
                        'views_count': 0,
                        'url': entry.get('link', ''),
                        'hashtags': hashtags,
                        'topics': [feed_info['category']],
                        'location': None,
                        'data_source': f'rss_{feed_name}',
                        'is_synthetic': False  # ✅ Real live data!
                    })
                
                except Exception as e:
                    logger.error(f"Error processing entry: {e}")
                    continue
            
            logger.info(f"Fetched {len(posts)} posts from {feed_info['name']}")
            return posts
        
        except Exception as e:
            logger.error(f"Error fetching RSS feed {feed_name}: {e}")
            return []
    
    def fetch_all_feeds(
        self, 
        limit_per_feed: int = 50,
        categories: List[str] = None
    ) -> List[Dict]:
        """
        Fetch posts from all configured RSS feeds
        
        Args:
            limit_per_feed: Max items per feed
            categories: Filter by categories (e.g. ['news', 'technology'])
        
        Returns:
            Combined list of posts from all feeds
        
        Example:
            scraper = RSSFeedScraper()
            # Get all posts
            all_posts = scraper.fetch_all_feeds(limit_per_feed=50)
            # Get only news posts
            news_posts = scraper.fetch_all_feeds(categories=['news'])
        """
        all_posts = []
        
        for feed_name, feed_info in self.FEEDS.items():
            # Filter by category if specified
            if categories and feed_info['category'] not in categories:
                continue
            
            try:
                posts = self.fetch_feed(feed_name, limit=limit_per_feed)
                all_posts.extend(posts)
            except Exception as e:
                logger.error(f"Error fetching {feed_name}: {e}")
                continue
        
        logger.info(f"Fetched total {len(all_posts)} posts from {len(self.FEEDS)} feeds")
        return all_posts
    
    def add_custom_feed(
        self, 
        feed_id: str, 
        url: str, 
        name: str, 
        category: str = 'general'
    ):
        """
        Add a custom RSS feed to the scraper
        
        Args:
            feed_id: Unique identifier for the feed
            url: RSS/Atom feed URL
            name: Display name
            category: Feed category
        
        Example:
            scraper = RSSFeedScraper()
            scraper.add_custom_feed(
                'toi', 
                'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',
                'Times of India',
                'news'
            )
            posts = scraper.fetch_feed('toi')
        """
        self.FEEDS[feed_id] = {
            'url': url,
            'name': name,
            'category': category
        }
        logger.info(f"Added custom feed: {name}")
    
    def list_feeds(self) -> Dict[str, Dict]:
        """List all available feeds with details"""
        return self.FEEDS


# Example usage
if __name__ == '__main__':
    # Test the scraper
    scraper = RSSFeedScraper()
    
    print("Available feeds:")
    for feed_id, feed_info in scraper.list_feeds().items():
        print(f"  {feed_id}: {feed_info['name']} ({feed_info['category']})")
    
    # Fetch BBC news
    print("\n\nFetching BBC News...")
    posts = scraper.fetch_feed('bbc', limit=5)
    
    print(f"\nFetched {len(posts)} posts:")
    for i, post in enumerate(posts, 1):
        print(f"\n{i}. {post['content_text'][:150]}...")
        print(f"   URL: {post['url']}")
        print(f"   Published: {post['created_at']}")
    
    # Fetch all news feeds
    print("\n\nFetching all news feeds...")
    news_posts = scraper.fetch_all_feeds(limit_per_feed=10, categories=['news'])
    print(f"Total news posts: {len(news_posts)}")
