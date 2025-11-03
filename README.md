# Handy-Haversack-Haverdashery

A comprehensive Pathfinder TTRPG companion application featuring character management, dice rolling, and encounter generation.

## Features

- **Character Sheets**: Create, edit, and manage character sheets with full ability scores and stats
- **Dice Roller**: Roll any dice from d4 to d100 with modifiers (supports multiple dice)
- **CR-Based Encounter Generator**: Generate balanced encounters based on party level and difficulty
- **Modern UI**: Built with React, TypeScript, and Tailwind CSS
- **FastAPI Backend**: High-performance Python backend with SQLite database

## Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight database for development
- **Uvicorn**: ASGI server

### Frontend
- **React 18**: UI library
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Utility-first CSS framework
- **React Scripts**: Build tooling

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

The backend will be available at http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The frontend will be available at http://localhost:3000

## API Documentation

Once the backend is running, visit http://localhost:8000/docs for interactive API documentation (Swagger UI).

### Main Endpoints

- `GET /api/characters/` - List all characters
- `POST /api/characters/` - Create a new character
- `GET /api/characters/{id}` - Get a specific character
- `PUT /api/characters/{id}` - Update a character
- `DELETE /api/characters/{id}` - Delete a character
- `POST /api/dice/roll` - Roll dice with modifiers
- `POST /api/encounters/generate` - Generate an encounter

## Usage

### Character Management

1. Click on the "📜 Characters" tab
2. Click "New Character" to create a character
3. Fill in the character details including name, class, race, and stats
4. Save the character
5. Select a character from the list to view or edit

### Dice Rolling

1. Click on the "🎲 Dice Roller" tab
2. Select the type of dice (d4, d6, d8, d10, d12, d20, d100)
3. Choose the number of dice to roll
4. Add any modifiers (positive or negative)
5. Click "Roll Dice" to see the results

### Encounter Generation

1. Click on the "⚔️ Encounters" tab
2. Set the party level (1-20)
3. Set the number of players
4. Choose difficulty (Easy, Medium, Hard, Deadly)
5. Click "Generate Encounter" to create a balanced encounter

## Development

### Backend Testing

The backend includes sample monsters seeded on startup. You can modify the monster data in `backend/main.py`.

### Frontend Development

The frontend uses React with TypeScript and Tailwind CSS. All components are located in `frontend/src/components/`.

## Project Structure

```
.
├── backend/
│   ├── main.py           # FastAPI application and routes
│   ├── database.py       # Database models and configuration
│   ├── schemas.py        # Pydantic schemas for validation
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── CharacterSheet.tsx
│   │   │   ├── DiceRoller.tsx
│   │   │   └── EncounterGenerator.tsx
│   │   ├── services/
│   │   │   └── api.ts    # API client
│   │   ├── App.tsx       # Main app component
│   │   ├── index.tsx     # Entry point
│   │   └── index.css     # Tailwind styles
│   ├── package.json
│   ├── tsconfig.json
│   └── tailwind.config.js
└── README.md
```

## Contributing

This is a personal project, but suggestions and improvements are welcome!

## License

See LICENSE file for details.
