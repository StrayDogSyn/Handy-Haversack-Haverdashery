# 📋 Initial Tasks

Task breakdown for both developers to get started with the Handy Haversack Haverdashery project.

---

## 🎯 Task Overview

### For Backend Developer (You)
**Focus:** API development, database, business logic
**Location:** `backend/` directory
**Estimated Time:** 2-4 weeks for Phase 1

### For Frontend Developer (James)
**Focus:** UI components, user experience, styling
**Location:** `frontend/` directory
**Estimated Time:** 2-4 weeks for Phase 1

---

## 🔴 Priority Levels

- **P0 - Critical:** Must be done first
- **P1 - High:** Core features
- **P2 - Medium:** Important but can wait
- **P3 - Low:** Nice to have

---

## 🐍 Backend Tasks (for you)

### Phase 1: MVP Foundation (Weeks 1-2)

#### P0 - Critical Setup ✅ COMPLETE
- [x] Set up FastAPI project structure
- [x] Configure SQLite database
- [x] Create character model
- [x] Implement dice rolling service
- [x] Add basic API endpoints
- [x] Set up CORS

#### P1 - Core Features

**Task 1.1: Initiative Tracker Backend** (4-6 hours)
```
📝 Description:
Create backend API for initiative tracking in combat encounters.

📁 Files to Create:
- backend/app/models/initiative.py
- backend/app/api/initiative.py
- backend/app/services/initiative_service.py

✅ Acceptance Criteria:
- Can add combatants with initiative values
- Can sort by initiative order
- Can track current turn
- Can update HP during combat
- Can remove defeated combatants
- API endpoints: POST /initiative, GET /initiative/{encounter_id},
  PUT /initiative/{id}, DELETE /initiative/{id}

📚 Resources:
- See existing character.py for model example
- Use SQLAlchemy relationships for encounter linkage

🔗 Depends On: None (can start immediately)
```

**Task 1.2: Spell Database Schema** (3-4 hours)
```
📝 Description:
Create database model and API for storing Pathfinder 2e spells.

📁 Files to Create:
- backend/app/models/spell.py
- backend/app/api/spells.py

✅ Acceptance Criteria:
- Spell model with: name, level, school, casting_time, range,
  duration, components, description
- CRUD endpoints for spells
- Search/filter by level, school, class
- Seed database with 10-20 common spells

📚 Resources:
- Spell data: https://2e.aonprd.com/Spells.aspx
- Use JSON field for complex data (components, heightening)

🔗 Depends On: None (can start immediately)
```

**Task 1.3: Character Damage/Healing API** (2-3 hours) ✅ COMPLETE
- [x] POST /characters/{id}/damage endpoint
- [x] POST /characters/{id}/heal endpoint
- [x] Validate HP doesn't go below 0 or above max
- [x] Add tests for edge cases

**Task 1.4: Encounter Storage** (3-4 hours)
```
📝 Description:
Save generated encounters to database for later reference.

📁 Files to Edit:
- backend/app/models/encounter.py (create)
- backend/app/api/encounters.py (update)

✅ Acceptance Criteria:
- Encounters saved to database with timestamp
- Can retrieve past encounters
- Can delete old encounters
- Link encounters to characters (party composition)

🔗 Depends On: None (can start immediately)
```

#### P2 - Enhancements

**Task 2.1: Ability Score Calculator** (2-3 hours)
```
📝 Description:
Add helper functions for calculating ability modifiers,
saving throws, skill bonuses, etc.

📁 Files to Create:
- backend/app/services/calculator_service.py
- backend/tests/test_calculator.py

✅ Acceptance Criteria:
- Calculate ability modifiers from scores
- Calculate saving throw bonuses
- Calculate skill check bonuses
- Calculate attack bonuses
- Comprehensive test coverage

🔗 Depends On: None (can start immediately)
```

**Task 2.2: Bulk Operations API** (2 hours)
```
📝 Description:
Add endpoints for bulk operations on characters and encounters.

✅ Acceptance Criteria:
- POST /characters/bulk (create multiple)
- DELETE /characters/bulk (delete multiple)
- GET /characters with pagination
- GET /encounters with filtering

🔗 Depends On: None (can start immediately)
```

**Task 2.3: Dice Statistics** (2-3 hours)
```
📝 Description:
Add statistical analysis for dice rolls.

📁 Files to Edit:
- backend/app/services/dice_service.py
- backend/app/api/dice.py

✅ Acceptance Criteria:
- Average roll value for notation
- Probability distributions
- Success rate for DC checks
- Roll history analytics

🔗 Depends On: Dice service already exists
```

#### P3 - Advanced Features

**Task 3.1: PDF Text Extraction** (6-8 hours)
```
📝 Description:
Extract text from Pathfinder PDF rulebooks for spell/monster data.

📁 Files to Create:
- backend/app/services/pdf_service.py
- backend/tests/test_pdf.py

✅ Acceptance Criteria:
- Upload PDF endpoint
- Extract text from PDF
- Parse spell data from extracted text
- Parse monster data from extracted text
- Store in database

📦 New Dependencies:
- pypdf2 or pdfplumber

🔗 Depends On: Spell model (Task 1.2)
⚠️ Note: This is complex, start with simple text extraction first
```

**Task 3.2: Bestiary Expansion** (4-6 hours)
```
📝 Description:
Expand monster database from current 20 to 100+ creatures.

📁 Files to Edit:
- backend/app/services/bestiary.py

✅ Acceptance Criteria:
- Add 80+ more monsters
- Include all common monster types
- Add special abilities field
- Add lore/description field

📚 Resources:
- Monster data: https://2e.aonprd.com/Monsters.aspx

🔗 Depends On: None (can start immediately)
```

### Phase 2: Campaign Management (Weeks 3-4)

**Task 4.1: Campaign Model** (3-4 hours)
```
📝 Description:
Create database model for tracking campaigns and sessions.

📁 Files to Create:
- backend/app/models/campaign.py
- backend/app/api/campaigns.py

✅ Acceptance Criteria:
- Campaign model with: name, description, GM, start_date
- Session model with: date, notes, encounters, XP_gained
- Link characters to campaigns (party system)
- CRUD endpoints for campaigns

🔗 Depends On: None
```

**Task 4.2: XP and Leveling** (4-5 hours)
```
📝 Description:
Implement XP tracking and automatic character leveling.

📁 Files to Edit:
- backend/app/models/character.py
- backend/app/services/character_service.py

✅ Acceptance Criteria:
- Track XP on characters
- Calculate XP from encounters
- Automatic level-up when threshold reached
- Level-up notifications

🔗 Depends On: Campaign model (Task 4.1)
```

---

## ⚛️ Frontend Tasks (for James)

### Phase 1: MVP Foundation (Weeks 1-2)

#### P0 - Critical Setup

**Task F1.1: Project Setup** (1-2 hours)
```
📝 Description:
Set up React TypeScript project with routing and state management.

📁 Files to Create/Edit:
- frontend/src/App.tsx (update)
- frontend/src/router.tsx (create)
- frontend/src/types/index.ts (create)

✅ Acceptance Criteria:
- React Router configured
- Basic navigation between pages
- TypeScript types for API responses
- Axios API client configured

🔗 Depends On: None (can start immediately)
```

#### P1 - Core Features

**Task F1.2: Character Sheet Component** (8-10 hours)
```
📝 Description:
Create comprehensive character sheet UI for viewing and editing characters.

📁 Files to Create:
- frontend/src/components/CharacterSheet.tsx
- frontend/src/components/AbilityScores.tsx
- frontend/src/components/SkillsPanel.tsx
- frontend/src/components/CombatStats.tsx

✅ Acceptance Criteria:
- Display all character fields
- Edit mode with form validation
- Calculate and display ability modifiers
- Show skill bonuses
- Apply damage/healing with UI
- Responsive design for mobile

🎨 Design Notes:
- Use Pathfinder red/gold color scheme
- Card-based layout for stat blocks
- Tabs for different character sections

🔗 Depends On: Character API exists (backend Task 1.3)
```

**Task F1.3: Character List Page** (3-4 hours)
```
📝 Description:
Create page to view all characters with search and filter.

📁 Files to Create:
- frontend/src/pages/CharacterList.tsx
- frontend/src/components/CharacterCard.tsx

✅ Acceptance Criteria:
- Grid of character cards
- Search by name
- Filter by class, level, ancestry
- Click card to view full sheet
- Create new character button
- Delete character with confirmation

🔗 Depends On: Character Sheet (Task F1.2)
```

**Task F1.4: Initiative Tracker UI** (6-8 hours)
```
📝 Description:
Create interactive initiative tracker for combat encounters.

📁 Files to Create:
- frontend/src/components/InitiativeTracker.tsx
- frontend/src/components/InitiativeEntry.tsx

✅ Acceptance Criteria:
- Add combatants with initiative values
- Sort by initiative order automatically
- Highlight current turn
- Next turn button
- Apply damage to combatants
- Remove defeated combatants
- Round counter

🎨 Design Notes:
- Use list/table layout
- Color code players vs. monsters
- Large, clickable buttons for combat actions

🔗 Depends On: Initiative API (backend Task 1.1)
```

**Task F1.5: Encounter Builder UI** (5-6 hours)
```
📝 Description:
Create UI for building and generating encounters.

📁 Files to Create:
- frontend/src/components/EncounterBuilder.tsx
- frontend/src/components/MonsterSelector.tsx

✅ Acceptance Criteria:
- Select party size and level
- Choose difficulty (trivial/low/moderate/severe/extreme)
- Generate encounter button
- Display suggested monsters
- Add to initiative tracker button
- Save encounter

🔗 Depends On: Encounter API exists
```

#### P2 - Enhancements

**Task F2.1: Dice Roller Improvements** (3-4 hours)
```
📝 Description:
Enhance existing DiceRoller component with more features.

📁 Files to Edit:
- frontend/src/components/DiceRoller.tsx

✅ Acceptance Criteria:
- Quick roll buttons (d20, d6, etc.)
- Advantage/Disadvantage toggle for d20
- Save favorite rolls
- Roll statistics display
- Animation for rolls
- Sound effects (optional)

🔗 Depends On: None (can start immediately)
```

**Task F2.2: Spell Browser** (6-8 hours)
```
📝 Description:
Create searchable spell database browser.

📁 Files to Create:
- frontend/src/components/SpellBrowser.tsx
- frontend/src/components/SpellCard.tsx
- frontend/src/components/SpellDetail.tsx

✅ Acceptance Criteria:
- List all spells with pagination
- Search by name
- Filter by level, school, class
- View detailed spell info in modal
- Favorite spells
- Export spell list to PDF (bonus)

🔗 Depends On: Spell API (backend Task 1.2)
```

**Task F2.3: Responsive Design Polish** (4-5 hours)
```
📝 Description:
Ensure all components work well on mobile and tablet.

📁 Files to Edit:
- All component files
- frontend/tailwind.config.js

✅ Acceptance Criteria:
- Mobile-first design
- Touch-friendly buttons
- Collapsible panels on small screens
- Hamburger menu for navigation
- Test on multiple screen sizes

🔗 Depends On: All major components complete
```

#### P3 - Advanced Features

**Task F3.1: Campaign Dashboard** (8-10 hours)
```
📝 Description:
Create dashboard for managing campaigns and sessions.

📁 Files to Create:
- frontend/src/pages/CampaignDashboard.tsx
- frontend/src/components/SessionLog.tsx
- frontend/src/components/PartyOverview.tsx

✅ Acceptance Criteria:
- View campaign details
- Log session notes
- Track party members
- View session history
- XP tracking visualization

🔗 Depends On: Campaign API (backend Task 4.1)
```

**Task F3.2: Dark Mode** (2-3 hours)
```
📝 Description:
Add dark mode toggle for better readability at night.

📁 Files to Edit:
- frontend/src/App.tsx
- frontend/tailwind.config.js

✅ Acceptance Criteria:
- Toggle in header
- Persistent preference (localStorage)
- Dark color scheme for all components
- Good contrast ratios

🔗 Depends On: None (can start anytime)
```

**Task F3.3: Keyboard Shortcuts** (3-4 hours)
```
📝 Description:
Add keyboard shortcuts for power users.

✅ Acceptance Criteria:
- Press 'R' to quick roll d20
- Press 'N' to advance initiative
- Press '/' to focus search
- Press '?' to show help modal
- Visual indicator for shortcuts

🔗 Depends On: All major features complete
```

---

## 🤝 Collaboration Points

### Sync Required Between Devs

**Initiative Tracker:**
- Backend finishes Task 1.1 before frontend Task F1.4
- Agree on API contract first
- Test with mock data if backend not ready

**Spell System:**
- Backend Task 1.2 before frontend Task F2.2
- Share TypeScript types for spell object
- Backend can seed with sample data

**Character Sheet:**
- Already working! Frontend can start Task F1.2 immediately
- Backend Task 1.3 adds damage/healing (bonus feature)

### Communication Checkpoints

**Week 1:**
- Day 3: Sync on initiative tracker API design
- Day 5: Review character sheet progress

**Week 2:**
- Day 3: Test initiative tracker integration
- Day 5: Review spell system design

**Week 3:**
- Day 1: Sprint planning for Phase 2
- Day 5: Demo completed features

---

## 📊 Progress Tracking

### Backend Checklist
- [x] Dice rolling (complete)
- [x] Character CRUD (complete)
- [x] Encounter generation (complete)
- [ ] Initiative tracker API
- [ ] Spell database
- [ ] Damage/healing refinements
- [ ] Encounter storage
- [ ] Campaign system

### Frontend Checklist
- [x] DiceRoller component (complete)
- [ ] Character Sheet UI
- [ ] Character List page
- [ ] Initiative Tracker UI
- [ ] Encounter Builder UI
- [ ] Spell Browser
- [ ] Campaign Dashboard

---

## 🎯 Definition of Done

A task is "done" when:
- ✅ Code is written and works locally
- ✅ Tests are written and passing
- ✅ Code is committed to feature branch
- ✅ Pull request is created
- ✅ Code review is complete
- ✅ Merged to main branch
- ✅ Documented (if needed)

---

## 🚀 Getting Started

### For Backend Developer
1. Pick a P1 task (suggest Task 1.1: Initiative Tracker)
2. Create feature branch: `git checkout -b feature/initiative-tracker`
3. Create files as specified in task description
4. Follow acceptance criteria
5. Write tests
6. Commit and push
7. Create PR

### For Frontend Developer
1. Start with Task F1.2 (Character Sheet)
2. Can work in parallel with backend
3. Use existing Character API
4. Create feature branch
5. Build component with mock data first
6. Integrate with real API
7. Create PR

---

## 📞 Need Help?

**Backend Questions:**
- Check ARCHITECTURE.md for design patterns
- Look at existing api/characters.py for examples
- Check FastAPI docs: https://fastapi.tiangolo.com/

**Frontend Questions:**
- Check existing DiceRoller.tsx for component example
- Look at Tailwind docs: https://tailwindcss.com/docs
- Check React docs: https://react.dev/

**Git/Workflow Questions:**
- Check QUICK_REFERENCE.md for commands
- Ask teammate before making major changes

---

## 🎉 Let's Build!

You now have:
- ✅ Clear tasks to work on
- ✅ Acceptance criteria for each task
- ✅ Priority ordering
- ✅ Time estimates
- ✅ Dependencies mapped out

**Pick a task and start coding!** 🎲
