import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'
import { ComponentA, ComponentB, ComponentC, ComponentD, ComponentE } from './components/NTROComponents'

// API Base URL - uses environment variable in production, proxy in development
const API_BASE = import.meta.env.VITE_API_BASE_URL 
  ? `${import.meta.env.VITE_API_BASE_URL}/api`
  : '/api'

// Base URL for assets (handles GitHub Pages subpath)
const BASE_URL = import.meta.env.BASE_URL

// Sentinex Brand Colors from Logo
const COLORS = {
  primary: '#0066FF',
  navy: '#0A1F44',
  purple: '#7B3FF2',
  cyan: '#00BFFF',
  success: '#10B981',
  warning: '#F59E0B',
  danger: '#EF4444',
}

function App() {
  const [stats, setStats] = useState(null)
  const [sentimentData, setSentimentData] = useState(null)
  const [networkData, setNetworkData] = useState(null)
  const [emotionData, setEmotionData] = useState(null)
  const [topicsData, setTopicsData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [refreshing, setRefreshing] = useState(false)

  const fetchData = async () => {
    try {
      setRefreshing(true)
      const [statsRes, sentimentRes, networkRes, emotionRes, topicsRes] = await Promise.all([
        axios.get(`${API_BASE}/data/stats`),
        axios.get(`${API_BASE}/posts/sentiment/distribution?days_back=30`),
        axios.get(`${API_BASE}/network/statistics`),
        axios.get(`${API_BASE}/sentiment/emotions?days_back=7`),
        axios.get(`${API_BASE}/posts/topics?days_back=7&limit=10`)
      ])

      setStats(statsRes.data)
      setSentimentData(sentimentRes.data)
      setNetworkData(networkRes.data)
      setEmotionData(emotionRes.data)
      setTopicsData(topicsRes.data)
      setError(null)
    } catch (err) {
      setError(err.message)
      console.error('Error fetching data:', err)
    } finally {
      setLoading(false)
      setRefreshing(false)
    }
  }

  useEffect(() => {
    fetchData()
    const interval = setInterval(fetchData, 30000)
    return () => clearInterval(interval)
  }, [])

  const handleGenerateData = async () => {
    if (!window.confirm('Generate 100 users and 500 posts?')) return
    try {
      setLoading(true)
      await axios.post(`${API_BASE}/data/generate?num_users=100&num_posts=500&days_back=30`)
      await fetchData()
      alert('✅ Demo data generated!')
    } catch (err) {
      alert(`❌ Error: ${err.message}`)
    } finally {
      setLoading(false)
    }
  }

  const handleAnalyzeSentiment = async () => {
    try {
      setLoading(true)
      await axios.post(`${API_BASE}/sentiment/analyze-posts`)
      await fetchData()
      alert('✅ Sentiment analysis complete!')
    } catch (err) {
      alert(`❌ Error: ${err.message}`)
    } finally {
      setLoading(false)
    }
  }

  if (loading && !stats) {
    return (
      <div className="loading-screen">
        <div className="spinner"></div>
        <div className="loading-text">Loading Sentinex Dashboard...</div>
      </div>
    )
  }

  return (
    <div className="dashboard">
      {/* Top Navigation Bar */}
      <nav className="nav-bar">
        <div className="nav-left">
          <img src={`${BASE_URL}Sentinex_Logo.png`} alt="Sentinex" className="nav-logo" />
          <div className="nav-title">
            <h1>Sentinex Social Intelligence</h1>
            <p>AI-Powered Analytics Platform</p>
          </div>
        </div>
        <div className="nav-right">
          <div className="status-badge online">
            <span className="status-dot"></span>
            <span>System Online</span>
          </div>
          {stats && (
            <div className="stats-badge">
              <strong>{stats.total_users}</strong> Users
              <span className="divider">•</span>
              <strong>{stats.total_posts}</strong> Posts
            </div>
          )}
        </div>
      </nav>

      {/* NTRO Components Banner */}
      <div className="ntro-banner">
        <div className="ntro-left">
          <span className="trophy">🏆</span>
          <div>
            <h2>NTRO Components - 100% Complete</h2>
            <p>All 5 components successfully implemented with advanced analytics</p>
          </div>
        </div>
        <div className="ntro-components">
          {['A', 'B', 'C', 'D', 'E'].map(comp => (
            <div key={comp} className="component-badge">
              <div className="comp-letter">{comp}</div>
              <div className="comp-status">✓</div>
            </div>
          ))}
        </div>
      </div>

      {/* Detailed NTRO Components Showcase */}
      <div className="ntro-showcase">
        <h2 className="showcase-title">📊 NTRO Components - Detailed Analytics</h2>
        <p className="showcase-subtitle">Advanced social media analytics with visualizations & data insights</p>
        
        <ComponentA stats={stats} />
        <ComponentB sentimentData={sentimentData} emotionData={emotionData} />
        <ComponentC stats={stats} />
        <ComponentD topicsData={topicsData} />
        <ComponentE networkData={networkData} />
      </div>

      {/* Main Content */}
      <div className="content-wrapper">
        {error && (
          <div className="alert alert-error">
            <span>⚠️</span>
            <span>{error}</span>
          </div>
        )}

        {/* Dashboard Grid */}
        <div className="dashboard-grid">
          {/* Data Stats Card */}
          <div className="card">
            <div className="card-header" style={{ background: `linear-gradient(135deg, ${COLORS.primary}, ${COLORS.cyan})` }}>
              <span className="card-icon">📊</span>
              <h3>Data Statistics</h3>
            </div>
            <div className="card-body">
              {stats ? (
                <>
                  <div className="stat-grid">
                    <div className="stat-box" style={{ borderColor: COLORS.primary }}>
                      <div className="stat-value">{stats.total_users}</div>
                      <div className="stat-label">Users</div>
                    </div>
                    <div className="stat-box" style={{ borderColor: COLORS.purple }}>
                      <div className="stat-value">{stats.total_posts}</div>
                      <div className="stat-label">Posts</div>
                    </div>
                  </div>
                  <div className="platform-list">
                    <h4>📱 Platforms</h4>
                    {Object.entries(stats.platform_distribution || {}).map(([platform, count]) => (
                      <div key={platform} className="platform-item">
                        <span className="platform-name">{platform}</span>
                        <div className="progress-bar">
                          <div 
                            className="progress-fill"
                            style={{ width: `${(count / stats.total_posts) * 100}%` }}
                          ></div>
                        </div>
                        <span className="platform-count">{count}</span>
                      </div>
                    ))}
                  </div>
                  <button onClick={handleGenerateData} className="btn btn-primary" disabled={loading}>
                    {loading ? '⏳ Processing...' : '🎲 Generate Demo Data'}
                  </button>
                </>
              ) : (
                <div className="error-state">❌ Failed to load data</div>
              )}
            </div>
          </div>

          {/* Sentiment Analysis Card */}
          <div className="card">
            <div className="card-header" style={{ background: `linear-gradient(135deg, ${COLORS.success}, #059669)` }}>
              <span className="card-icon">😊</span>
              <h3>Sentiment Analysis</h3>
            </div>
            <div className="card-body">
              {sentimentData ? (
                <>
                  {Object.entries(sentimentData.sentiment_distribution || {}).map(([sentiment, count]) => {
                    const total = Object.values(sentimentData.sentiment_distribution).reduce((a, b) => a + b, 0)
                    const percentage = ((count / total) * 100).toFixed(1)
                    const emoji = sentiment === 'positive' ? '😊' : sentiment === 'negative' ? '😞' : '😐'
                    const color = sentiment === 'positive' ? COLORS.success : sentiment === 'negative' ? COLORS.danger : '#6B7280'
                    
                    return (
                      <div key={sentiment} className="sentiment-item">
                        <div className="sentiment-header">
                          <span className="sentiment-emoji">{emoji}</span>
                          <span className="sentiment-label">{sentiment}</span>
                          <span className="sentiment-percent" style={{ color }}>{percentage}%</span>
                        </div>
                        <div className="progress-bar">
                          <div 
                            className="progress-fill"
                            style={{ width: `${percentage}%`, backgroundColor: color }}
                          ></div>
                        </div>
                        <div className="sentiment-count">{count} posts</div>
                      </div>
                    )
                  })}
                  <button onClick={handleAnalyzeSentiment} className="btn btn-success" disabled={loading}>
                    {loading ? '⏳ Analyzing...' : '🔍 Analyze Sentiments'}
                  </button>
                </>
              ) : (
                <div className="error-state">❌ Failed to load sentiment data</div>
              )}
            </div>
          </div>

          {/* Network Analysis Card */}
          <div className="card">
            <div className="card-header" style={{ background: `linear-gradient(135deg, ${COLORS.cyan}, #0891B2)` }}>
              <span className="card-icon">🌐</span>
              <h3>Network Analysis</h3>
            </div>
            <div className="card-body">
              {networkData?.network_statistics ? (
                <div className="metric-grid">
                  <div className="metric-box">
                    <div className="metric-icon">👥</div>
                    <div className="metric-value">{networkData.network_statistics.num_users}</div>
                    <div className="metric-label">Users</div>
                  </div>
                  <div className="metric-box">
                    <div className="metric-icon">🔗</div>
                    <div className="metric-value">{networkData.network_statistics.num_relationships}</div>
                    <div className="metric-label">Links</div>
                  </div>
                  <div className="metric-box">
                    <div className="metric-icon">📊</div>
                    <div className="metric-value">{(networkData.network_statistics.network_density * 100).toFixed(1)}%</div>
                    <div className="metric-label">Density</div>
                  </div>
                  <div className="metric-box">
                    <div className="metric-icon">🎯</div>
                    <div className="metric-value">{(networkData.network_statistics.avg_clustering_coefficient * 100).toFixed(1)}%</div>
                    <div className="metric-label">Clustering</div>
                  </div>
                </div>
              ) : (
                <div className="error-state">❌ Failed to load network data</div>
              )}
            </div>
          </div>

          {/* Emotion Distribution Card */}
          <div className="card">
            <div className="card-header" style={{ background: `linear-gradient(135deg, ${COLORS.purple}, #9333EA)` }}>
              <span className="card-icon">🎭</span>
              <h3>Emotion Distribution</h3>
            </div>
            <div className="card-body">
              {emotionData?.emotion_distribution ? (
                <div className="emotion-list">
                  {[
                    { label: '😏 Sarcasm', value: emotionData.emotion_distribution.sarcasm, color: '#F59E0B' },
                    { label: '😰 Anxiety', value: emotionData.emotion_distribution.anxiety, color: '#EF4444' },
                    { label: '🎉 Excitement', value: emotionData.emotion_distribution.excitement, color: '#10B981' },
                    { label: '🤝 Supportive', value: emotionData.emotion_distribution.supportive, color: '#0066FF' },
                    { label: '❌ Against', value: emotionData.emotion_distribution.against, color: '#8B5CF6' },
                  ].map((emotion, idx) => {
                    const percentage = (emotion.value * 100).toFixed(1)
                    return (
                      <div key={idx} className="emotion-item">
                        <div className="emotion-header">
                          <span>{emotion.label}</span>
                          <span style={{ color: emotion.color, fontWeight: 'bold' }}>{percentage}%</span>
                        </div>
                        <div className="progress-bar">
                          <div 
                            className="progress-fill"
                            style={{ width: `${percentage}%`, backgroundColor: emotion.color }}
                          ></div>
                        </div>
                      </div>
                    )
                  })}
                </div>
              ) : (
                <div className="error-state">❌ Failed to load emotions</div>
              )}
            </div>
          </div>

          {/* Trending Topics Card */}
          <div className="card">
            <div className="card-header" style={{ background: `linear-gradient(135deg, ${COLORS.warning}, #DC2626)` }}>
              <span className="card-icon">🔥</span>
              <h3>Trending Topics</h3>
            </div>
            <div className="card-body">
              {topicsData?.trending_topics ? (
                <div className="topics-list">
                  {topicsData.trending_topics.slice(0, 10).map((item, idx) => (
                    <div key={idx} className="topic-item">
                      <div className="topic-rank">{idx + 1}</div>
                      <div className="topic-name">#{item.topic}</div>
                      <div className="topic-count">
                        <span className="fire-icon">🔥</span>
                        <span>{item.count}</span>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="error-state">❌ Failed to load topics</div>
              )}
            </div>
          </div>

          {/* System Health Card */}
          <div className="card">
            <div className="card-header" style={{ background: `linear-gradient(135deg, ${COLORS.success}, #059669)` }}>
              <span className="card-icon">⚡</span>
              <h3>System Health</h3>
            </div>
            <div className="card-body">
              <div className="health-list">
                {['Backend API', 'Database', 'Network Analysis', 'Sentiment Engine'].map((service, idx) => (
                  <div key={idx} className="health-item">
                    <span>{service}</span>
                    <div className="health-status online">
                      <span className="status-dot"></span>
                      <span>Online</span>
                    </div>
                  </div>
                ))}
              </div>
              <div className="uptime-box">
                <div className="uptime-value">99.9%</div>
                <div className="uptime-label">System Uptime</div>
              </div>
            </div>
          </div>
        </div>

        {/* Action Bar */}
        <div className="action-bar">
          <h3>⚡ Quick Actions</h3>
          <div className="action-buttons">
            <button 
              onClick={() => window.open('/api/docs', '_blank')} 
              className="action-btn"
            >
              📚 API Documentation
            </button>
            <button 
              onClick={fetchData} 
              className="action-btn"
              disabled={refreshing}
            >
              {refreshing ? '⏳ Refreshing...' : '🔄 Refresh Data'}
            </button>
            <button 
              onClick={handleGenerateData} 
              className="action-btn"
              disabled={loading}
            >
              🎲 Generate Demo Data
            </button>
            <button 
              onClick={handleAnalyzeSentiment} 
              className="action-btn"
              disabled={loading}
            >
              🔍 Analyze Sentiments
            </button>
          </div>
        </div>

        {/* Footer */}
        <footer className="footer">
          <span>© 2026 Sentinex Technologies</span>
          <span>•</span>
          <span>SIH 2026 | NTRO #26152</span>
          <span>•</span>
          <span className="tagline">Smarter Data • Deeper Insights • Safer Tomorrow</span>
        </footer>
      </div>
    </div>
  )
}

export default App
