# 🏗️ Architecture Documentation

System design and technical architecture for the Handy Haversack Haverdashery.

---

## 🎯 Overview

This is a **full-stack web application** designed to assist Pathfinder 2e players and Game Masters with:
- Dice rolling and probability
- Character management
- Encounter generation
- Combat tracking (future)
- Spell management (future)

**Architecture Style:** RESTful API with separate frontend

---

## 📚 Technology Stack

### Backend
- **Language:** Python 3.9+
- **Framework:** FastAPI (async web framework)
- **Database:** SQLite with SQLAlchemy ORM
- **Validation:** Pydantic models
- **Testing:** pytest
- **Documentation:** Auto-generated OpenAPI/Swagger

### Frontend
- **Language:** TypeScript
- **Framework:** React 18
- **Build Tool:** Vite
- **Styling:** Tailwind CSS
- **HTTP Client:** Axios
- **State Management:** React hooks (useState, useEffect)

### Infrastructure
- **Development:** Local development servers
- **Database:** SQLite (file-based, no server needed)
- **API Communication:** REST with JSON
- **CORS:** Configured for local development

---

## 🗂️ Project Structure

```
Handy-Haversack-Haverdashery/
│
├── backend/                    # Python FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI app, CORS, startup
│   │   ├── database.py        # SQLAlchemy setup, session mgmt
│   │   │
│   │   ├── api/               # API route handlers
│   │   │   ├── __init__.py
│   │   │   ├── dice.py        # /dice/* endpoints
│   │   │   ├── characters.py  # /characters/* endpoints
│   │   │   └── encounters.py  # /encounters/* endpoints
│   │   │
│   │   ├── models/            # Database models (SQLAlchemy)
│   │   │   ├── __init__.py
│   │   │   ├── character.py   # Character table definition
│   │   │   └── encounter.py   # Encounter table (future)
│   │   │
│   │   └── services/          # Business logic
│   │       ├── __init__.py
│   │       ├── dice_service.py      # Dice rolling logic
│   │       ├── encounter_service.py # Encounter generation
│   │       └── bestiary.py          # Monster data
│   │
│   ├── tests/                 # Test files
│   │   ├── __init__.py
│   │   ├── test_dice.py
│   │   └── test_characters.py
│   │
│   ├── data/                  # Data storage
│   │   ├── pdfs/             # PDF rulebooks (future)
│   │   ├── json/             # JSON data files
│   │   └── sqlite/           # SQLite database
│   │       └── pathfinder.db
│   │
│   ├── requirements.txt       # Python dependencies
│   ├── .env                  # Environment variables
│   └── .env.example          # Environment template
│
├── frontend/                  # React TypeScript frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── DiceRoller.tsx      # Dice rolling UI
│   │   │   ├── CharacterSheet.tsx  # Character display (future)
│   │   │   └── EncounterBuilder.tsx # Encounter UI (future)
│   │   │
│   │   ├── services/
│   │   │   └── api.ts         # Axios API client
│   │   │
│   │   ├── types/
│   │   │   └── index.ts       # TypeScript type definitions
│   │   │
│   │   ├── App.tsx            # Main app component
│   │   ├── main.tsx          # React entry point
│   │   └── index.css         # Global styles
│   │
│   ├── public/               # Static assets
│   ├── package.json          # npm dependencies
│   ├── vite.config.ts       # Vite configuration
│   ├── tailwind.config.js   # Tailwind CSS config
│   ├── tsconfig.json        # TypeScript config
│   └── .env                 # Environment variables
│
├── docs/                     # Documentation
│   ├── INDEX.md
│   ├── GETTING_STARTED.md
│   ├── ARCHITECTURE.md       # This file
│   └── INITIAL_TASKS.md
│
├── setup-windows.bat         # Windows setup script
├── setup-unix.sh            # Mac/Linux setup script
├── .gitignore               # Git ignore rules
├── README.md                # Project overview
└── LICENSE                  # MIT License
```

---

## 🔄 Data Flow

### API Request Flow

```
User Action (Frontend)
        ↓
React Component
        ↓
Axios HTTP Request
        ↓
FastAPI Route Handler (api/)
        ↓
Pydantic Validation
        ↓
Service Layer (services/)
        ↓
Database Layer (models/)
        ↓
SQLAlchemy ORM
        ↓
SQLite Database
        ↓
← Response flows back up
```

### Example: Rolling Dice

```
1. User types "2d6+3" in DiceRoller component
2. User clicks "Roll" button
3. Component calls API: POST /dice/roll {"notation": "2d6+3"}
4. FastAPI receives request
5. Validates input with Pydantic model
6. Calls DiceService.roll_dice("2d6+3")
7. Service parses notation, generates random numbers
8. Stores result in roll history (in-memory or DB)
9. Returns result: {"notation": "2d6+3", "rolls": [4,5], "total": 12}
10. Frontend displays result to user
```

---

## 🗄️ Database Schema

### Current Tables

#### characters
```sql
CREATE TABLE characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    ancestry VARCHAR(50),
    background VARCHAR(50),
    class_name VARCHAR(50),
    level INTEGER DEFAULT 1,
    
    -- Ability Scores
    strength INTEGER,
    dexterity INTEGER,
    constitution INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    
    -- Combat Stats
    hit_points INTEGER,
    armor_class INTEGER,
    initiative INTEGER,
    
    -- Additional Data (JSON)
    skills TEXT,           -- JSON array of skill proficiencies
    feats TEXT,           -- JSON array of feats
    inventory TEXT,       -- JSON array of items
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Future Tables

#### encounters (planned)
```sql
CREATE TABLE encounters (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    challenge_rating FLOAT,
    monsters TEXT,  -- JSON array
    difficulty VARCHAR(20),
    created_at TIMESTAMP
);
```

#### initiative_tracker (planned)
```sql
CREATE TABLE initiative_entries (
    id INTEGER PRIMARY KEY,
    encounter_id INTEGER,
    name VARCHAR(100),
    initiative_value INTEGER,
    is_player BOOLEAN,
    current_hp INTEGER,
    max_hp INTEGER,
    FOREIGN KEY (encounter_id) REFERENCES encounters(id)
);
```

---

## 🔌 API Design

### RESTful Principles

- **Resource-based URLs:** `/characters`, `/encounters`
- **HTTP verbs:** GET, POST, PUT, DELETE
- **Status codes:** 200 OK, 201 Created, 404 Not Found, 400 Bad Request
- **JSON format:** All requests and responses use JSON
- **Consistent structure:** Predictable response format

### API Endpoint Patterns

```
# Collection endpoints (plural nouns)
GET    /characters          # List all
POST   /characters          # Create new

# Item endpoints (with ID)
GET    /characters/{id}     # Get specific
PUT    /characters/{id}     # Update
DELETE /characters/{id}     # Delete

# Action endpoints (verbs)
POST   /dice/roll           # Roll dice
POST   /characters/{id}/damage  # Apply damage
```

### Request/Response Format

**Request:**
```json
{
  "field_name": "value",
  "another_field": 123
}
```

**Successful Response:**
```json
{
  "id": 1,
  "field_name": "value",
  "created_at": "2025-11-03T12:00:00Z"
}
```

**Error Response:**
```json
{
  "detail": "Error message explaining what went wrong"
}
```

---

## 🧩 Component Architecture (Frontend)

### Component Hierarchy

```
App (main layout)
├── Header
├── Navigation
└── Router
    ├── Home
    ├── DiceRoller          (implemented)
    │   └── DiceHistory
    ├── CharacterSheet      (future)
    │   ├── AbilityScores
    │   ├── SkillsTab
    │   └── InventoryTab
    ├── EncounterBuilder    (future)
    │   └── MonsterList
    └── InitiativeTracker   (future)
        └── InitiativeEntry
```

### Component Responsibilities

**DiceRoller:**
- Input for dice notation
- Roll button and modifiers
- Display results
- Show roll history
- Call API for rolls

**CharacterSheet (planned):**
- Display character stats
- Edit character details
- Apply damage/healing
- Manage inventory
- Level up functionality

**EncounterBuilder (planned):**
- Select monsters
- Set difficulty
- Generate balanced encounters
- Save encounters

---

## 🔒 Security Considerations

### Current (Development)

- **CORS:** Enabled for localhost only
- **Input Validation:** Pydantic models validate all inputs
- **SQL Injection:** Protected by SQLAlchemy ORM
- **No Authentication:** Open API for local development

### Future (Production)

**Must Add:**
- User authentication (JWT tokens)
- API rate limiting
- HTTPS/TLS encryption
- Environment-based CORS
- Input sanitization for file uploads
- Database backups

---

## 🧪 Testing Strategy

### Current Tests

**Backend:**
- Unit tests for dice service
- API endpoint tests
- Database model tests

**Frontend:**
- Component rendering tests (future)
- Integration tests (future)

### Test Coverage Goals

- **Backend:** 80%+ code coverage
- **Critical Paths:** 100% (dice rolling, character CRUD)
- **Edge Cases:** Tested for all user inputs

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests (future)
cd frontend
npm test
```

---

## 📊 Performance Considerations

### Current Performance

- **API Response Time:** <50ms for most endpoints
- **Database Queries:** Direct SQLite, no optimization needed yet
- **Frontend Bundle:** ~200KB gzipped

### Scalability Plans

**When to Optimize:**
- Database: Switch to PostgreSQL if >10k characters
- Caching: Add Redis for frequently accessed data
- CDN: Use for static assets in production
- API: Add pagination for large lists

---

## 🛣️ Development Roadmap

### Phase 1: MVP (Current)
✅ Dice rolling
✅ Character CRUD
✅ Encounter generation
✅ Basic frontend

### Phase 2: Core Features (Next 2 months)
- Initiative tracker
- Character sheet UI
- Combat tracker
- Spell database

### Phase 3: Advanced Features (Months 3-4)
- PDF parsing
- Campaign management
- Party system
- Session notes

### Phase 4: Production (Month 5)
- User authentication
- Cloud deployment
- Mobile responsive
- Performance optimization

---

## 🔧 Configuration

### Environment Variables

**Backend (.env):**
```env
DATABASE_URL=sqlite:///./data/sqlite/pathfinder.db
CORS_ORIGINS=http://localhost:5173
DEBUG=true
SECRET_KEY=your-secret-key-here  # Future use
```

**Frontend (.env):**
```env
VITE_API_URL=http://localhost:8000
```

### Configuration Files

**backend/app/main.py:**
- CORS settings
- API routers
- Startup/shutdown events

**frontend/vite.config.ts:**
- Dev server port
- Proxy settings (if needed)
- Build optimization

**frontend/tailwind.config.js:**
- Custom colors (Pathfinder theme)
- Custom fonts
- Responsive breakpoints

---

## 📝 Code Standards

### Python (Backend)

- **Style:** PEP 8
- **Type Hints:** Used throughout
- **Docstrings:** All public functions
- **Naming:** snake_case for functions/variables

Example:
```python
def calculate_ability_modifier(ability_score: int) -> int:
    """Calculate the ability modifier for a given score.
    
    Args:
        ability_score: The ability score (1-30)
        
    Returns:
        The calculated modifier (-5 to +10)
    """
    return (ability_score - 10) // 2
```

### TypeScript (Frontend)

- **Style:** ESLint + Prettier
- **Type Safety:** Strict mode enabled
- **Naming:** camelCase for variables, PascalCase for components

Example:
```typescript
interface DiceRollResult {
  notation: string;
  rolls: number[];
  modifier: number;
  total: number;
}

const rollDice = async (notation: string): Promise<DiceRollResult> => {
  const response = await api.post('/dice/roll', { notation });
  return response.data;
};
```

---

## 🤝 Contributing Guidelines

### Git Workflow

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes and commit: `git commit -m "feat: add initiative tracker"`
3. Push to GitHub: `git push origin feature/your-feature`
4. Create Pull Request
5. Wait for review
6. Merge to main

### Commit Message Format

```
type(scope): short description

Longer description if needed.

- Bullet points for details
- List any breaking changes
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Build/config changes

---

## 🎓 Key Design Decisions

### Why FastAPI?
- Auto-generated API documentation
- Type safety with Pydantic
- Async support for scalability
- Easy to learn and use

### Why React + TypeScript?
- Type safety prevents bugs
- Large community and ecosystem
- Component reusability
- Modern development experience

### Why SQLite?
- No server setup needed
- Perfect for local development
- Easy to migrate to PostgreSQL later
- File-based, portable

### Why Tailwind CSS?
- Utility-first approach
- No CSS file management
- Consistent design system
- Highly customizable

---

## 📚 Additional Resources

**FastAPI:**
- Docs: https://fastapi.tiangolo.com/
- Tutorial: https://fastapi.tiangolo.com/tutorial/

**React + TypeScript:**
- React Docs: https://react.dev/
- TypeScript Handbook: https://www.typescriptlang.org/docs/

**SQLAlchemy:**
- Docs: https://docs.sqlalchemy.org/
- Tutorial: https://docs.sqlalchemy.org/en/20/tutorial/

**Pathfinder 2e:**
- SRD: https://2e.aonprd.com/
- Rules: https://2e.aonprd.com/Rules.aspx

---

## 🎉 Summary

This architecture provides:
- ✅ Clean separation of concerns
- ✅ Type safety throughout
- ✅ Scalable structure
- ✅ Easy to test
- ✅ Well-documented
- ✅ Simple to extend

**Perfect foundation for building a comprehensive Pathfinder companion app!** 🎲
