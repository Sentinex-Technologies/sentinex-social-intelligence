# Sentinex Social Intelligence - Frontend Dashboard

Beautiful, responsive dashboard for visualizing social media analytics.

## Features

✅ **NTRO Components Status** - Real-time tracking of all 5 components  
✅ **Data Statistics** - User count, post count, platform distribution  
✅ **Sentiment Analysis** - Positive/negative/neutral distribution  
✅ **Network Analysis** - Users, connections, network density  
✅ **Emotion Distribution** - Sarcasm, anxiety, excitement, supportive, against  
✅ **Trending Topics** - Hot topics and hashtags  

## Quick Start

### 1. Start Backend Server
```bash
cd ../backend
./venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 2. Open Dashboard
Open `index.html` in your browser, or use a simple HTTP server:

```bash
# Python 3
python3 -m http.server 3000

# Or Node.js
npx http-server -p 3000
```

Then visit: http://localhost:3000

## Features

- **Real-time Updates**: Auto-refreshes every 30 seconds
- **Interactive**: Generate demo data and analyze sentiment with one click
- **Responsive**: Works on desktop, tablet, and mobile
- **Beautiful UI**: Modern gradient design with smooth animations

## API Integration

The dashboard connects to:
- `http://localhost:8000/api/data/*` - Data management
- `http://localhost:8000/api/sentiment/*` - Sentiment analysis
- `http://localhost:8000/api/network/*` - Network analysis
- `http://localhost:8000/api/posts/*` - Post analytics

## Demo Workflow

1. Click "Generate Demo Data" - Creates 100 users and 500 posts
2. Click "Analyze Sentiments" - Runs multi-dimensional sentiment analysis
3. Watch the dashboard populate with:
   - Sentiment distribution
   - Emotion scores (Component B)
   - Network topology metrics (Component E)
   - Trending topics (Component D)

## Screenshots

All 5 NTRO components visualized in one dashboard! 🎯
