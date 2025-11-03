# 🎲 Handy Haversack Haverdashery

A comprehensive Pathfinder 2e companion application built with FastAPI and React.

## 🎯 Features

### Current Features (MVP)
- **Dice Roller**: Full support for dice notation (2d6+3, 1d20, etc.)
- **Advantage/Disadvantage**: Roll d20 with advantage or disadvantage
- **Character Management**: Complete CRUD operations for characters
- **Encounter Generator**: CR-based encounter creation with 30+ monsters
- **Roll History**: Track your recent rolls
- **API Documentation**: Auto-generated Swagger/OpenAPI docs

### Coming Soon
- Initiative tracker
- Character sheet UI
- Spell database and browser
- Campaign management
- PDF rulebook parsing

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Git

### Automated Setup

**Windows:**
```bash
setup-windows.bat
```

**Mac/Linux:**
```bash
chmod +x setup-unix.sh
./setup-unix.sh
```

### Manual Setup

See [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md) for detailed setup instructions.

### Running the Application

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Then open: **http://localhost:5173**

## 📚 Documentation

- **[Getting Started Guide](docs/GETTING_STARTED.md)** - Complete setup instructions
- **[Architecture Documentation](docs/ARCHITECTURE.md)** - System design and tech stack
- **[Initial Tasks](docs/INITIAL_TASKS.md)** - Development roadmap and task breakdown
- **[Quick Reference](QUICK_REFERENCE.md)** - Command cheat sheet
- **[Documentation Index](docs/INDEX.md)** - All documentation

## 🏗️ Tech Stack

**Backend:**
- FastAPI (Python web framework)
- SQLAlchemy ORM with SQLite
- Pydantic for validation
- pytest for testing

**Frontend:**
- React 18 with TypeScript
- Vite (build tool)
- Tailwind CSS
- Axios for API calls

## 🎮 API Endpoints

Visit **http://localhost:8000/docs** for full interactive API documentation.

### Key Endpoints
- `POST /dice/roll` - Roll dice with notation
- `GET /characters` - List all characters
- `POST /characters` - Create new character
- `POST /encounters/generate` - Generate balanced encounter
- `GET /bestiary` - View all monsters

## 📁 Project Structure

```
Handy-Haversack-Haverdashery/
├── backend/          # FastAPI backend
│   ├── app/
│   │   ├── api/      # Route handlers
│   │   ├── models/   # Database models
│   │   └── services/ # Business logic
│   ├── tests/        # Backend tests
│   └── data/         # SQLite database
├── frontend/         # React frontend
│   └── src/
│       └── components/
├── docs/            # Documentation
└── setup scripts    # Automated setup
```

## 🧪 Testing

```bash
cd backend
pytest
```

## 🤝 Contributing

This project is set up for collaborative development:

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and test
3. Commit: `git commit -m "feat: add your feature"`
4. Push: `git push origin feature/your-feature`
5. Create a Pull Request

See [docs/INITIAL_TASKS.md](docs/INITIAL_TASKS.md) for planned features and tasks.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎲 Credits

Built for Pathfinder 2e enthusiasts by StrayDogSyn and team.

*"In the beginning, there was a d20..." - Gary Gygax (probably)*

## 🆘 Support

- Check the [Getting Started Guide](docs/GETTING_STARTED.md#troubleshooting) for common issues
- Review the [Quick Reference](QUICK_REFERENCE.md) for commands
- Read the [Architecture Documentation](docs/ARCHITECTURE.md) to understand the system

---

**Ready to adventure?** 🗡️ Start rolling those dice!
A complex overhaul of all the combined repositories of the initial projects that contained the Pasa Phist Projects
