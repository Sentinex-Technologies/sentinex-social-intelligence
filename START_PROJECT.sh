#!/bin/bash

echo "=================================================="
echo "  🚀 Sentinex Social Intelligence Platform"
echo "  Smart India Hackathon 2026 - Problem #26152"
echo "=================================================="
echo ""

# Navigate to backend directory
cd "$(dirname "$0")/backend"

# Kill any existing servers
echo "🧹 Cleaning up old processes..."
lsof -ti:8002 | xargs kill -9 2>/dev/null || true
sleep 1

# Start backend server
echo "🔧 Starting backend server on port 8002..."
./venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8002 &
BACKEND_PID=$!

# Wait for backend to start
echo "⏳ Waiting for backend to start..."
sleep 5

# Check if backend is running
if lsof -ti:8002 > /dev/null 2>&1; then
    echo "✅ Backend server started successfully!"
    echo "   📡 API running at: http://localhost:8002"
    echo "   📚 API Docs: http://localhost:8002/docs"
else
    echo "❌ Backend failed to start!"
    exit 1
fi

echo ""
echo "🌐 Opening dashboard in browser..."
open "$(dirname "$0")/frontend/index.html"

echo ""
echo "=================================================="
echo "  ✅ Project is running!"
echo "=================================================="
echo ""
echo "Backend API: http://localhost:8002"
echo "API Documentation: http://localhost:8002/docs"
echo "Dashboard: file://$(pwd)/../frontend/index.html"
echo ""
echo "📝 Backend logs are being displayed below."
echo "   Press Ctrl+C to stop the server"
echo "=================================================="
echo ""

# Show backend logs
wait $BACKEND_PID
