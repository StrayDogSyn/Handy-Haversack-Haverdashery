# Initial Tasks - Getting Started

## 🎯 Week 1: Setup & Familiarization

### Both Contributors (Setup)
- [ ] Clone the repository
- [ ] Run setup script (`setup-windows.bat` or `setup-unix.sh`)
- [ ] Get both backend and frontend running
- [ ] Test the dice roller in browser
- [ ] Test the API at http://localhost:8000/docs
- [ ] Create a test character via API
- [ ] Generate a test encounter via API

### Communication
- [ ] Set up Discord/Slack channel for quick questions
- [ ] Decide on meeting schedule (if any)
- [ ] Agree on Git workflow (branch naming, PR process)

---

## 🔧 StrayDogSyn - Backend Focus

### Week 1: Get Comfortable
**Goal: Understand the existing backend code**

- [ ] Read through `backend/app/main.py` - understand FastAPI setup
- [ ] Review `backend/app/services/dice_engine.py` - see how dice logic works
- [ ] Run `pytest backend/tests/test_dice.py` - see tests in action
- [ ] Create a test character using the API docs
- [ ] Generate 5 different encounters at various difficulty levels

**Mini Challenge:** Add a new dice type
- [ ] Add d3 (1-3) to the valid dice list
- [ ] Test it works: "1d3", "2d3+1"
- [ ] Commit and push

### Week 2: First Feature - Initiative Tracker

**Task: Build an initiative tracker system**

Files to create/modify:
- [ ] `backend/app/models/initiative.py` - database model
- [ ] `backend/app/services/initiative_tracker.py` - logic
- [ ] `backend/app/api/initiative.py` - API endpoints
- [ ] Update `backend/app/main.py` to include router

**API Endpoints to Create:**
```
POST /api/initiative/start
- Start new initiative tracker
- Input: encounter_id (optional), participants list
- Output: Tracker with turn order

POST /api/initiative/add-participant  
- Add character/monster to tracker
- Input: name, initiative_roll
- Output: Updated turn order

POST /api/initiative/next-turn
- Advance to next turn
- Output: Current turn details

GET /api/initiative/{tracker_id}
- Get current initiative status
- Output: Full tracker state
```

**Database Model:**
```python
class InitiativeTracker:
    id
    name (e.g., "Goblin Ambush")
    current_round
    current_turn_index
    participants (JSON list)
    is_active (boolean)
    created_at
```

**Stretch Goals:**
- [ ] Add damage tracking per participant
- [ ] Add status effects (prone, stunned, etc.)
- [ ] Add "delay action" feature

---

## 💻 jamesbeattie221 (GrumbleBee) - Frontend Focus

### Week 1: Get Comfortable  
**Goal: Understand React structure and existing code**

- [ ] Explore `frontend/src/components/DiceRoller.tsx` - see how it works
- [ ] Make a small style change (change a color in Tailwind)
- [ ] Add a new quick-roll button (like "8d6" for fireballs!)
- [ ] Test connecting to backend API
- [ ] Use browser DevTools to watch network requests

**Mini Challenge:** Improve DiceRoller UI
- [ ] Add a "Clear History" button
- [ ] Add animation when showing results (CSS transition)
- [ ] Make the result display "bounce" on new rolls
- [ ] Commit and push

### Week 2: First Feature - Character Sheet Component

**Task: Build a character sheet display component**

File to create:
- [ ] `frontend/src/components/CharacterSheet.tsx`

**Component Requirements:**

**Display Section:**
```typescript
- Character name (large, prominent)
- Class, Race, Level
- Ability Scores in grid (STR, DEX, CON, INT, WIS, CHA)
  - Show score and modifier (e.g., "16 (+3)")
- Combat stats: HP bar, AC, Initiative
- Skills list (from JSON)
- Feats list (from JSON)
```

**Edit Section:**
```typescript
- Form to create new character
- All fields editable
- Submit button calls API
- Success/error messages
```

**API Integration:**
```typescript
// In component
const [characters, setCharacters] = useState([]);
const [selectedChar, setSelectedChar] = useState(null);

// Load characters
useEffect(() => {
  axios.get('http://localhost:8000/api/characters/')
    .then(res => setCharacters(res.data));
}, []);

// Select character to view
const viewCharacter = (id) => {
  axios.get(`http://localhost:8000/api/characters/${id}`)
    .then(res => setSelectedChar(res.data));
};
```

**Styling with Tailwind:**
- Use card layout (bg-white rounded-lg shadow)
- Pathfinder colors from tailwind.config
- Responsive grid for stats
- Hover effects on buttons

**Stretch Goals:**
- [ ] Add HP modification buttons (+/-10 HP)
- [ ] Visual HP bar with color (green/yellow/red)
- [ ] Collapsible sections (skills, inventory)
- [ ] Character list with search/filter

---

## 🤝 Collaborative Tasks

### Week 1-2: Integration
- [ ] **Both:** Test character creation flow end-to-end
- [ ] **Both:** Ensure error handling works (try breaking things!)
- [ ] **StrayDog:** Review James's frontend PR
- [ ] **James:** Review StrayDog's backend PR

### Documentation
- [ ] **Both:** Update README if you add features
- [ ] **Both:** Add comments to complex code
- [ ] **StrayDog:** Document new API endpoints
- [ ] **James:** Screenshot new UI components

---

## 📋 GitHub Workflow

### Branch Naming Convention
```
feature/dice-roller-improvements
feature/initiative-tracker-backend
feature/character-sheet-component
bugfix/dice-validation-error
docs/update-getting-started
```

### Commit Message Format
```
Add: New feature (e.g., "Add: Initiative tracker API")
Fix: Bug fix (e.g., "Fix: Dice validation for negative modifiers")
Update: Improvements (e.g., "Update: Character schema with deity field")
Docs: Documentation (e.g., "Docs: Add API examples to README")
Style: Code style (e.g., "Style: Format with black")
Test: Tests (e.g., "Test: Add initiative tracker tests")
```

### Pull Request Template
```markdown
## What does this PR do?
Brief description of the feature/fix

## Changes Made
- Added X
- Modified Y
- Fixed Z

## Testing
- [ ] Tested locally
- [ ] Backend: API docs work
- [ ] Frontend: UI displays correctly
- [ ] No console errors

## Screenshots (if UI changes)
[Add screenshots here]

## Notes for Reviewer
Any special considerations or questions
```

---

## 🎯 Success Metrics

### Week 1
- ✅ Both developers can run the full stack locally
- ✅ Both have made at least one commit
- ✅ One PR merged per person

### Week 2
- ✅ Initiative tracker working in API
- ✅ Character sheet displaying in UI
- ✅ Characters can be created from frontend
- ✅ At least 5 PRs merged total

---

## 💡 Tips for Success

**For Both:**
1. **Commit early, commit often** - Small commits are easier to review
2. **Test before pushing** - Make sure it works on your machine
3. **Read each other's code** - Learn from each other's approaches
4. **Ask questions** - There are no dumb questions
5. **Have fun!** - This is a game helper, it should be enjoyable to build

**For StrayDogSyn (Backend):**
- Use the `/docs` endpoint constantly - it's your best friend
- Test with curl or Postman if frontend isn't ready yet
- Write at least basic tests for new features
- Think about error cases (what if user sends bad data?)

**For GrumbleBee (Frontend):**
- Use browser DevTools Network tab to debug API calls
- Start with hardcoded data, then connect to real API
- Make it work first, make it pretty second
- Don't worry about perfect styling initially

---

## 🆘 When Stuck

**Backend Issues:**
- Check terminal 1 for Python errors
- Review FastAPI docs: https://fastapi.tiangolo.com
- Test endpoint in `/docs` before blaming frontend
- Use `print()` statements liberally for debugging

**Frontend Issues:**
- Check browser console for JavaScript errors
- Use React DevTools to inspect component state
- Verify API is running (visit http://localhost:8000)
- Check Network tab to see actual API responses

**Git Issues:**
- Google the exact error message first
- Ask before force-pushing anything
- When in doubt, create a new branch

---

## 🎉 Quick Wins (Easy Tasks)

If you finish early or want something simple:

**Backend:**
- [ ] Add more monsters to encounter_generator.py
- [ ] Add a "roll stats" endpoint (4d6 drop lowest, six times)
- [ ] Add endpoint to get character by name (not just ID)
- [ ] Add validation: HP current can't exceed HP max

**Frontend:**
- [ ] Add dark mode toggle
- [ ] Add sound effects on dice rolls (optional!)
- [ ] Add "Roll for stats" button in character creation
- [ ] Add footer with project name and version

---

## Next Month Preview

After Week 2, possible next features:

1. **Combat Tracker** (integrate Initiative + Character HP)
2. **Spell Database** (backend) + Spell Search (frontend)
3. **PDF Parser** to import monsters from your books
4. **Campaign Manager** to track multiple sessions
5. **Party View** to see all characters at once

---

**Remember:** The goal isn't perfection, it's progress. Every commit makes the project better!

Ready to roll for initiative? 🎲
