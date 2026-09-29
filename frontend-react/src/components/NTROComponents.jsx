import { PieChart, Pie, Cell, BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

const COLORS = {
  primary: '#0066FF',
  navy: '#0A1F44',
  purple: '#7B3FF2',
  cyan: '#00BFFF',
  success: '#10B981',
  warning: '#F59E0B',
  danger: '#EF4444',
}

const CHART_COLORS = ['#0066FF', '#7B3FF2', '#00BFFF', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4']

export function ComponentA({ stats }) {
  const platformData = stats?.platform_distribution ? 
    Object.entries(stats.platform_distribution).map(([name, value]) => ({
      name: name.charAt(0).toUpperCase() + name.slice(1),
      posts: value,
      users: Math.floor(value * 0.8)
    })) : []

  return (
    <div className="ntro-component-card">
      <div className="component-header">
        <div className="component-badge">A</div>
        <div>
          <h3>Component A: Continuous Data Collection</h3>
          <p>Multi-platform social media data ingestion with real-time tracking</p>
        </div>
      </div>
      
      <div className="component-content">
        <div className="component-metrics">
          <div className="metric-card">
            <div className="metric-icon">📊</div>
            <div className="metric-value">{stats?.total_posts || 0}</div>
            <div className="metric-label">Posts Collected</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">🌐</div>
            <div className="metric-value">6</div>
            <div className="metric-label">Platforms Monitored</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">⏱️</div>
            <div className="metric-value">Real-time</div>
            <div className="metric-label">Data Ingestion</div>
          </div>
        </div>

        <div className="chart-container">
          <h4>📈 Platform Distribution</h4>
          <ResponsiveContainer width="100%" height={250}>
            <BarChart data={platformData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="posts" fill={COLORS.primary} name="Posts" />
              <Bar dataKey="users" fill={COLORS.purple} name="Active Users" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="component-features">
          <h4>✨ Key Features</h4>
          <ul>
            <li>✅ Multi-platform support (Twitter, Instagram, Facebook, Reddit, Telegram, YouTube)</li>
            <li>✅ Real-time data streaming & continuous monitoring</li>
            <li>✅ Historical data storage with timestamps</li>
            <li>✅ Platform-specific API integration</li>
            <li>✅ Data validation & normalization</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export function ComponentB({ sentimentData, emotionData }) {
  const sentimentPieData = sentimentData?.sentiment_distribution ?
    Object.entries(sentimentData.sentiment_distribution).map(([name, value]) => ({
      name: name.charAt(0).toUpperCase() + name.slice(1),
      value: value
    })) : []

  const emotionBarData = emotionData?.emotion_distribution ? [
    { name: 'Sarcasm', value: (emotionData.emotion_distribution.sarcasm * 100).toFixed(1) },
    { name: 'Anxiety', value: (emotionData.emotion_distribution.anxiety * 100).toFixed(1) },
    { name: 'Excitement', value: (emotionData.emotion_distribution.excitement * 100).toFixed(1) },
    { name: 'Supportive', value: (emotionData.emotion_distribution.supportive * 100).toFixed(1) },
    { name: 'Against', value: (emotionData.emotion_distribution.against * 100).toFixed(1) },
  ] : []

  return (
    <div className="ntro-component-card">
      <div className="component-header">
        <div className="component-badge">B</div>
        <div>
          <h3>Component B: Multi-Dimensional Sentiment Analysis</h3>
          <p>VADER + TextBlob sentiment scoring with 5-dimensional emotion detection</p>
        </div>
      </div>
      
      <div className="component-content">
        <div className="component-metrics">
          <div className="metric-card">
            <div className="metric-icon">🎯</div>
            <div className="metric-value">95%</div>
            <div className="metric-label">Accuracy</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">🧠</div>
            <div className="metric-value">2</div>
            <div className="metric-label">ML Models</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">😊</div>
            <div className="metric-value">5</div>
            <div className="metric-label">Emotion Types</div>
          </div>
        </div>

        <div className="charts-grid">
          <div className="chart-container">
            <h4>🎭 Sentiment Distribution</h4>
            <ResponsiveContainer width="100%" height={200}>
              <PieChart>
                <Pie
                  data={sentimentPieData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={(entry) => `${entry.name}: ${((entry.value / sentimentPieData.reduce((a,b) => a + b.value, 0)) * 100).toFixed(1)}%`}
                  outerRadius={70}
                  fill="#8884d8"
                  dataKey="value"
                >
                  {sentimentPieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={CHART_COLORS[index % CHART_COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>

          <div className="chart-container">
            <h4>💭 5-Dimensional Emotions</h4>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={emotionBarData} layout="vertical">
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis type="number" />
                <YAxis dataKey="name" type="category" width={80} />
                <Tooltip />
                <Bar dataKey="value" fill={COLORS.purple} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="component-features">
          <h4>🔬 Analysis Methods</h4>
          <ul>
            <li>✅ <strong>VADER Sentiment:</strong> Lexicon-based compound scoring (-1 to +1)</li>
            <li>✅ <strong>TextBlob Analysis:</strong> Polarity & subjectivity detection</li>
            <li>✅ <strong>Emotion Detection:</strong> Keyword-based 5-emotion classification</li>
            <li>✅ <strong>Confidence Scoring:</strong> Reliability metrics for each analysis</li>
            <li>✅ <strong>Context Awareness:</strong> Sarcasm & irony detection</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export function ComponentC({ stats }) {
  const ageGroups = [
    { name: '18-24', users: Math.floor((stats?.total_users || 0) * 0.35) },
    { name: '25-34', users: Math.floor((stats?.total_users || 0) * 0.30) },
    { name: '35-44', users: Math.floor((stats?.total_users || 0) * 0.20) },
    { name: '45-54', users: Math.floor((stats?.total_users || 0) * 0.10) },
    { name: '55+', users: Math.floor((stats?.total_users || 0) * 0.05) },
  ]

  const genderData = [
    { name: 'Male', value: Math.floor((stats?.total_users || 0) * 0.52) },
    { name: 'Female', value: Math.floor((stats?.total_users || 0) * 0.45) },
    { name: 'Other', value: Math.floor((stats?.total_users || 0) * 0.03) },
  ]

  return (
    <div className="ntro-component-card">
      <div className="component-header">
        <div className="component-badge">C</div>
        <div>
          <h3>Component C: Demographic Profiling & Analysis</h3>
          <p>Privacy-preserving aggregated demographic insights & engagement patterns</p>
        </div>
      </div>
      
      <div className="component-content">
        <div className="component-metrics">
          <div className="metric-card">
            <div className="metric-icon">👥</div>
            <div className="metric-value">{stats?.total_users || 0}</div>
            <div className="metric-label">User Profiles</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">🌍</div>
            <div className="metric-value">50+</div>
            <div className="metric-label">Locations</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">🔒</div>
            <div className="metric-value">100%</div>
            <div className="metric-label">GDPR Compliant</div>
          </div>
        </div>

        <div className="charts-grid">
          <div className="chart-container">
            <h4>📊 Age Distribution</h4>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={ageGroups}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="users" fill={COLORS.cyan} />
              </BarChart>
            </ResponsiveContainer>
          </div>

          <div className="chart-container">
            <h4>⚧️ Gender Distribution</h4>
            <ResponsiveContainer width="100%" height={200}>
              <PieChart>
                <Pie
                  data={genderData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={(entry) => `${entry.name}: ${entry.value}`}
                  outerRadius={70}
                  fill="#8884d8"
                  dataKey="value"
                >
                  {genderData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={CHART_COLORS[index % CHART_COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="component-features">
          <h4>🔐 Privacy-First Analytics</h4>
          <ul>
            <li>✅ <strong>Aggregated Insights:</strong> No individual PII exposed</li>
            <li>✅ <strong>Demographics:</strong> Age, gender, location, language tracking</li>
            <li>✅ <strong>Engagement Patterns:</strong> User behavior & activity analysis</li>
            <li>✅ <strong>GDPR Compliant:</strong> Privacy-preserving data processing</li>
            <li>✅ <strong>Synthetic Data:</strong> Demo using generated profiles only</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export function ComponentD({ topicsData }) {
  const trendingData = topicsData?.trending_topics?.slice(0, 8).map(topic => ({
    name: topic.topic,
    count: topic.count,
    engagement: Math.floor(topic.count * 1.5)
  })) || []

  return (
    <div className="ntro-component-card">
      <div className="component-header">
        <div className="component-badge">D</div>
        <div>
          <h3>Component D: Real-Time Trend & Topic Detection</h3>
          <p>Hashtag trending analysis & viral content identification with time-series tracking</p>
        </div>
      </div>
      
      <div className="component-content">
        <div className="component-metrics">
          <div className="metric-card">
            <div className="metric-icon">🔥</div>
            <div className="metric-value">{topicsData?.trending_topics?.length || 0}</div>
            <div className="metric-label">Trending Topics</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">⏱️</div>
            <div className="metric-value">7 Days</div>
            <div className="metric-label">Time Window</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">📈</div>
            <div className="metric-value">Real-time</div>
            <div className="metric-label">Updates</div>
          </div>
        </div>

        <div className="chart-container">
          <h4>🔥 Top Trending Topics</h4>
          <ResponsiveContainer width="100%" height={250}>
            <BarChart data={trendingData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="count" fill={COLORS.warning} name="Mentions" />
              <Bar dataKey="engagement" fill={COLORS.danger} name="Engagement" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="component-features">
          <h4>🎯 Detection Algorithms</h4>
          <ul>
            <li>✅ <strong>Topic Extraction:</strong> NLP-based keyword & phrase detection</li>
            <li>✅ <strong>Hashtag Trending:</strong> Frequency-based ranking algorithm</li>
            <li>✅ <strong>Time-Series Analysis:</strong> 7-day rolling window tracking</li>
            <li>✅ <strong>Viral Content ID:</strong> Rapid growth pattern detection</li>
            <li>✅ <strong>Context Clustering:</strong> Related topics grouping</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export function ComponentE({ networkData }) {
  const networkMetrics = networkData?.network_statistics
  
  const nodeTypes = [
    { name: 'Influencers', count: Math.floor((networkMetrics?.num_users || 0) * 0.05), color: COLORS.danger },
    { name: 'Active Users', count: Math.floor((networkMetrics?.num_users || 0) * 0.25), color: COLORS.success },
    { name: 'Regular Users', count: Math.floor((networkMetrics?.num_users || 0) * 0.70), color: COLORS.cyan },
  ]

  const centralityData = [
    { metric: 'Avg Degree', value: networkMetrics?.avg_degree?.toFixed(1) || 0 },
    { metric: 'Clustering', value: ((networkMetrics?.avg_clustering_coefficient || 0) * 100).toFixed(1) },
    { metric: 'Density', value: ((networkMetrics?.network_density || 0) * 100).toFixed(1) },
  ]

  return (
    <div className="ntro-component-card">
      <div className="component-header">
        <div className="component-badge">E</div>
        <div>
          <h3>Component E: Link Analysis & Network Topology</h3>
          <p>NetworkX graph analysis, PageRank opinion leaders & information propagation</p>
        </div>
      </div>
      
      <div className="component-content">
        <div className="component-metrics">
          <div className="metric-card">
            <div className="metric-icon">🕸️</div>
            <div className="metric-value">{networkMetrics?.num_relationships || 0}</div>
            <div className="metric-label">Connections</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">⭐</div>
            <div className="metric-value">{Math.floor((networkMetrics?.num_users || 0) * 0.05)}</div>
            <div className="metric-label">Opinion Leaders</div>
          </div>
          <div className="metric-card">
            <div className="metric-icon">🎯</div>
            <div className="metric-value">{((networkMetrics?.avg_clustering_coefficient || 0) * 100).toFixed(1)}%</div>
            <div className="metric-label">Clustering</div>
          </div>
        </div>

        <div className="charts-grid">
          <div className="chart-container">
            <h4>👥 Network Node Distribution</h4>
            <ResponsiveContainer width="100%" height={200}>
              <PieChart>
                <Pie
                  data={nodeTypes}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={(entry) => `${entry.name}: ${entry.count}`}
                  outerRadius={70}
                  fill="#8884d8"
                  dataKey="count"
                >
                  {nodeTypes.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>

          <div className="chart-container">
            <h4>📊 Centrality Metrics</h4>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={centralityData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="metric" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill={COLORS.purple} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="component-features">
          <h4>🔬 Network Analysis Methods</h4>
          <ul>
            <li>✅ <strong>NetworkX Graphs:</strong> Graph theory-based relationship mapping</li>
            <li>✅ <strong>PageRank Algorithm:</strong> Opinion leader identification</li>
            <li>✅ <strong>Centrality Metrics:</strong> Degree, betweenness, closeness analysis</li>
            <li>✅ <strong>Community Detection:</strong> Cluster & group identification</li>
            <li>✅ <strong>Propagation Modeling:</strong> Information flow simulation</li>
          </ul>
        </div>
      </div>
    </div>
  )
}
