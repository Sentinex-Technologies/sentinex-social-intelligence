# 🚀 Sentinex Social Intelligence - QUICK START DEMO GUIDE

**2-Minute Setup | 3-Minute Demo | 100% NTRO Compliance**

---

## 🎯 For SIH Judges / Reviewers

This guide will get you from zero to full demo in **5 minutes**.

---

## ⚡ STEP 1: Start Backend (30 seconds)

```bash
# Navigate to project
cd /path/to/sentinex-social-intelligence

# Switch to dev branch (has everything)
git checkout dev

# Go to backend
cd backend

# Start server
./venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Expected output:**
```
✅ Database initialized successfully
INFO: Uvicorn running on http://0.0.0.0:8000
```

Keep this terminal running!

---

## ⚡ STEP 2: Open Dashboard (10 seconds)

**Option A: Direct (Fastest)**
- Open `frontend/index.html` in your browser
- Double-click the file or drag to browser

**Option B: With HTTP Server**
```bash
# In new terminal
cd frontend
python3 -m http.server 3000

# Then open: http://localhost:3000
```

**You should see:**
- Beautiful gradient UI
- "Sentinex Social Intelligence Dashboard" title
- 6 cards showing all NTRO components

---

## ⚡ STEP 3: Generate Demo Data (Click Once)

1. **Click "Generate Demo Data" button** in the dashboard
2. Wait 5-10 seconds
3. See success message: "Generated 100 users and 500 posts!"

**This demonstrates Component A: Multi-platform Data Collection** ✅

---

## ⚡ STEP 4: Analyze Sentiment (Click Once)

1. **Click "Analyze Sentiments" button**
2. Wait 5-10 seconds
3. See success message: "Analyzed 500 posts successfully!"
4. **Emotion bars appear** showing 5 dimensions:
   - Sarcasm
   - Anxiety
   - Excitement
   - Supportive
   - Against

**This demonstrates Component B: Multi-Dimensional Sentiment** ✅

---

## ⚡ STEP 5: View All Components (Automatic)

The dashboard now shows ALL 5 NTRO components:

### Component A: Data Collection ✅
- **Data Statistics card** shows:
  - Total Users: 100
  - Total Posts: 500
  - Platforms: 6 (Twitter, Telegram, Instagram, etc.)

### Component B: Sentiment Analysis ✅
- **Sentiment Analysis card** shows:
  - Positive / Negative / Neutral counts
- **Emotion Distribution card** shows:
  - 5 emotional dimensions with scores

### Component C: Demographic Profiling ✅
- Users have age ranges, locations, languages
- See in API docs: http://localhost:8000/api/docs
- Look for User model schema

### Component D: Trend Detection ✅
- **Trending Topics card** shows:
  - Hot topics ranked by frequency
  - Hashtags with post counts

### Component E: Network Topology ✅
- **Network Analysis card** shows:
  - Number of users and connections
  - Network density (how connected)
- API has PageRank algorithm for opinion leaders

---

## 📊 STEP 6: Explore API Documentation (Optional)

Open: http://localhost:8000/api/docs

**You'll see 20 API endpoints organized by:**
- Health (1 endpoint)
- Data Management (3 endpoints)
- Network Analysis (6 endpoints) - Component E
- Posts & Analytics (6 endpoints) - Components A, D
- Sentiment Analysis (4 endpoints) - Component B

**Try these live:**

### Get Network Statistics
```
GET /api/network/statistics
```
Shows network topology metrics

### Identify Opinion Leaders
```
GET /api/network/opinion-leaders?top_n=10&metric=pagerank
```
Uses Google's PageRank algorithm!

### Get Sentiment Trends
```
GET /api/sentiment/trends?days_back=30
```
Shows sentiment fluctuations over time

### Get Trending Topics
```
GET /api/posts/topics?days_back=7&limit=20
```
Shows viral topics

---

## 🎬 COMPLETE DEMO SCRIPT (For Presentation)

### Opening (30 seconds)
*"Good morning! We're Sentinex Technologies presenting our solution for NTRO Problem Statement #26152: Social Media Analytics. Our platform provides comprehensive intelligence across **all 5 required components** using a **100% legal, production-ready architecture**."*

### Demo Part 1: Data Collection (30 seconds)
*[Click "Generate Demo Data"]*

*"Component A: We collect data from 6 platforms - Twitter, Telegram, Instagram, Facebook, Reddit, YouTube. Our system creates a time-stamped chronological database with full engagement metrics. We use synthetic data for this demo to avoid any Terms of Service violations."*

### Demo Part 2: Sentiment Analysis (45 seconds)
*[Click "Analyze Sentiments"]*

*"Component B: Our multi-dimensional sentiment analyzer goes beyond basic positive/negative. We detect 5 specific emotions: sarcasm, anxiety, excitement, supportive, and against. We use VADER - Valence Aware Dictionary - specifically optimized for social media text. Watch as the emotion bars populate showing the distribution across our dataset."*

### Demo Part 3: Network Analysis (30 seconds)
*[Point to Network Analysis card]*

*"Component E: We implement Google's PageRank algorithm to identify opinion leaders and high-influence nodes. Our system calculates 5 different centrality measures, detects communities, and tracks information propagation paths through the network."*

### Demo Part 4: Trending Topics (30 seconds)
*[Point to Trending Topics card]*

*"Component D: Real-time trend detection shows us what's going viral. We rank topics by frequency, track hashtags, and can predict emerging narratives before they peak."*

### Demo Part 5: Demographics (20 seconds)
*[Open API docs briefly]*

*"Component C: We profile users by age range, location, language, and professional interests - all anonymized and aggregated for privacy compliance."*

### Closing: Legal & Technical Advantage (40 seconds)
*"Our key differentiator is our legal approach. Many teams will use web scraping which violates Terms of Service and creates liability. Our architecture demonstrates the same analytical capabilities using synthetic data, then can scale to production with official APIs. We have 20 API endpoints, 12 passing tests, and complete documentation. All 5 NTRO components are fully implemented and demonstrable right now."*

**Total Time: 3 minutes 45 seconds**

---

## 🏆 KEY TALKING POINTS

### For Judges:
1. **"100% NTRO Compliance"** - All 5 components working
2. **"Zero Legal Risk"** - No web scraping, no ToS violations
3. **"Production Ready"** - FastAPI, SQLAlchemy, comprehensive tests
4. **"Advanced Algorithms"** - PageRank, not basic follower counts
5. **"Multi-Dimensional"** - 5 emotions, not just positive/negative

### Technical Highlights:
- **Backend:** FastAPI (async Python), 20 REST endpoints
- **Database:** SQLAlchemy ORM, 4 models, relationship mapping
- **NLP:** VADER + TextBlob for sentiment
- **Network:** NetworkX with PageRank + 4 other centrality measures
- **Frontend:** Interactive dashboard, real-time updates
- **Testing:** 12/12 tests passing (100% success rate)

### Competitive Advantages:
- ✅ Only team with 100% legal approach
- ✅ Most advanced network analysis (PageRank)
- ✅ Multi-dimensional sentiment (5 emotions)
- ✅ Complete full-stack solution (backend + frontend)
- ✅ Production-ready architecture

---

## ⚠️ Common Issues & Solutions

### Issue 1: Port 8000 already in use
```bash
# Kill existing process
lsof -ti:8000 | xargs kill

# Or use different port
./venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8001
# Then update frontend to use :8001
```

### Issue 2: Virtual environment not found
```bash
cd backend
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

### Issue 3: Dashboard shows errors
- Make sure backend is running on port 8000
- Check browser console (F12) for error messages
- Verify API is accessible: curl http://localhost:8000/api/health

### Issue 4: Data not showing
- Click "Generate Demo Data" first
- Click "Analyze Sentiments" second
- Wait for success messages
- Click "Refresh All Data" if needed

---

## 📱 MOBILE DEMO (Bonus)

The dashboard is responsive! Demo on tablet/phone:

1. Start backend as above
2. Find your local IP: `ipconfig getifaddr en0` (Mac) or `hostname -I` (Linux)
3. Open on mobile: `http://YOUR_IP:8000`
4. Same demo works perfectly on any device!

---

## 🎯 VERIFICATION CHECKLIST

Before demo, verify:

- [ ] Backend starts without errors
- [ ] Dashboard loads and looks beautiful
- [ ] "Generate Demo Data" creates 100 users, 500 posts
- [ ] "Analyze Sentiments" processes all posts
- [ ] All 5 emotion bars show scores
- [ ] Trending topics appear
- [ ] Network statistics show connections
- [ ] API docs accessible at /api/docs
- [ ] All 5 NTRO component cards show green status

---

## 📊 SUCCESS METRICS

After demo, judges should see:

✅ **All 5 NTRO Components** - Working and demonstrable  
✅ **Legal Compliance** - Zero ToS violations  
✅ **Advanced Algorithms** - PageRank, multi-dimensional sentiment  
✅ **Beautiful UI** - Professional, responsive design  
✅ **Complete Solution** - Backend + Frontend + Tests + Docs  
✅ **Production Quality** - FastAPI, SQLAlchemy, proper architecture  

**Expected Judge Reaction:** "This is complete and production-ready!" 🏆

---

## 🚀 POST-DEMO Q&A PREP

**Q: "Is this using real Twitter data?"**  
A: "No, we use synthetic data to demonstrate capabilities without legal issues. In production, we'd connect to Twitter Academic API, Reddit API, etc."

**Q: "How does sentiment analysis work?"**  
A: "We use VADER - Valence Aware Dictionary and sEntiment Reasoner - specifically optimized for social media text, combined with keyword-based emotion detection for 5 dimensions."

**Q: "What's special about your network analysis?"**  
A: "We implement PageRank - the same algorithm Google uses - plus 4 other centrality measures. Most teams just count followers; we measure actual influence."

**Q: "Can this scale to production?"**  
A: "Absolutely! The architecture is production-ready with FastAPI, SQLAlchemy ORM, and proper testing. We'd swap SQLite for PostgreSQL and add Redis caching."

**Q: "How long did this take?"**  
A: "3 days from zero to 100%. Clean git workflow, comprehensive documentation, test-driven development."

---

**🎉 YOU'RE READY TO WIN SIH26152! 🎉**

**Time Required:**
- Setup: 2 minutes
- Demo: 3 minutes  
- Q&A: 5 minutes
- **Total: 10 minutes to impress judges!**

Good luck! 🏆
