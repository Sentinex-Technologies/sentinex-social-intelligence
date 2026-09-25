# System Architecture

**Sentinex Social Intelligence**  
High-level architecture for SIH26152 Social Media Analytics prototype.

---

## 🏗️ Overview

Sentinex is designed as a **modular, scalable social media analytics platform** with clear separation between data ingestion, processing, analysis, and presentation layers.

The system collects social media data from multiple platforms, processes it through various analytics engines, and presents insights through an interactive dashboard.

---

## 📊 High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      DATA SOURCES                           │
│  X/Twitter │ Instagram │ LinkedIn │ Telegram │ Facebook     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                 DATA INGESTION LAYER                        │
│  • Platform-specific scrapers/API clients                   │
│  • Rate limiting & error handling                           │
│  • Data normalization & validation                          │
│  • Timestamped storage                                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                DATA PROCESSING PIPELINE                     │
│  • Text cleaning & preprocessing                            │
│  • Entity extraction (mentions, hashtags, URLs)             │
│  • Language detection                                       │
│  • Deduplication & filtering                                │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  ANALYTICS ENGINE                           │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  Sentiment   │  │    Trend     │  │ Demographics │    │
│  │  & Emotion   │  │  Detection   │  │   Analysis   │    │
│  │   Analysis   │  │              │  │  (Aggregate) │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐                       │
│  │   Network    │  │   Temporal   │                       │
│  │  & Influence │  │   Analysis   │                       │
│  │   Analysis   │  │              │                       │
│  └──────────────┘  └──────────────┘                       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    API LAYER (REST)                         │
│  • GET /api/stats           - Overall statistics            │
│  • GET /api/sentiment       - Sentiment analysis results    │
│  • GET /api/trends          - Trending topics               │
│  • GET /api/demographics    - Aggregate insights            │
│  • GET /api/network         - Network analysis data         │
│  • GET /api/timeline        - Temporal analysis             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              VISUALIZATION DASHBOARD                        │
│  • Interactive charts & graphs                              │
│  • Real-time updates                                        │
│  • Explainable AI insights                                  │
│  • Export capabilities                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧩 Component Breakdown

### 1. Data Ingestion Layer

**Purpose:** Collect social media data from multiple platforms while respecting rate limits and terms of service.

**Responsibilities:**
- Platform-specific data collection (X, Instagram, LinkedIn, Telegram, Facebook)
- API integration with rate limiting
- Web scraping (when APIs unavailable)
- Data validation and normalization
- Timestamped storage for historical analysis

**Technologies:**
- Python 3.9+
- Requests library (API calls)
- Selenium/Playwright (web scraping when needed)
- SQLite (initial storage)

**Data Model:**
```python
{
  "post_id": "unique_identifier",
  "platform": "twitter | instagram | linkedin | telegram | facebook",
  "username": "anonymized_user_identifier",
  "timestamp": "2026-09-26T00:00:00Z",  # ISO 8601 format
  "text": "post content text",
  "media": ["url1", "url2"],
  "engagement": {
    "likes": 150,
    "comments": 25,
    "shares": 10,
    "views": 1500
  },
  "metadata": {
    "language": "en",
    "location": "region_code",  # Aggregated, not precise
    "hashtags": ["#ai", "#tech"],
    "mentions": ["@user1", "@user2"]
  }
}
```

---

### 2. Data Processing Pipeline

**Purpose:** Clean, normalize, and prepare raw social media data for analysis.

**Responsibilities:**
- Text preprocessing (lowercase, remove special characters, URLs)
- Tokenization and normalization
- Entity extraction (hashtags, mentions, URLs)
- Language detection and translation (if needed)
- Duplicate detection and removal
- Data quality checks

**Technologies:**
- Pandas (data manipulation)
- spaCy / NLTK (NLP preprocessing)
- Regular expressions
- langdetect (language detection)

**Pipeline Steps:**
```python
Raw Data
    ↓
Text Cleaning (remove URLs, special chars)
    ↓
Tokenization (split into words)
    ↓
Normalization (lowercase, lemmatization)
    ↓
Entity Extraction (hashtags, mentions)
    ↓
Language Detection
    ↓
Duplicate Removal
    ↓
Cleaned Data → Analytics
```

---

### 3. Analytics Engine

The core of Sentinex, consisting of multiple specialized analysis modules.

#### 3.1 Sentiment & Emotion Analysis

**Purpose:** Determine sentiment polarity and emotional tone of social media posts.

**Approach:**
- **VADER Sentiment Analysis** - Pre-trained on social media text
- **TextBlob** - Additional polarity scoring
- **Emotion Classification** - Detect emotions (joy, anger, sadness, fear, surprise, disgust)
- **Confidence Scores** - Provide explainability

**Input:**
```python
{
  "text": "I absolutely love the new AI features! This is amazing!"
}
```

**Output:**
```python
{
  "sentiment": "positive",
  "polarity": 0.85,  # Range: -1 (negative) to +1 (positive)
  "subjectivity": 0.75,  # Range: 0 (objective) to 1 (subjective)
  "emotions": {
    "joy": 0.90,
    "surprise": 0.60,
    "anger": 0.05,
    "sadness": 0.02,
    "fear": 0.01,
    "disgust": 0.01
  },
  "confidence": 0.92
}
```

**Use Cases:**
- Track public sentiment over time
- Identify negative/positive trending topics
- Alert on sentiment spikes (crisis detection)

---

#### 3.2 Trend Detection & Topic Analysis

**Purpose:** Identify emerging topics, trending hashtags, and viral narratives.

**Approach:**
- **TF-IDF** (Term Frequency-Inverse Document Frequency) for keyword extraction
- **Hashtag frequency analysis** - Track trending hashtags
- **Time-based trending** - Measure velocity of topic growth
- **Topic clustering** - Group related discussions
- **N-gram analysis** - Detect common phrases

**Output:**
```python
{
  "trending_topics": [
    {
      "topic": "climate action",
      "growth_rate": "+45%",
      "post_count": 1250,
      "sentiment": "positive",
      "peak_time": "2026-09-25T14:00:00Z"
    },
    {
      "topic": "AI innovation",
      "growth_rate": "+32%",
      "post_count": 980,
      "sentiment": "neutral",
      "peak_time": "2026-09-25T16:30:00Z"
    }
  ],
  "trending_hashtags": [
    {"tag": "#ClimateAction", "count": 1520, "growth": "+45%"},
    {"tag": "#AIRevolution", "count": 1100, "growth": "+32%"}
  ],
  "emerging_narratives": [
    {
      "narrative": "renewable energy adoption",
      "keywords": ["solar", "wind", "green energy"],
      "velocity": "high",
      "community_clusters": [1, 3, 5]
    }
  ]
}
```

---

#### 3.3 Demographic Analysis (Aggregate Only)

**Purpose:** Provide anonymized, aggregate demographic insights without individual profiling.

**Approach:**
- Age group binning (18-24, 25-34, 35-44, 45+)
- Geographic region aggregation (no precise locations)
- Platform usage patterns
- Engagement patterns by demographic
- **Privacy-first:** All data is aggregated and anonymized

**Output:**
```python
{
  "age_distribution": {
    "18-24": 30,  # Percentage
    "25-34": 40,
    "35-44": 20,
    "45+": 10
  },
  "region_distribution": {
    "North": 25,
    "South": 25,
    "East": 25,
    "West": 25
  },
  "platform_usage": {
    "twitter": 45,
    "instagram": 30,
    "linkedin": 15,
    "facebook": 10
  },
  "engagement_by_age": {
    "18-24": {"avg_likes": 15, "avg_comments": 3},
    "25-34": {"avg_likes": 20, "avg_comments": 5}
  },
  "total_users_analyzed": 5000,  # Aggregate count only
  "privacy_note": "All data is anonymized and aggregated"
}
```

**Privacy Commitment:**
- ✅ No individual user tracking
- ✅ No personal information stored
- ✅ Aggregate patterns only
- ✅ Anonymized identifiers

---

#### 3.4 Network & Influence Analysis

**Purpose:** Map social connections, identify influential users, and detect communities.

**Approach:**
- **Graph construction** - Users as nodes, interactions as edges
- **Community detection** - Louvain algorithm for clustering
- **Centrality measures**:
  - Degree centrality (most connected)
  - Betweenness centrality (bridges between communities)
  - Eigenvector centrality (connected to influential users)
- **Influence scoring** - Combine engagement, reach, and centrality

**Technologies:**
- NetworkX (graph analysis)
- Community detection algorithms
- Graph visualization libraries

**Output:**
```python
{
  "communities": [
    {
      "community_id": 1,
      "size": 150,
      "primary_topic": "tech enthusiasts",
      "avg_sentiment": 0.65,
      "key_hashtags": ["#AI", "#innovation"]
    },
    {
      "community_id": 2,
      "size": 120,
      "primary_topic": "climate activists",
      "avg_sentiment": 0.55,
      "key_hashtags": ["#ClimateAction", "#sustainability"]
    }
  ],
  "influencers": [
    {
      "user_id": "anonymous_user_123",
      "influence_score": 0.89,
      "community": 1,
      "reach": 5000,
      "engagement_rate": 0.12,
      "centrality": {
        "degree": 0.85,
        "betweenness": 0.72,
        "eigenvector": 0.90
      }
    }
  ],
  "network_stats": {
    "total_nodes": 500,
    "total_edges": 1250,
    "avg_degree": 2.5,
    "clustering_coefficient": 0.35,
    "communities_detected": 5
  }
}
```

---

#### 3.5 Temporal Analysis

**Purpose:** Track trends, sentiment, and engagement over time.

**Approach:**
- Time-series data aggregation
- Moving averages for smoothing
- Seasonality detection
- Event correlation (spikes, drops)
- Forecasting (basic trend projection)

**Output:**
```python
{
  "time_series": [
    {
      "date": "2026-09-01",
      "post_count": 1200,
      "avg_sentiment": 0.60,
      "trending_topics": ["topic1", "topic2"]
    },
    {
      "date": "2026-09-02",
      "post_count": 1350,
      "avg_sentiment": 0.70,
      "trending_topics": ["topic2", "topic3"]
    }
  ],
  "sentiment_trend": {
    "direction": "increasing",
    "change_rate": "+5% per day",
    "prediction_7d": 0.75
  },
  "peak_activity_hours": [14, 18, 20],  # Hours of day
  "weekly_pattern": {
    "monday": 1200,
    "tuesday": 1300,
    "wednesday": 1400,
    "thursday": 1350,
    "friday": 1500,
    "saturday": 1000,
    "sunday": 900
  }
}
```

---

### 4. API Layer (REST)

**Purpose:** Expose analytics results through RESTful API endpoints.

**Technology:** FastAPI (Python)

**Endpoints:**

```
GET  /api/stats
     → Overall statistics (total posts, users, sentiment summary)
     
GET  /api/sentiment?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&platform=twitter
     → Sentiment analysis results with filters
     
GET  /api/trends?limit=10&sort=growth
     → Top trending topics and hashtags
     
GET  /api/demographics
     → Aggregate demographic insights
     
GET  /api/network?community_id=1
     → Network analysis data for specific community
     
GET  /api/timeline?metric=sentiment&granularity=daily&days=30
     → Temporal analysis time-series data
     
GET  /api/influence?min_score=0.7
     → List of influential users/accounts
     
POST /api/analyze
     → Analyze custom text input for sentiment
```

**Response Format:**
```json
{
  "success": true,
  "data": { ... },
  "metadata": {
    "timestamp": "2026-09-26T00:00:00Z",
    "query_time_ms": 45,
    "record_count": 100
  }
}
```

---

### 5. Visualization Dashboard

**Purpose:** Interactive web-based dashboard for exploring analytics.

**Technology:** React + Vite + Recharts/D3.js + TailwindCSS

**Components:**

1. **Overview Dashboard**
   - Key metrics cards (total posts, avg sentiment, trending topics)
   - Sentiment distribution pie chart
   - Timeline graph (posts over time)
   - Top hashtags word cloud

2. **Sentiment Analysis View**
   - Sentiment breakdown (positive/negative/neutral)
   - Emotion wheel visualization
   - Sentiment timeline with events
   - Filter by platform, date range

3. **Trending Topics View**
   - Real-time trending topics list
   - Growth rate indicators
   - Topic sentiment heatmap
   - Related hashtags network

4. **Demographics View**
   - Age distribution bar chart
   - Geographic heatmap (regional)
   - Platform usage pie chart
   - Engagement patterns by demographic

5. **Network Analysis View**
   - Force-directed graph visualization
   - Community clusters
   - Influence leaderboard
   - Connection explorer

6. **Timeline Analysis View**
   - Multi-metric time-series
   - Comparison charts
   - Event markers
   - Trend predictions

---

## 🔄 Data Flow

```
1. Social Media Post Published
   ↓
2. Ingestion Layer (scraper/API) collects post
   ↓
3. Validation & Normalization
   ↓
4. Storage (SQLite database with timestamp)
   ↓
5. Processing Pipeline (cleaning, entity extraction)
   ↓
6. Analytics Engine (sentiment, trends, network, etc.)
   ↓
7. Results Storage (analytics cache)
   ↓
8. API Layer exposes results via REST endpoints
   ↓
9. Dashboard fetches and visualizes data
   ↓
10. User interacts and explores insights
```

---

## 🔐 Security & Privacy Architecture

**Data Protection:**
- Anonymized user identifiers (no real usernames stored)
- Encrypted data at rest
- Secure API endpoints (CORS, rate limiting)
- No storage of passwords or sensitive credentials
- Environment-based configuration (.env)

**Privacy Principles:**
- **Aggregate Only** - Demographic insights are never individualized
- **Minimal Retention** - Data stored only as long as needed
- **No Profiling** - No individual user behavior tracking
- **Transparency** - Clear explanation of what data is collected and why

**Access Control:**
- Read-only dashboard (no public write access)
- Internal analytics only
- No public API exposure (for demo)

---

## 📦 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend API** | Python 3.9+, FastAPI | REST API server |
| **Data Storage** | SQLite (prototype), PostgreSQL (production) | Persistent data storage |
| **Data Processing** | Pandas, NumPy | Data manipulation & analysis |
| **NLP** | spaCy, TextBlob, VADER | Text processing & sentiment |
| **Network Analysis** | NetworkX | Graph algorithms |
| **Frontend** | React 18, Vite | User interface |
| **Visualization** | Recharts, D3.js | Charts & graphs |
| **Styling** | TailwindCSS | UI design |
| **Testing** | pytest, Jest | Automated testing |

---

## 🚀 Deployment Architecture

### Prototype (Current)

```
┌────────────────────────────────────┐
│      Local Development Server      │
│                                    │
│  Backend (FastAPI) :8000          │
│  Frontend (Vite) :5173            │
│  Database (SQLite file)           │
│  No authentication                │
└────────────────────────────────────┘
```

### Production (Future)

```
┌─────────────────────────────────────────┐
│         Load Balancer / CDN             │
└─────────────┬───────────────────────────┘
              │
    ┌─────────┴──────────┐
    ▼                    ▼
┌─────────┐        ┌─────────┐
│Frontend │        │Frontend │
│ Server  │        │ Server  │
│ (Nginx) │        │ (Nginx) │
└─────────┘        └─────────┘
    │                    │
    └─────────┬──────────┘
              ▼
    ┌──────────────────┐
    │   API Gateway    │
    │  (Rate Limiting) │
    └─────────┬────────┘
              │
    ┌─────────┴──────────┐
    ▼                    ▼
┌─────────┐        ┌─────────┐
│ Backend │        │ Backend │
│  API    │        │  API    │
│(FastAPI)│        │(FastAPI)│
└────┬────┘        └────┬────┘
     │                  │
     └─────────┬────────┘
               ▼
     ┌──────────────────┐
     │    PostgreSQL    │
     │   + Redis Cache  │
     └──────────────────┘
```

---

## 📈 Scalability Considerations

### Current Capacity (Prototype)
- ~1,000 - 10,000 posts
- Single server
- SQLite database
- Synchronous processing
- Local deployment

### Future Scaling (Production)
- Millions of posts
- Distributed architecture
- PostgreSQL with sharding
- Asynchronous task queues (Celery + Redis)
- Horizontal scaling with load balancing
- CDN for frontend assets
- Microservices architecture (optional)

---

## 🧪 Testing Strategy

**Unit Tests:**
- Sentiment analysis accuracy
- Trend detection algorithms
- Network analysis calculations
- Data processing functions

**Integration Tests:**
- API endpoints
- Database operations
- Complete data pipeline flow

**UI Tests:**
- Dashboard component rendering
- Visualization accuracy
- User interaction flows

**Performance Tests:**
- API response time
- Database query optimization
- Large dataset handling

---

## 📊 Monitoring & Logging (Future)

- Application logs (errors, warnings, info)
- Performance metrics (response time, throughput)
- User analytics (dashboard usage)
- Error tracking (Sentry or similar)
- Uptime monitoring

---

## 🔮 Future Enhancements

1. **Real-time Stream Processing**
   - Live social media feeds
   - WebSocket updates to dashboard
   - Real-time alerts

2. **Advanced ML Models**
   - Custom trained transformers (BERT, GPT)
   - Multi-language sentiment analysis
   - Fake news detection
   - Bot detection

3. **Enhanced Network Analysis**
   - Influence propagation modeling
   - Echo chamber detection
   - Misinformation tracking

4. **Mobile Application**
   - iOS/Android apps
   - Push notifications
   - Mobile-optimized visualizations

5. **Automated Reporting**
   - Scheduled PDF reports
   - Email digests
   - Customizable alerts

---

## 📝 Design Principles

**Modularity:**
- Each component is independent and replaceable
- Clear interfaces between layers
- Easy to add new analytics modules

**Scalability:**
- Horizontal scaling capability
- Async processing for heavy workloads
- Caching strategies

**Maintainability:**
- Clean code architecture
- Comprehensive documentation
- Automated testing
- Version control with Git

**Privacy & Ethics:**
- Aggregate insights only
- No individual tracking
- Transparent AI
- Responsible data handling

---

## 🎯 Summary

Sentinex Social Intelligence is architected as a **modular, privacy-first, scalable analytics platform** that:

✅ Collects data from multiple social media platforms  
✅ Processes and analyzes using multiple AI/ML techniques  
✅ Provides aggregate, anonymized insights  
✅ Presents results through an interactive dashboard  
✅ Maintains security and privacy throughout  
✅ Scales from prototype to production  

**Organization:** Sentinex Technologies  
**Project:** SIH26152 - Social Media Analytics
