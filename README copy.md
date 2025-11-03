# Handy Haversack Haverdashery 🎲

A comprehensive Pathfinder TTRPG companion application for character management, dice rolling, and encounter generation.

## Features

### Phase 1: Core Functionality (MVP)
- **Character Tracker**: Digital character sheets with full stat management
- **Dice Roller**: Polyhedral dice roller with modifiers and roll history
- **Encounter Generator**: CR-based encounter building with party consideration

### Phase 2: Advanced Features (Planned)
- PDF parsing for importing Pathfinder content
- Initiative tracker integration
- Spell database and preparation system
- Inventory management with weight/bulk tracking
- Campaign session notes and history

## Tech Stack

**Backend:**
- Python 3.11+
- FastAPI (REST API)
- SQLAlchemy (ORM)
- SQLite (development) → PostgreSQL (production)
- Pydantic (data validation)

**Frontend:**
- React with TypeScript
- Tailwind CSS for styling
- Axios for API calls
- React Router for navigation

## Project Structure

```
pathfinder-companion/
├── backend/
│   ├── app/
│   │   ├── api/          # API route handlers
│   │   ├── models/       # Database models
│   │   ├── services/     # Business logic
│   │   └── utils/        # Helper functions
│   ├── tests/            # Backend tests
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── services/     # API service layer
│   │   ├── hooks/        # Custom React hooks
│   │   └── types/        # TypeScript type definitions
│   └── package.json      # Node dependencies
├── data/
│   ├── pdfs/            # Pathfinder PDF resources
│   ├── json/            # Parsed game data
│   └── sqlite/          # Local database files
└── docs/                # Documentation

```

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Node.js 18+ and npm
- Git

### Backend Setup

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

# Run the development server
uvicorn app.main:app --reload
```

Backend will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend will be available at `http://localhost:3000`

## Development Workflow

1. **Create a new branch** for your feature: `git checkout -b feature/your-feature-name`
2. **Make your changes** and commit with clear messages
3. **Push to GitHub**: `git push origin feature/your-feature-name`
4. **Create a Pull Request** for review
5. **Merge after approval**

## API Endpoints (Planned)

### Characters
- `GET /api/characters` - List all characters
- `POST /api/characters` - Create new character
- `GET /api/characters/{id}` - Get character details
- `PUT /api/characters/{id}` - Update character
- `DELETE /api/characters/{id}` - Delete character

### Dice Rolling
- `POST /api/dice/roll` - Roll dice (supports expressions like "2d6+3")
- `GET /api/dice/history` - Get roll history

### Encounters
- `POST /api/encounters/generate` - Generate random encounter
- `GET /api/encounters/{id}` - Get encounter details

## Contributors

- **StrayDogSyn** - Project Lead
- **jamesbeattie221@gmail.com** - Contributor

## License

Creative Commons Zero v1.0 Universal

---

*"Roll for initiative!"* 🎲
