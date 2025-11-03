# 🎲 Quick Reference Guide

## Common Commands

### Backend
```bash
# Start the backend server
cd backend
uvicorn app.main:app --reload

# Run tests
pytest

# Install dependencies
pip install -r requirements.txt
```

### Frontend
```bash
# Start the frontend dev server
cd frontend
npm run dev

# Install dependencies
npm install

# Build for production
npm run build
```

### Database
```bash
# Database is auto-created on first backend run
# Location: backend/data/sqlite/pathfinder.db
```

---

## API Endpoints

### Health Check
- `GET /health` - Check if API is running

### Dice Rolling
- `POST /dice/roll` - Roll dice (e.g., "2d6+3")
- `POST /dice/roll/advantage` - Roll d20 with advantage
- `POST /dice/roll/disadvantage` - Roll d20 with disadvantage
- `GET /dice/history` - Get roll history
- `DELETE /dice/history` - Clear roll history

### Characters
- `POST /characters` - Create character
- `GET /characters` - List all characters
- `GET /characters/{id}` - Get character details
- `PUT /characters/{id}` - Update character
- `DELETE /characters/{id}` - Delete character
- `POST /characters/{id}/damage` - Apply damage
- `POST /characters/{id}/heal` - Heal character

### Encounters
- `POST /encounters/generate` - Generate encounter
- `GET /encounters/{id}` - Get encounter details
- `GET /bestiary` - List all monsters

---

## Dice Notation

- `1d20` - Roll one 20-sided die
- `2d6+3` - Roll two 6-sided dice, add 3
- `4d6-2` - Roll four 6-sided dice, subtract 2
- `1d100` - Roll percentile dice
- Advantage/Disadvantage: Use specific endpoints

---

## File Locations

### Backend
- Main app: `backend/app/main.py`
- Models: `backend/app/models/`
- API routes: `backend/app/api/`
- Services: `backend/app/services/`
- Tests: `backend/tests/`
- Database: `backend/data/sqlite/`

### Frontend
- Components: `frontend/src/components/`
- Main app: `frontend/src/App.tsx`
- Config: `frontend/tailwind.config.js`

### Documentation
- All docs: `docs/`
- Getting started: `docs/GETTING_STARTED.md`
- Architecture: `docs/ARCHITECTURE.md`
- Tasks: `docs/INITIAL_TASKS.md`

---

## Environment Variables

### Backend (.env)
```
DATABASE_URL=sqlite:///./data/sqlite/pathfinder.db
CORS_ORIGINS=http://localhost:5173
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000
```

---

## Common Issues

### Backend won't start
- Check Python version (3.9+)
- Install dependencies: `pip install -r requirements.txt`
- Check port 8000 is available

### Frontend won't start
- Check Node version (16+)
- Install dependencies: `npm install`
- Check port 5173 is available

### Database errors
- Database is auto-created
- Check write permissions in `backend/data/sqlite/`
- Delete database file to reset

---

## Git Workflow

```bash
# Start new feature
git checkout -b feature/your-feature-name

# Make changes and commit
git add .
git commit -m "Description of changes"

# Push to GitHub
git push origin feature/your-feature-name

# Create Pull Request on GitHub
# After review and approval, merge to main
```

---

## Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_dice.py

# Run with coverage
pytest --cov=app tests/
```

---

## Port Reference

- Backend API: `http://localhost:8000`
- Frontend Dev: `http://localhost:5173`
- API Docs: `http://localhost:8000/docs`
- Alternative API Docs: `http://localhost:8000/redoc`

---

## Quick Start (After Setup)

1. Open two terminals
2. Terminal 1: `cd backend && uvicorn app.main:app --reload`
3. Terminal 2: `cd frontend && npm run dev`
4. Open browser to `http://localhost:5173`
5. Start coding!

---

## Need More Help?

- **Setup**: See `docs/GETTING_STARTED.md`
- **Architecture**: See `docs/ARCHITECTURE.md`
- **Tasks**: See `docs/INITIAL_TASKS.md`
- **All Docs**: See `docs/INDEX.md`
