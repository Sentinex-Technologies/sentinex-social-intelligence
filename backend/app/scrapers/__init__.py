"""
Live Data Scrapers Package

Optional scrapers for post-SIH live data integration.
Current SIH demo uses synthetic data (recommended).

Available scrapers:
- RedditScraper: Fetch posts from Reddit (FREE, easy)
- RSSFeedScraper: Fetch from RSS feeds (FREE, easiest)
- TelegramScraper: Fetch from Telegram channels (FREE, medium)

Not recommended:
- Twitter: Paid ($100/month)
- Instagram/Facebook: Impossible (anti-bot protection)
"""

from .reddit_scraper import RedditScraper
from .rss_scraper import RSSFeedScraper

__all__ = ['RedditScraper', 'RSSFeedScraper']
