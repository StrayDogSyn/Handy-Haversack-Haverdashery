# System Architecture - Handy Haversack Haverdashery

## High-Level Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      USER BROWSER                           │
│                   http://localhost:3000                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ HTTP Requests
                     │ (Axios)
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   REACT FRONTEND                            │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐           │
│  │ DiceRoller │  │ Character  │  │ Encounter  │           │
│  │ Component  │  │   Sheet    │  │ Generator  │           │
│  └────────────┘  └────────────┘  └────────────┘           │
│                                                             │
│  ┌──────────────────────────────────────────────┐          │
│  │         API Service Layer (Axios)            │          │
│  └──────────────────────────────────────────────┘          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ REST API Calls
                     │ JSON
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              FASTAPI BACKEND SERVER                         │
│              http://localhost:8000                          │
│                                                             │
│  ┌─────────────────────────────────────────────┐           │
│  │            API ROUTES (/api)                │           │
│  ├──────────────┬──────────────┬───────────────┤           │
│  │ /characters  │    /dice     │  /encounters  │           │
│  │              │              │               │           │
│  │  - GET /     │  - POST roll │  - POST gen   │           │
│  │  - POST /    │  - GET hist  │  - GET mons   │           │
│  │  - GET /{id} │              │               │           │
│  │  - PUT /{id} │              │               │           │
│  │  - DELETE    │              │               │           │
│  └──────┬───────┴──────┬───────┴──────┬────────┘           │
│         │              │              │                    │
│         ▼              ▼              ▼                    │
│  ┌──────────────────────────────────────────┐             │
│  │          SERVICE LAYER                   │             │
│  ├────────────┬─────────────┬───────────────┤             │
│  │ Character  │ Dice        │  Encounter    │             │
│  │ Logic      │ Engine      │  Generator    │             │
│  └────────────┴─────────────┴───────────────┘             │
│         │                                                  │
│         │ SQLAlchemy ORM                                   │
│         ▼                                                  │
│  ┌──────────────────────────────────────────┐             │
│  │        DATABASE MODELS                   │             │
│  │  - Character (table: characters)         │             │
│  │  - Future: Spell, Item, Monster          │             │
│  └──────────────────────────────────────────┘             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ SQL Queries
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 SQLite DATABASE                             │
│           data/sqlite/pathfinder.db                         │
│                                                             │
│  Tables:                                                    │
│  - characters (id, name, stats, etc.)                       │
│  - Future: spells, items, monsters                          │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow Examples

### Example 1: Rolling Dice

```
USER clicks "Roll 1d20+5"
    ↓
DiceRoller component
    ↓
axios.post('/api/dice/roll', {expression: '1d20+5'})
    ↓
FastAPI receives request
    ↓
/api/dice.py → roll_dice()
    ↓
dice_engine.py → roll()
    ↓
Returns: {rolls: [15], total: 20, ...}
    ↓
FastAPI sends JSON response
    ↓
DiceRoller component updates state
    ↓
USER sees result: 20
```

### Example 2: Creating a Character

```
USER fills out character form
    ↓
CharacterSheet component
    ↓
axios.post('/api/characters/', characterData)
    ↓
FastAPI receives request
    ↓
/api/characters.py → create_character()
    ↓
Validates with Pydantic schema
    ↓
Creates Character model instance
    ↓
SQLAlchemy inserts into database
    ↓
Returns new character with ID
    ↓
FastAPI sends JSON response
    ↓
CharacterSheet shows success
    ↓
USER sees new character
```

### Example 3: Generating Encounter

```
USER sets party level=5, size=4, difficulty=moderate
    ↓
EncounterGenerator component
    ↓
axios.post('/api/encounters/generate', encounterParams)
    ↓
FastAPI receives request
    ↓
/api/encounters.py → generate_encounter()
    ↓
encounter_generator.py calculates target CR
    ↓
Selects monsters from bestiary
    ↓
Returns: {monsters: [...], total_cr: 5.5, ...}
    ↓
FastAPI sends JSON response
    ↓
EncounterGenerator displays monsters
    ↓
USER sees encounter ready to run
```

## Technology Stack Detail

### Frontend Stack
```
React 18
├── TypeScript (type safety)
├── Tailwind CSS (styling)
├── Axios (HTTP client)
└── React Router (navigation - future)
```

### Backend Stack
```
FastAPI
├── Uvicorn (ASGI server)
├── SQLAlchemy (ORM)
├── Pydantic (validation)
├── Python 3.11+
└── SQLite → PostgreSQL (future)
```

## Directory Structure Deep Dive

```
backend/app/
├── api/                    # HTTP endpoints
│   ├── characters.py       # Character CRUD routes
│   ├── dice.py            # Dice rolling routes
│   └── encounters.py       # Encounter generation routes
├── models/                 # Data models
│   ├── character.py        # SQLAlchemy model
│   └── schemas.py          # Pydantic schemas (validation)
├── services/               # Business logic
│   ├── dice_engine.py      # Dice rolling logic
│   └── encounter_generator.py  # Encounter creation
├── utils/                  # Helper functions
├── database.py             # DB connection & config
└── main.py                 # FastAPI app initialization

frontend/src/
├── components/             # React components
│   ├── DiceRoller.tsx      # ✅ Complete
│   ├── CharacterSheet.tsx  # TODO
│   └── EncounterDisplay.tsx # TODO
├── services/               # API calls
│   └── api.ts             # TODO: Axios configuration
├── hooks/                  # Custom React hooks
│   └── useCharacter.ts    # TODO
├── types/                  # TypeScript types
│   └── character.ts       # TODO
└── App.tsx                 # Main app component
```

## API Endpoint Map

```
BASE URL: http://localhost:8000

/                           GET    Health check
/api/health                 GET    API health status

/api/characters/            GET    List all characters
                           POST   Create character
/api/characters/{id}        GET    Get specific character
                           PUT    Update character
                           DELETE Delete character
/api/characters/{id}/damage POST   Apply damage
/api/characters/{id}/heal   POST   Heal character

/api/dice/roll             POST   Roll dice
/api/dice/roll-multiple    POST   Roll multiple times
/api/dice/history          GET    Get roll history
                           DELETE Clear history
/api/dice/supported-dice   GET    List valid dice types

/api/encounters/generate    POST   Generate encounter
/api/encounters/monsters    GET    List available monsters
/api/encounters/difficulty-guide GET Get CR guidelines
```

## Database Schema

```sql
-- Current Schema

Table: characters
├── id (INTEGER PRIMARY KEY)
├── name (VARCHAR)
├── player_name (VARCHAR)
├── race (VARCHAR)
├── character_class (VARCHAR)
├── level (INTEGER)
├── alignment (VARCHAR)
├── deity (VARCHAR)
├── strength (INTEGER)
├── dexterity (INTEGER)
├── constitution (INTEGER)
├── intelligence (INTEGER)
├── wisdom (INTEGER)
├── charisma (INTEGER)
├── hit_points_max (INTEGER)
├── hit_points_current (INTEGER)
├── armor_class (INTEGER)
├── initiative (INTEGER)
├── skills (JSON)
├── feats (JSON)
├── inventory (JSON)
├── spells (JSON)
├── notes (TEXT)
├── created_at (DATETIME)
└── updated_at (DATETIME)

-- Future Tables
- spells (id, name, level, school, ...)
- items (id, name, cost, weight, ...)
- monsters (id, name, cr, hp, ac, ...)
- campaigns (id, name, dm, ...)
- sessions (id, campaign_id, date, notes, ...)
```

## Development Flow

```
Feature Development Cycle:

1. PLAN
   ├── Identify feature
   ├── Design API if needed
   └── Create GitHub issue

2. BACKEND
   ├── Create/update model
   ├── Write service logic
   ├── Add API endpoint
   ├── Write tests
   └── Test in /docs

3. FRONTEND
   ├── Create component
   ├── Add API call
   ├── Style with Tailwind
   └── Test in browser

4. INTEGRATE
   ├── Connect frontend to backend
   ├── Test full flow
   └── Handle errors

5. DEPLOY
   ├── Commit changes
   ├── Create PR
   ├── Review
   └── Merge to main
```

---

## Next Features to Build

**Backend:**
- [ ] Initiative tracker service
- [ ] Spell database
- [ ] PDF parser
- [ ] Combat calculator

**Frontend:**
- [ ] Character sheet component
- [ ] Encounter display
- [ ] Initiative tracker UI
- [ ] Navigation menu

**Integration:**
- [ ] Real-time updates
- [ ] User authentication
- [ ] Campaign management
- [ ] Export/import characters

---

This architecture is designed to be:
- **Modular**: Each component has a single responsibility
- **Scalable**: Easy to add new features without breaking existing ones
- **Testable**: Each layer can be tested independently
- **Maintainable**: Clear structure makes it easy to find and fix issues
