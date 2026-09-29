#!/bin/bash

echo "=================================================="
echo "  🚀 Sentinex Social Intelligence Platform"
echo "  Smart India Hackathon 2026 - Problem #26152"
echo "  React + Vite Frontend"
echo "=================================================="
echo ""

# Navigate to project root
cd "$(dirname "$0")"

# Kill any existing servers
echo "🧹 Cleaning up old processes..."
lsof -ti:8002 | xargs kill -9 2>/dev/null || true
lsof -ti:5173 | xargs kill -9 2>/dev/null || true
sleep 1

# Start backend server
echo "🔧 Starting backend server on port 8002..."
cd backend
nohup ./venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8002 > /tmp/sentinex-backend.log 2>&1 &
BACKEND_PID=$!
cd ..

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
echo "🌐 Starting React + Vite frontend on port 5173..."
cd frontend-react
npm run dev &
FRONTEND_PID=$!
cd ..

sleep 3

echo ""
echo "=================================================="
echo "  ✅ Project is running!"
echo "=================================================="
echo ""
echo "🎯 React Frontend: http://localhost:5173"
echo "🔧 Backend API: http://localhost:8002"
echo "📚 API Documentation: http://localhost:8002/docs"
echo ""
echo "📝 Opening browser..."
sleep 2
open http://localhost:5173

echo ""
echo "=================================================="
echo "  Press Ctrl+C to stop all servers"
echo "=================================================="
echo ""

# Wait for user interrupt
wait
