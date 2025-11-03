#!/bin/bash

echo "================================================"
echo "Handy Haversack Haverdashery - Quick Setup"
echo "================================================"
echo ""

echo "[1/4] Setting up Backend..."
cd backend

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating .env file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file"
else
    echo ".env file already exists"
fi

cd ..

echo ""
echo "[2/4] Setting up Frontend..."
cd frontend

echo "Installing npm dependencies..."
npm install

cd ..

echo ""
echo "[3/4] Creating data directories..."
mkdir -p data/sqlite
mkdir -p data/json
mkdir -p data/pdfs

echo ""
echo "[4/4] Setup Complete!"
echo ""
echo "================================================"
echo "Next Steps:"
echo "================================================"
echo ""
echo "1. Open TWO terminal windows"
echo ""
echo "2. Terminal 1 - Backend:"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   uvicorn app.main:app --reload"
echo ""
echo "3. Terminal 2 - Frontend:"
echo "   cd frontend"
echo "   npm start"
echo ""
echo "4. Open browser to:"
echo "   Frontend: http://localhost:3000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "================================================"
echo "Happy rolling! 🎲"
echo "================================================"
