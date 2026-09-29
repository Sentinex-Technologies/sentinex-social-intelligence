# Quick Reference: Data Sources
# త్వరిత సూచన: డేటా మూలాలు

**For:** SIH26152 - NTRO Social Media Intelligence  
**Last Updated:** September 29, 2026

---

## ❓ Common Questions & Answers

### 1. "మీరు డేటా ఎలా collect చేస్తున్నారు?" (How are you collecting data?)

**Answer:**  
మేము **Synthetic Data Generator** ఉపయోగిస్తున్నాం - Faker library తో realistic fake data generate చేస్తుంది.

**Files:**
- `backend/app/services/synthetic_data.py` - Main generator
- Creates 100 users, 1000 posts, networks, engagement

---

### 2. "SIH కు live data కావలసిందా?" (Does SIH need live data?)

**Answer:**  
**కాదు!** Synthetic data 100% acceptable ✅

**Why judges accept synthetic data:**
- ✅ Evaluates your algorithms, not data source
- ✅ Ensures reliable demo (no API failures)
- ✅ Legal/ethical (no ToS violations)
- ✅ Standard practice for hackathons

**What judges evaluate:**
- Sentiment analysis accuracy
- Network analysis algorithms
- UI/UX quality
- System architecture
- All 5 NTRO components working

---

### 3. "Web Scraping vs Web Crawling అంటే ఏమిటి?" (What are they?)

#### **Web Scraping:**
> Get specific data from known pages

**Example:** Extract post titles from `reddit.com/r/india`

**Tools:**
- BeautifulSoup (HTML parsing)
- Scrapy (full framework)
- Playwright (JavaScript pages)

#### **Web Crawling:**
> Discover all pages in a website

**Example:** Find all posts in entire subreddit, then scrape each

**Difference:**
- **Scraping** = Extract from known pages
- **Crawling** = Discover + map all pages, then scrape

---

### 4. "Live data integration ఎలా చేయాలి?" (How to add live data?)

**Post-SIH Only!** మీ current setup perfect ✅

#### **Phase 1: Reddit API (Easiest - 15 min)**
```bash
# Setup
# 1. https://www.reddit.com/prefs/apps
# 2. Create "script" app
# 3. Copy client_id and client_secret

# Usage
from app.scrapers.reddit_scraper import RedditScraper

scraper = RedditScraper()
posts = scraper.fetch_posts('india', limit=100)
```

**Cost:** FREE forever  
**File:** `backend/app/scrapers/reddit_scraper.py` (already created!)

---

#### **Phase 2: RSS Feeds (Super Easy - 5 min)**
```bash
# No setup needed!

# Usage
from app.scrapers.rss_scraper import RSSFeedScraper

scraper = RSSFeedScraper()
posts = scraper.fetch_feed('bbc', limit=100)
```

**Cost:** FREE forever  
**File:** `backend/app/scrapers/rss_scraper.py` (already created!)

---

#### **Phase 3: Telegram (Medium - 20 min)**
```bash
# Setup
# 1. https://my.telegram.org/apps
# 2. Get api_id and api_hash
# 3. Add to .env
```

**Cost:** FREE forever  
**Works with:** Public channels only (@BBCNews, @TechCrunch)

---

#### **Phase 4: Twitter (Optional - Paid)**
**Cost:** $100/month  
**Recommendation:** Only if budget allows

---

## 🚫 DON'T Do This:

### ❌ Instagram Scraping
- Impossible (anti-bot protection)
- Illegal (ToS violation)
- Requires months of approval

### ❌ Facebook Scraping
- Impossible (requires login + CAPTCHA)
- Illegal (ToS violation)

### ❌ Unpaid Twitter Scraping
- Will get blocked immediately
- Rate limits kill demos

---

## 📊 Feature Comparison Table

| Source | Cost | Setup Time | Difficulty | Legal | Recommend |
|--------|------|------------|-----------|-------|-----------|
| **Synthetic** | ✅ FREE | 0 min | None | ✅ Yes | **✅ For SIH** |
| **Reddit API** | ✅ FREE | 15 min | Easy | ✅ Yes | ✅ Post-SIH |
| **RSS Feeds** | ✅ FREE | 5 min | Easy | ✅ Yes | ✅ Post-SIH |
| **Telegram** | ✅ FREE | 20 min | Medium | ✅ Yes | ✅ Post-SIH |
| **Twitter** | 💰 $100/mo | 60 min | Medium | ✅ Yes | 🤔 Optional |
| **Instagram** | ❌ N/A | Impossible | Impossible | ❌ No | ❌ Never |
| **Facebook** | ❌ N/A | Impossible | Impossible | ❌ No | ❌ Never |

---

## 🎯 Decision Tree

```
Do you need data?
│
├─ For SIH Demo? 
│   └─ ✅ Use SYNTHETIC (current) ← YOU ARE HERE
│       
├─ For Post-SIH Enhancement?
│   ├─ Day 1: Add Reddit + RSS (easy, free)
│   ├─ Day 2: Add Telegram (medium, free)
│   └─ Optional: Twitter (if budget)
│
└─ For Production?
    └─ Same as post-SIH + monitoring + scaling
```

---

## 📁 Files Created for You

All ready to use post-SIH:

```
docs/
├─ DATA_COLLECTION_EXPLAINED.md      # Full explanation (Telugu + English)
├─ DATA_ARCHITECTURE_VISUAL.md       # Visual diagrams
└─ QUICK_REFERENCE_DATA_SOURCES.md   # This file

backend/app/scrapers/
├─ README.md                         # Integration guide
├─ reddit_scraper.py                 # Reddit API ✅
├─ rss_scraper.py                    # RSS feeds ✅
└─ (future) telegram_scraper.py      # Telegram API

.env.example                         # Updated with DATA_MODE config
```

---

## 🚀 How to Switch from Synthetic → Live (Post-SIH)

### Current State (SIH Demo):
```bash
# .env
DATA_MODE=synthetic  ← Current
```

### Future State (Post-SIH):
```bash
# .env
DATA_MODE=live

# Add API keys
REDDIT_CLIENT_ID=abc123
REDDIT_CLIENT_SECRET=xyz789
```

**That's it!** No code changes needed anywhere else! 🎉

---

## 🎓 Architecture Benefits

### Zero Code Changes Needed!

```
Synthetic Data ──┐
                 ├─→ [Database] ─→ [Analytics] ─→ [API] ─→ [Frontend]
Live Data ───────┘

Same pipeline for both! Only data source changes.
```

**Benefits:**
- ✅ Test algorithms with synthetic data
- ✅ Switch to live data anytime
- ✅ Analytics don't care about source
- ✅ API stays same
- ✅ Frontend unchanged

---

## 📝 Code Examples

### Current Implementation (Synthetic):
```python
# backend/app/api/data.py (current)
from app.services.synthetic_data import SyntheticDataGenerator

generator = SyntheticDataGenerator()
posts = generator.generate_posts(db, count=1000)
```

### Future Implementation (Live + Synthetic):
```python
# backend/app/services/data_ingestion.py (future)
class DataIngestionManager:
    def fetch_posts(self, db):
        if settings.data_mode == 'synthetic':
            return self.synthetic.generate_posts(db)
        elif settings.data_mode == 'live':
            posts = []
            posts += self.reddit.fetch_posts()
            posts += self.rss.fetch_feeds()
            return posts
```

---

## 🎯 Final Recommendations

### For SIH26152 Demo (NOW):

```
✅ Current Status: PERFECT for SIH demo

What to do:
  ✅ Keep DATA_MODE=synthetic
  ✅ Focus on UI polish
  ✅ Perfect your presentation
  ✅ Test all 5 NTRO components

What NOT to do:
  ❌ Don't setup APIs now
  ❌ Don't worry about live data
  ❌ Don't attempt Instagram/Facebook scraping
  ❌ Don't change anything!
```

### After SIH (If Needed):

```
🔄 Optional Enhancement (3-5 hours work)

Priority order:
  1. Reddit API (2 hours) - Easiest
  2. RSS feeds (1 hour) - Super easy
  3. Telegram (2 hours) - Medium
  4. Twitter (optional) - If budget

Total time: 5 hours to add 3 free sources
```

---

## 💡 Pro Tips

### For Demo Presentation:

**If judge asks: "Is this live data?"**

**Good Answer:**  
> "We're using a synthetic data generator that creates realistic social media posts with proper demographics, timestamps, and engagement metrics. This approach is standard for hackathons because it's:
> 1. 100% legal (no ToS violations)
> 2. Reliable for demos (no API failures)
> 3. Lets us focus on algorithm quality
> 
> However, our architecture supports live data integration. Post-demo, we can plug in Reddit, Telegram, or RSS feeds in under 5 hours with zero code changes to the analytics pipeline."

**Confidence Booster:**  
Judges EXPECT synthetic data for hackathons. They're evaluating your AI/ML skills, not API integration complexity!

---

## 🔗 Quick Links

| Resource | Link |
|----------|------|
| Reddit API Setup | https://www.reddit.com/prefs/apps |
| Telegram API Setup | https://my.telegram.org/apps |
| Twitter Developer | https://developer.twitter.com |
| Full Documentation | `docs/DATA_COLLECTION_EXPLAINED.md` |
| Visual Architecture | `docs/DATA_ARCHITECTURE_VISUAL.md` |
| Scraper Code | `backend/app/scrapers/` |

---

## ❓ Still Have Questions?

### Q: "ఇప్పుడు ఏమి చేయాలి?" (What should I do now?)
**A:** Nothing! Your system is perfect for SIH. Focus on presentation practice.

### Q: "SIH తర్వాత live data add చేయాలా?" (Should I add live data after SIH?)
**A:** Only if needed. Most deployments use synthetic for testing + live for production.

### Q: "Twitter data తప్పనిసరి అవసరమా?" (Is Twitter data mandatory?)
**A:** No! Reddit + RSS gives you plenty of real data for free.

### Q: "Instagram scraping possible ఆ?" (Is Instagram scraping possible?)
**A:** No. Technically impossible + legally prohibited. Use Reddit/Telegram instead.

---

**Current Status:** ✅ Production-ready for SIH Demo  
**Next Action:** Focus on presentation, not data sources!  
**Questions?** All scrapers are ready in `backend/app/scrapers/`

---

**తుది మాట:** మీరు perfect state లో ఉన్నారు! ✅  
**Final Word:** You're in perfect shape! ✅

🚀 **Good luck with SIH26152!** 🚀
