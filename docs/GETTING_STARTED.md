# 🚀 Getting Started Guide

Complete setup guide for the Handy Haversack Haverdashery Pathfinder companion app.

---

## 📋 Prerequisites

### Required Software

**Backend:**
- Python 3.9 or higher
- pip (Python package manager)

**Frontend:**
- Node.js 16 or higher
- npm (comes with Node.js)

**Database:**
- SQLite (comes with Python)

**Version Control:**
- Git

### Check Your Versions

```bash
# Check Python version
python --version

# Check Node version
node --version

# Check npm version
npm --version

# Check git version
git --version
```

### Install Missing Software

**Windows:**
- Python: Download from https://python.org
- Node.js: Download from https://nodejs.org
- Git: Download from https://git-scm.com

**macOS:**
```bash
# Using Homebrew
brew install python node git
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip nodejs npm git
```

---

## 🎯 Quick Setup (Automated)

### Windows

1. Open PowerShell in project root
2. Run the setup script:
```bash
.\setup-windows.bat
```

### Mac/Linux

1. Open Terminal in project root
2. Make script executable and run:
```bash
chmod +x setup-unix.sh
./setup-unix.sh
```

**The script will:**
- Create Python virtual environment
- Install backend dependencies
- Install frontend dependencies
- Create .env files
- Initialize database
- Verify installation

**After script completes**, skip to [Verify Installation](#verify-installation)

---

## 🔧 Manual Setup (If Script Fails)

### Step 1: Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
# Windows:
copy .env.example .env
# Mac/Linux:
cp .env.example .env
```

### Step 2: Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install dependencies
npm install

# Copy environment template
# Windows:
copy .env.example .env
# Mac/Linux:
cp .env.example .env
```

### Step 3: Database Setup

The database will be automatically created when you first run the backend server.

---

## ▶️ Running the Application

### Start Backend Server

```bash
# From backend directory, with venv activated
uvicorn app.main:app --reload
```

**You should see:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

**Backend is now running at:** http://localhost:8000

### Start Frontend Server

**Open a NEW terminal window:**

```bash
# From frontend directory
npm run dev
```

**You should see:**
```
VITE v4.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
```

**Frontend is now running at:** http://localhost:5173

---

## ✅ Verify Installation

### 1. Check Backend Health

**Open browser to:** http://localhost:8000/health

**You should see:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-03T..."
}
```

### 2. Check API Documentation

**Open browser to:** http://localhost:8000/docs

You should see the interactive Swagger UI with all API endpoints.

### 3. Check Frontend

**Open browser to:** http://localhost:5173

You should see the Pathfinder-themed app with the DiceRoller component.

### 4. Test Dice Rolling

In the frontend:
1. Enter "2d6" in the dice input
2. Click "Roll"
3. You should see a result

### 5. Test API Directly

**Using browser or curl:**

```bash
# Health check
curl http://localhost:8000/health

# Roll dice
curl -X POST http://localhost:8000/dice/roll \
  -H "Content-Type: application/json" \
  -d '{"notation": "2d6+3"}'
```

**Expected response:**
```json
{
  "notation": "2d6+3",
  "rolls": [4, 5],
  "modifier": 3,
  "total": 12
}
```

---

## 🗂️ Project Structure

```
Handy-Haversack-Haverdashery/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application
│   │   ├── database.py          # Database setup
│   │   ├── api/                 # API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── dice.py
│   │   │   ├── characters.py
│   │   │   └── encounters.py
│   │   ├── models/              # Database models
│   │   │   ├── __init__.py
│   │   │   └── character.py
│   │   └── services/            # Business logic
│   │       ├── __init__.py
│   │       ├── dice_service.py
│   │       └── encounter_service.py
│   ├── tests/                   # Test files
│   │   └── test_dice.py
│   ├── data/
│   │   ├── pdfs/               # PDF storage
│   │   ├── json/               # JSON data
│   │   └── sqlite/             # SQLite database
│   ├── venv/                   # Virtual environment
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Environment variables
│   └── .env.example           # Environment template
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── DiceRoller.tsx  # Dice roller component
│   │   ├── App.tsx             # Main app component
│   │   └── main.tsx            # Entry point
│   ├── public/                 # Static assets
│   ├── node_modules/           # Node dependencies
│   ├── package.json            # npm dependencies
│   ├── tailwind.config.js      # Tailwind CSS config
│   ├── vite.config.ts          # Vite config
│   ├── .env                    # Environment variables
│   └── .env.example           # Environment template
│
└── docs/                       # Documentation
    ├── GETTING_STARTED.md      # This file
    ├── ARCHITECTURE.md
    ├── INITIAL_TASKS.md
    └── INDEX.md
```

---

## 🔐 Environment Configuration

### Backend (.env)

```env
DATABASE_URL=sqlite:///./data/sqlite/pathfinder.db
CORS_ORIGINS=http://localhost:5173
DEBUG=true
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000
```

---

## 🛠️ Development Workflow

### Daily Startup

1. Open two terminal windows
2. Terminal 1: Start backend
   ```bash
   cd backend
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Mac/Linux
   uvicorn app.main:app --reload
   ```
3. Terminal 2: Start frontend
   ```bash
   cd frontend
   npm run dev
   ```

### Making Changes

**Backend changes:**
- Edit files in `backend/app/`
- Server auto-reloads on save
- Check terminal for errors

**Frontend changes:**
- Edit files in `frontend/src/`
- Browser auto-refreshes on save
- Check browser console for errors

### Running Tests

```bash
# From backend directory, with venv activated
pytest

# Run specific test
pytest tests/test_dice.py

# Run with output
pytest -v

# Run with coverage
pytest --cov=app tests/
```

---

## 🐛 Troubleshooting

### Backend Issues

**Problem: `uvicorn: command not found`**
```bash
# Solution: Make sure venv is activated and dependencies installed
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

**Problem: Port 8000 already in use**
```bash
# Solution: Use a different port
uvicorn app.main:app --reload --port 8001

# Or kill the process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F
# Mac/Linux:
lsof -ti:8000 | xargs kill -9
```

**Problem: Module not found errors**
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**Problem: Database errors**
```bash
# Solution: Delete and recreate database
# Windows:
del backend\data\sqlite\pathfinder.db
# Mac/Linux:
rm backend/data/sqlite/pathfinder.db
# Restart backend server to recreate
```

### Frontend Issues

**Problem: `npm: command not found`**
```bash
# Solution: Install Node.js from https://nodejs.org
```

**Problem: Port 5173 already in use**
```bash
# Solution: Kill the process or use different port
npm run dev -- --port 5174
```

**Problem: Module not found errors**
```bash
# Solution: Reinstall node_modules
rm -rf node_modules package-lock.json
npm install
```

**Problem: API calls failing (CORS errors)**
```bash
# Solution: Check backend .env CORS_ORIGINS
# Should include: http://localhost:5173
# Restart backend after changing .env
```

### General Issues

**Problem: Changes not appearing**
```bash
# Solution: Hard refresh browser
# Windows/Linux: Ctrl + Shift + R
# Mac: Cmd + Shift + R
```

**Problem: Git conflicts**
```bash
# Solution: Stash changes, pull, reapply
git stash
git pull
git stash pop
```

---

## 📚 Next Steps

Now that everything is set up:

1. ✅ Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand the system
2. ✅ Check [INITIAL_TASKS.md](INITIAL_TASKS.md) for your first tasks
3. ✅ Bookmark [QUICK_REFERENCE.md](../QUICK_REFERENCE.md) for commands
4. ✅ Explore the API at http://localhost:8000/docs
5. ✅ Try rolling some dice in the frontend!

---

## 🤝 Team Setup

### For the Backend Developer (You)

- Focus on `backend/` directory
- Your tasks are in INITIAL_TASKS.md (Backend section)
- Test your changes with pytest
- Use API docs to verify endpoints

### For the Frontend Developer (James)

- Focus on `frontend/` directory
- Tasks are in INITIAL_TASKS.md (Frontend section)
- Test in browser at http://localhost:5173
- Use API docs to understand endpoints

### Working Together

- Both can work simultaneously
- Backend changes don't affect frontend (if API contract stays same)
- Frontend changes don't affect backend
- Communicate when changing API endpoints!

---

## 🎓 Learning Resources

**FastAPI:**
- Tutorial: https://fastapi.tiangolo.com/tutorial/
- Advanced: https://fastapi.tiangolo.com/advanced/

**React + TypeScript:**
- React docs: https://react.dev/
- TypeScript: https://www.typescriptlang.org/docs/

**Tailwind CSS:**
- Docs: https://tailwindcss.com/docs
- Cheatsheet: https://nerdcave.com/tailwind-cheat-sheet

**Pathfinder 2e:**
- SRD: https://2e.aonprd.com/
- Rules: https://2e.aonprd.com/Rules.aspx

---

## 📞 Need Help?

1. Check this guide's troubleshooting section
2. Check [QUICK_REFERENCE.md](../QUICK_REFERENCE.md)
3. Read error messages carefully
4. Google the error message
5. Check API docs at http://localhost:8000/docs
6. Ask your teammate!

---

## 🎉 You're Ready!

Everything should now be:
- ✅ Installed
- ✅ Configured
- ✅ Running
- ✅ Tested

**Time to start building!** 🎲

Check [INITIAL_TASKS.md](INITIAL_TASKS.md) for your first tasks.
