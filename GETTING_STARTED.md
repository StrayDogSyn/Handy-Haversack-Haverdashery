# Getting Started - Handy Haversack Haverdashery

Welcome! This guide will get you set up and coding quickly.

## Prerequisites

Make sure you have these installed:
- **Python 3.11+**: [Download here](https://www.python.org/downloads/)
- **Node.js 18+**: [Download here](https://nodejs.org/)
- **Git**: [Download here](https://git-scm.com/downloads/)
- **VS Code** (recommended): [Download here](https://code.visualstudio.com/)

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/StrayDogSyn/Handy-Haversack-Haverdashery.git
cd Handy-Haversack-Haverdashery
```

### 2. Set Up the Backend

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Initialize the database (will be created automatically on first run)
```

### 3. Set Up the Frontend

```bash
# Navigate to frontend (from project root)
cd frontend

# Install dependencies
npm install

# The app is now ready to run
```

## Running the Application

You'll need **two terminal windows** - one for backend, one for frontend.

### Terminal 1: Backend

```bash
cd backend

# Make sure virtual environment is activated
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Run the FastAPI server
uvicorn app.main:app --reload
```

Backend will be at: `http://localhost:8000`
API docs at: `http://localhost:8000/docs`

### Terminal 2: Frontend

```bash
cd frontend

# Run the React development server
npm start
```

Frontend will be at: `http://localhost:3000`

## Testing the Setup

### Test the Backend

1. Open your browser to `http://localhost:8000/docs`
2. You should see the FastAPI interactive documentation
3. Try the `/api/health` endpoint - it should return `{"status": "healthy"}`

### Test the Dice Roller

1. In the API docs, find `/api/dice/roll`
2. Click "Try it out"
3. Enter:
   ```json
   {
     "expression": "1d20+5",
     "advantage": false,
     "disadvantage": false
   }
   ```
4. Click "Execute"
5. You should see a dice roll result!

### Test Character Creation

1. In the API docs, find `/api/characters/` (POST)
2. Try creating a test character with the example data
3. Then try `/api/characters/` (GET) to see your character

## Project Structure Quick Reference

```
backend/app/
├── api/          # API endpoints (characters.py, dice.py)
├── models/       # Database models (character.py, schemas.py)
├── services/     # Business logic (dice_engine.py)
└── main.py       # Application entry point

frontend/src/
├── components/   # React components (DiceRoller.tsx, etc.)
├── services/     # API calls
└── App.tsx       # Main React component
```

## Development Workflow

### Creating a New Feature

1. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Backend: Add models, services, API endpoints
   - Frontend: Add components, connect to API

3. **Test your changes**
   - Backend: Run tests with `pytest backend/tests/`
   - Frontend: Test in browser

4. **Commit and push**
   ```bash
   git add .
   git commit -m "Add: description of your feature"
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** on GitHub

## Common Tasks

### Adding a New API Endpoint

1. Create/modify file in `backend/app/api/`
2. Add route functions using FastAPI
3. Include router in `main.py`
4. Test in `/docs`

### Adding a New React Component

1. Create file in `frontend/src/components/`
2. Import and use in `App.tsx`
3. Connect to backend API using axios

### Updating Database Models

1. Modify `backend/app/models/character.py`
2. For production: Create Alembic migration
3. For dev: Delete `data/sqlite/pathfinder.db` and restart server

## Useful Commands

```bash
# Backend - Run tests
pytest backend/tests/

# Backend - Check code style
black backend/app/

# Frontend - Build for production
npm run build

# Frontend - Run tests
npm test
```

## Troubleshooting

### Port Already in Use
- Backend: Change port in `uvicorn` command: `--port 8001`
- Frontend: Create `.env` file with `PORT=3001`

### Module Not Found (Python)
- Make sure virtual environment is activated
- Try `pip install -r requirements.txt` again

### Database Errors
- Delete `data/sqlite/pathfinder.db`
- Restart backend server (it will recreate)

### CORS Errors in Frontend
- Make sure backend is running
- Check `BACKEND_CORS_ORIGINS` in `.env`

## Next Steps

Check out these issues to get started:
- [ ] Implement encounter generator
- [ ] Add character sheet UI
- [ ] Create initiative tracker
- [ ] Add PDF parsing for monsters

## Getting Help

- **Issues**: Create a GitHub issue
- **Discord**: [Link to your Discord/Slack]
- **Docs**: Check `/docs` folder for detailed guides

Happy rolling! 🎲
