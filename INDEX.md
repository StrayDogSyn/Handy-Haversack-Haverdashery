# 📚 Handy Haversack Haverdashery - Documentation Index

Welcome to your complete Pathfinder companion app! This document is your roadmap to all the documentation and resources in this project.

---

## 🚀 Start Here

**Brand new to the project?**
1. Read: [PROJECT_SUMMARY.md](../PROJECT_SUMMARY.md) - Overview of what we built
2. Follow: [GETTING_STARTED.md](GETTING_STARTED.md) - Complete setup guide
3. Reference: [QUICK_REFERENCE.md](../QUICK_REFERENCE.md) - Command cheat sheet

---

## 📖 Core Documentation

### Project Overview
- **[README.md](../README.md)** - Project description, tech stack, and basic info
- **[PROJECT_SUMMARY.md](../PROJECT_SUMMARY.md)** - What's complete, what's next, task division

### Setup Guides
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Detailed setup instructions for new developers
- **[setup-windows.bat](../setup-windows.bat)** - Automated setup for Windows
- **[setup-unix.sh](../setup-unix.sh)** - Automated setup for Mac/Linux

### Quick References
- **[QUICK_REFERENCE.md](../QUICK_REFERENCE.md)** - Commands, troubleshooting, API testing
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture and data flow diagrams

### Development
- **[INITIAL_TASKS.md](INITIAL_TASKS.md)** - Week-by-week tasks for each developer
- **[../data/pdfs/README.md](../data/pdfs/README.md)** - PDF storage guidelines

---

## 🗂️ Project Structure

```
pathfinder-companion/
│
├── 📄 Documentation (Start Here!)
│   ├── README.md                  ← Project overview
│   ├── PROJECT_SUMMARY.md         ← What we built
│   ├── QUICK_REFERENCE.md         ← Commands cheat sheet
│   └── docs/
│       ├── GETTING_STARTED.md     ← Setup guide
│       ├── ARCHITECTURE.md        ← System design
│       └── INITIAL_TASKS.md       ← Development tasks
│
├── 🐍 Backend (Python + FastAPI)
│   ├── app/
│   │   ├── api/                   ← API endpoints
│   │   │   ├── characters.py      ← Character CRUD
│   │   │   ├── dice.py           ← Dice rolling
│   │   │   └── encounters.py     ← Encounter generator
│   │   ├── models/               ← Data models
│   │   │   ├── character.py      ← Database model
│   │   │   └── schemas.py        ← Validation schemas
│   │   ├── services/             ← Business logic
│   │   │   ├── dice_engine.py    ← Dice rolling engine
│   │   │   └── encounter_generator.py
│   │   ├── database.py           ← DB configuration
│   │   └── main.py               ← FastAPI app entry
│   ├── tests/
│   │   └── test_dice.py          ← Dice roller tests
│   └── requirements.txt          ← Python dependencies
│
├── ⚛️ Frontend (React + TypeScript)
│   ├── src/
│   │   └── components/
│   │       └── DiceRoller.tsx    ← Complete dice roller UI
│   ├── package.json              ← Node dependencies
│   └── tailwind.config.js        ← Styling config
│
├── 💾 Data
│   ├── pdfs/                     ← Your Pathfinder PDFs
│   ├── json/                     ← Parsed game data
│   └── sqlite/                   ← Database (auto-created)
│
└── 🛠️ Setup Scripts
    ├── setup-windows.bat         ← Windows setup
    └── setup-unix.sh             ← Mac/Linux setup
```

---

## 🎯 Quick Navigation

### I want to...

**...set up the project for the first time**
→ [GETTING_STARTED.md](GETTING_STARTED.md)

**...understand how the system works**
→ [ARCHITECTURE.md](ARCHITECTURE.md)

**...know what to build next**
→ [INITIAL_TASKS.md](INITIAL_TASKS.md)

**...find a command I forgot**
→ [QUICK_REFERENCE.md](../QUICK_REFERENCE.md)

**...understand the project scope**
→ [PROJECT_SUMMARY.md](../PROJECT_SUMMARY.md)

**...see available API endpoints**
→ Run backend and visit: http://localhost:8000/docs

**...test the dice roller**
→ Start both servers, visit: http://localhost:3000

---

## 📊 Current Feature Status

### ✅ Complete (MVP)
- Dice roller with modifiers and advantage/disadvantage
- Character CRUD operations with full stats
- CR-based encounter generator with 20+ monsters
- SQLite database with character table
- React dice roller component with Tailwind styling
- Complete API documentation
- Comprehensive setup and development docs

### 🔨 In Progress
- Nothing yet - fresh project ready for development!

### 📋 Planned (Phase 2)
- Character sheet UI component
- Initiative tracker (backend + frontend)
- Encounter display component
- Navigation and routing
- More monsters in bestiary

### 🌟 Future (Phase 3+)
- PDF parsing for automatic content import
- Spell database and search
- Inventory management system
- Campaign session tracking
- Combat calculator
- Party management

---

## 🧪 Testing & Validation

### Backend Testing
```bash
# Run dice roller tests
pytest backend/tests/test_dice.py

# Test API interactively
# Visit: http://localhost:8000/docs
```

### Frontend Testing
```bash
# Start dev server
npm start

# Test in browser
# Visit: http://localhost:3000
```

### Manual API Testing
See [QUICK_REFERENCE.md](../QUICK_REFERENCE.md) for curl commands

---

## 🛠️ Development Workflow

1. **Pick a task** from [INITIAL_TASKS.md](INITIAL_TASKS.md)
2. **Create branch**: `git checkout -b feature/your-feature`
3. **Build feature** (reference [ARCHITECTURE.md](ARCHITECTURE.md) for structure)
4. **Test locally** (see Quick Reference for commands)
5. **Commit**: `git commit -m "Add: feature description"`
6. **Push**: `git push origin feature/your-feature`
7. **Create PR** on GitHub
8. **Review & merge**

---

## 📞 Getting Help

### Common Issues
Check [QUICK_REFERENCE.md](../QUICK_REFERENCE.md) → Troubleshooting section

### Understanding the Code
Read [ARCHITECTURE.md](ARCHITECTURE.md) for data flow diagrams

### Task Questions
See [INITIAL_TASKS.md](INITIAL_TASKS.md) for detailed task breakdowns

### Setup Problems
See [GETTING_STARTED.md](GETTING_STARTED.md) → Troubleshooting

---

## 📈 Version History

**v0.1.0 - MVP Release**
- ✅ Dice roller backend + frontend
- ✅ Character management API
- ✅ Encounter generator
- ✅ Complete documentation
- ✅ Setup automation scripts

**v0.2.0 - Planned**
- Initiative tracker
- Character sheet UI
- Expanded bestiary

---

## 🎲 Tech Stack Reference

### Backend
- **Python 3.11+**
- **FastAPI** - Modern web framework
- **SQLAlchemy** - ORM for database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **SQLite** → PostgreSQL migration path

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first styling
- **Axios** - HTTP client
- **React Router** (planned) - Navigation

---

## 📝 Conventions

### Code Style
- **Python**: Follow PEP 8, use `black` for formatting
- **TypeScript**: Use Prettier, functional components
- **Naming**: descriptive_snake_case (Python), camelCase (TypeScript)

### Git Commits
- **Add**: New features
- **Fix**: Bug fixes
- **Update**: Improvements to existing code
- **Docs**: Documentation changes
- **Test**: Test additions/changes
- **Style**: Code formatting (no logic changes)

### API Design
- RESTful endpoints
- JSON request/response
- Proper HTTP status codes
- Comprehensive error messages

---

## 🎯 Goals & Principles

**Project Goals:**
1. Create a genuinely useful Pathfinder companion tool
2. Build portfolio-worthy full-stack application
3. Practice collaborative development with Git
4. Learn modern web development practices

**Development Principles:**
1. **Incremental**: One feature at a time
2. **Tested**: Test before committing
3. **Documented**: Code should explain itself
4. **Collaborative**: Review each other's work
5. **Fun**: Enjoy the process!

---

## 🏆 Project Roadmap

### Month 1: Foundation (Done!)
- ✅ Project setup
- ✅ Core features (dice, characters, encounters)
- ✅ Documentation

### Month 2: UI & UX
- Character sheet components
- Initiative tracker
- Improved styling and UX

### Month 3: Advanced Features
- PDF parsing
- Spell database
- Campaign tracking

### Month 4: Polish & Deploy
- Performance optimization
- Testing coverage
- Production deployment
- User documentation

---

## 🌟 Contributing

This is a collaborative learning project between:
- **StrayDogSyn** - Backend focus, project lead
- **jamesbeattie221@gmail.com (GrumbleBee)** - Frontend focus

For task assignments, see [INITIAL_TASKS.md](INITIAL_TASKS.md)

---

## 📜 License

Creative Commons Zero v1.0 Universal

This project is open source and available for learning, modification, and personal use.

---

## 🎉 Let's Build Something Awesome!

You have everything you need:
- ✅ Complete working MVP
- ✅ Clear development path
- ✅ Comprehensive documentation
- ✅ Defined tasks for each developer

**Ready to start coding?**

1. Run setup: `setup-windows.bat` or `./setup-unix.sh`
2. Read: [GETTING_STARTED.md](GETTING_STARTED.md)
3. Pick task: [INITIAL_TASKS.md](INITIAL_TASKS.md)
4. Start building! 🎲

---

*"The dice are cast. Let's see what you roll."* - Julius Caesar (probably)
