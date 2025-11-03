# Contributing to Handy Haversack Haverdashery

Thank you for contributing to the Pathfinder 2e Companion App! This guide will help you get started with our development workflow and coding standards.

## 👥 Team Structure

- **Backend Developer** (StrayDogSyn): Python/FastAPI, database, services, API endpoints
- **Frontend Developer** (GrumbleBee): React/TypeScript, UI components, styling, routing

## 🚀 Getting Started

### 1. Clone and Setup

```bash
git clone https://github.com/StrayDogSyn/Handy-Haversack-Haverdashery.git
cd Handy-Haversack-Haverdashery

# Run automated setup
.\setup-windows.bat  # Windows
# OR
./setup-unix.sh      # Mac/Linux
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Your Changes

Follow the coding standards below and test your work.

### 4. Commit and Push

```bash
git add .
git commit -m "feat: add initiative tracker"
git push origin feature/your-feature-name
```

### 5. Open a Pull Request

- Go to GitHub and open a PR from your branch to `main`
- Add a clear description of what you changed and why
- Request review from your teammate
- Address any feedback and update your PR

## 📝 Coding Standards

### Python (Backend)

#### File Organization
```
backend/app/
├── api/              # REST endpoint routers
├── models/           # SQLAlchemy database models
├── services/         # Business logic layer
├── schemas/          # Pydantic validation schemas (future)
└── utils/            # Helper functions (future)
```

#### Naming Conventions
- **Files**: `snake_case.py` (e.g., `dice_service.py`)
- **Classes**: `PascalCase` (e.g., `Character`, `DiceService`)
- **Functions**: `snake_case()` (e.g., `roll_dice()`, `generate_encounter()`)
- **Variables**: `snake_case` (e.g., `party_level`, `monster_list`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_PARTY_SIZE`, `DEFAULT_DICE`)

#### Code Style
- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints for function parameters and return values
- Maximum line length: 100 characters
- Use docstrings for all public functions/classes

```python
def roll_dice(notation: str, modifier: int = 0) -> dict:
    """
    Roll dice using standard notation (e.g., "2d6+3").
    
    Args:
        notation: Dice notation string (XdY format)
        modifier: Additional modifier to add to roll
        
    Returns:
        Dictionary with roll results and breakdown
    """
    # Implementation here
    pass
```

#### FastAPI Best Practices
- Use dependency injection for database sessions
- Define Pydantic models for request/response validation
- Add proper HTTP status codes
- Include error handling with try/except blocks

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

@router.post("/characters", status_code=status.HTTP_201_CREATED)
async def create_character(
    character: CharacterCreate,
    db: Session = Depends(get_db)
):
    try:
        # Implementation
        return character
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
```

#### Testing
- Write tests for all new features in `backend/tests/`
- Use `pytest` with descriptive test names
- Aim for >80% code coverage

```python
def test_roll_dice_returns_correct_range():
    """Test that dice rolls are within valid range."""
    result = roll_dice("1d6")
    assert 1 <= result["total"] <= 6
```

### TypeScript/React (Frontend)

#### File Organization
```
frontend/src/
├── components/       # React components
├── hooks/           # Custom React hooks (future)
├── services/        # API client services (future)
├── types/           # TypeScript type definitions (future)
├── utils/           # Helper functions (future)
└── styles/          # Additional CSS (future)
```

#### Naming Conventions
- **Files**: `PascalCase.tsx` for components (e.g., `DiceRoller.tsx`)
- **Files**: `camelCase.ts` for utilities (e.g., `apiClient.ts`)
- **Components**: `PascalCase` (e.g., `CharacterSheet`, `DiceRoller`)
- **Functions**: `camelCase()` (e.g., `handleRoll()`, `calculateModifier()`)
- **Variables**: `camelCase` (e.g., `diceNotation`, `rollHistory`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `API_BASE_URL`, `MAX_ROLLS`)
- **Interfaces/Types**: `PascalCase` (e.g., `Character`, `DiceRoll`)

#### Code Style
- Use functional components with hooks (no class components)
- Use TypeScript for type safety (avoid `any` type)
- Maximum line length: 100 characters
- Use Prettier for consistent formatting

```typescript
interface DiceRollResult {
  notation: string;
  total: number;
  rolls: number[];
  timestamp: string;
}

const DiceRoller: React.FC = () => {
  const [notation, setNotation] = useState<string>('1d20');
  const [history, setHistory] = useState<DiceRollResult[]>([]);

  const handleRoll = async (): Promise<void> => {
    try {
      const response = await axios.post('/api/dice/roll', { notation });
      setHistory([response.data, ...history]);
    } catch (error) {
      console.error('Roll failed:', error);
    }
  };

  return (
    // JSX here
  );
};
```

#### React Best Practices
- Keep components small and focused (single responsibility)
- Extract reusable logic into custom hooks
- Use meaningful prop names and destructure them
- Add PropTypes or TypeScript interfaces for all props

```typescript
interface CharacterCardProps {
  character: Character;
  onEdit: (id: number) => void;
  onDelete: (id: number) => void;
}

export const CharacterCard: React.FC<CharacterCardProps> = ({
  character,
  onEdit,
  onDelete
}) => {
  // Component implementation
};
```

#### Styling with Tailwind
- Use Tailwind utility classes for styling
- Keep custom CSS minimal
- Use Pathfinder theme colors defined in `tailwind.config.js`
- Group related classes logically

```typescript
<button className="bg-pathfinder-red text-pathfinder-gold px-6 py-3 rounded-lg hover:bg-red-900 transition-colors">
  Roll Dice
</button>
```

## 🌿 Branch Naming

Use descriptive branch names with prefixes:

- `feature/` - New features (e.g., `feature/initiative-tracker`)
- `fix/` - Bug fixes (e.g., `fix/dice-validation`)
- `refactor/` - Code improvements (e.g., `refactor/character-service`)
- `docs/` - Documentation updates (e.g., `docs/api-reference`)
- `test/` - Test additions (e.g., `test/encounter-generation`)
- `chore/` - Maintenance tasks (e.g., `chore/update-dependencies`)

## 💬 Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>: <description>

[optional body]

[optional footer]
```

### Types
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `style` - Code style/formatting (no logic changes)
- `refactor` - Code restructuring (no feature changes)
- `test` - Adding or updating tests
- `chore` - Maintenance tasks

### Examples
```
feat: add initiative tracker API endpoints

Implements POST /api/initiative/start and GET /api/initiative/order
endpoints with full CRUD operations for combat tracking.

Closes #12
```

```
fix: correct dice roll validation for d100

Previously allowed invalid notation like "d100+1000", now properly
validates modifiers are reasonable.
```

```
docs: update API reference for character endpoints
```

## 🔍 Code Review Process

### For Authors
1. Ensure all tests pass before requesting review
2. Write clear PR description explaining changes
3. Keep PRs focused and reasonably sized (<500 lines if possible)
4. Respond to feedback constructively
5. Mark conversations as resolved when addressed

### For Reviewers
1. Review within 24 hours when possible
2. Focus on logic, readability, and best practices
3. Ask questions if something is unclear
4. Approve when satisfied, or request changes with specific feedback
5. Be constructive and respectful

### PR Checklist
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New features have tests
- [ ] Documentation updated if needed
- [ ] No console.log or debug code left in
- [ ] No sensitive data (API keys, passwords) committed
- [ ] Branch is up to date with main

## 🧪 Testing

### Backend Testing
```bash
cd backend
pytest tests/ -v                    # Run all tests
pytest tests/test_dice.py -v       # Run specific test file
pytest --cov=app tests/            # Run with coverage
```

### Frontend Testing
```bash
cd frontend
npm test                           # Run tests (when implemented)
npm run test:coverage              # Run with coverage
```

### Manual Testing
1. Start both servers (backend on :8000, frontend on :5173)
2. Test the feature in the UI
3. Check browser console for errors
4. Test API endpoints directly at http://localhost:8000/docs
5. Test edge cases and error scenarios

## 📚 Documentation

### When to Update Docs
- Adding new API endpoints → Update `docs/ARCHITECTURE.md`
- Adding new features → Update `docs/PROJECT_SUMMARY.md`
- Changing setup process → Update `docs/GETTING_STARTED.md`
- Adding new tasks → Update `docs/INITIAL_TASKS.md`

### API Documentation
FastAPI generates automatic API docs at `/docs`. Ensure your endpoint docstrings are clear:

```python
@router.post("/roll")
async def roll_dice(request: DiceRollRequest):
    """
    Roll dice using standard notation.
    
    Supports formats like "1d20", "2d6+3", "1d100-10"
    Returns the total, individual rolls, and history.
    """
    pass
```

## 🐛 Debugging Tips

### Backend
- Use `print()` or `logging` for debugging
- Check FastAPI logs in terminal
- Test endpoints directly at http://localhost:8000/docs
- Use `pytest --pdb` to debug failing tests

### Frontend
- Use browser DevTools (F12) Console tab
- Check Network tab for API call failures
- Use React DevTools extension
- Add `console.log()` for debugging (remove before committing!)

## ⚡ Performance Guidelines

### Backend
- Use database indexes for frequently queried fields
- Avoid N+1 queries (use SQLAlchemy's `joinedload()`)
- Cache expensive computations when possible
- Use async/await for I/O operations

### Frontend
- Minimize re-renders with `useMemo` and `useCallback`
- Lazy load components with `React.lazy()`
- Optimize images and assets
- Debounce search inputs and frequent API calls

## 🔒 Security

### Do NOT Commit
- API keys or secrets
- Database credentials
- `.env` files with real values
- Personal information

### Always
- Use environment variables for sensitive data
- Validate all user input on backend
- Sanitize data before displaying in UI
- Use parameterized SQL queries (SQLAlchemy handles this)

## 📞 Getting Help

- **Questions about tasks**: Check `docs/INITIAL_TASKS.md`
- **Setup issues**: Check `docs/GETTING_STARTED.md`
- **Architecture questions**: Check `docs/ARCHITECTURE.md`
- **General discussion**: Use GitHub Issues or Discussions
- **Urgent issues**: Contact your teammate directly

## 🎯 Sprint Planning

We work in 2-week sprints. Check `docs/roadmap/roadmap.html` for current sprint priorities.

### Sprint Process
1. **Sprint Planning** (Monday Week 1): Pick tasks from backlog
2. **Daily Standups** (async): Share progress in commits/PRs
3. **Sprint Review** (Friday Week 2): Demo completed features
4. **Sprint Retro** (Friday Week 2): Discuss what went well and improvements

## 📋 Task Management

Tasks are tracked in `docs/INITIAL_TASKS.md` with:
- **Priority**: P0 (Critical), P1 (High), P2 (Medium), P3 (Low)
- **Time Estimate**: Hours expected to complete
- **Dependencies**: What needs to be done first
- **Assignee**: Backend or Frontend developer

## ✅ Definition of Done

A task is "done" when:
- [ ] Code is written and follows style guidelines
- [ ] Tests are written and passing
- [ ] Documentation is updated
- [ ] PR is reviewed and approved
- [ ] Code is merged to main
- [ ] Feature works in production-like environment

---

## 🙏 Thank You!

Your contributions make this project possible. Happy coding! 🎲✨
