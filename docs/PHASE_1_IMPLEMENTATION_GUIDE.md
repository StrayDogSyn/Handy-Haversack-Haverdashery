# 🛠️ Phase 1 Implementation Guide
## Priority Features - Technical Deep Dive

This guide provides step-by-step implementation details for Phase 1 features. Think of it as the strategy guide that comes with the game - specific tactics, not just the rules.

---

## Feature 1: Advanced Dice Mechanics 🎲

**Complexity:** ●●○ (Medium)  
**Time Estimate:** 3-5 days  
**Owner:** StrayDogSyn (Backend) + GrumbleBee (Frontend polish)

### Current State
You already have:
- ✅ Basic polyhedral dice (d4, d6, d8, d10, d12, d20, d100)
- ✅ Modifier support (e.g., "2d6+3")
- ✅ Roll history
- ✅ Advantage/disadvantage for d20

### What's Missing (Priority Order)

#### 1. D3 Support (Easy Win - 1 day)

**Why it matters:** Common in Pathfinder for small weapons, some spells, etc.

**Backend Implementation:**
```python
# backend/app/services/dice_service.py

def roll_dice(dice_type: int, count: int = 1) -> List[int]:
    """Roll any polyhedral dice, including d3"""
    if dice_type == 3:
        # D3 is special - roll 1d6 and divide by 2, round up
        # Results: 1-2 → 1, 3-4 → 2, 5-6 → 3
        rolls = [random.randint(1, 6) for _ in range(count)]
        return [(r + 1) // 2 for r in rolls]
    
    return [random.randint(1, dice_type) for _ in range(count)]
```

**Why this approach?**
D3s don't physically exist (well, they do, but they're weird). The standard method is rolling a d6 and doing math. This mimics real-world tabletop behavior.

**Frontend Update:**
```typescript
// frontend/src/components/DiceRoller.tsx

const diceTypes = [3, 4, 6, 8, 10, 12, 20, 100]; // Add d3!

<button
  onClick={() => rollDice(3, 1)}
  className="dice-button bg-purple-600 hover:bg-purple-700"
>
  <span className="text-2xl">🎲</span>
  <span className="text-sm">d3</span>
</button>
```

**Test Cases:**
```python
# backend/tests/test_dice.py

def test_d3_distribution():
    """Ensure d3 produces 1, 2, 3 equally over many rolls"""
    results = [roll_dice(3, 1)[0] for _ in range(3000)]
    
    # Each value should appear ~1000 times (±10%)
    assert 900 <= results.count(1) <= 1100
    assert 900 <= results.count(2) <= 1100
    assert 900 <= results.count(3) <= 1100
    assert min(results) == 1
    assert max(results) == 3
```

---

#### 2. Critical Hit/Fumble Detection (Medium - 2 days)

**What it does:** Automatically detect natural 20s (crits) and natural 1s (fumbles) for d20 rolls.

**Backend Implementation:**
```python
# backend/app/models/dice.py

from pydantic import BaseModel
from typing import Optional

class RollResult(BaseModel):
    dice_type: int
    rolls: List[int]
    modifier: int
    total: int
    is_critical: bool = False
    is_fumble: bool = False
    degree_of_success: Optional[str] = None  # For PF2e

def roll_with_analysis(
    dice_expr: str,
    target_dc: Optional[int] = None
) -> RollResult:
    """
    Roll dice and analyze for crits/fumbles.
    
    Examples:
        "1d20+5" with DC 15 → degree of success calculation
        "1d20+0" → just crit/fumble detection
    """
    # Parse expression (you already have this)
    dice_type, count, modifier = parse_dice_expression(dice_expr)
    
    # Roll the dice
    rolls = roll_dice(dice_type, count)
    total = sum(rolls) + modifier
    
    result = RollResult(
        dice_type=dice_type,
        rolls=rolls,
        modifier=modifier,
        total=total
    )
    
    # Crit/fumble only applies to d20
    if dice_type == 20 and count == 1:
        natural_roll = rolls[0]
        
        if natural_roll == 20:
            result.is_critical = True
        elif natural_roll == 1:
            result.is_fumble = True
        
        # PF2e degree of success (if DC provided)
        if target_dc is not None:
            result.degree_of_success = calculate_degree_of_success(
                total, target_dc, natural_roll
            )
    
    return result
```

**Pathfinder 2e Degree of Success:**
```python
def calculate_degree_of_success(
    total: int,
    dc: int,
    natural_roll: int
) -> str:
    """
    PF2e has 4 outcomes: Critical Success, Success, Failure, Critical Failure
    
    Rules:
    - Beat DC by 10+ OR natural 20: Critical Success
    - Beat DC by 1-9: Success  
    - Miss DC by 1-9: Failure
    - Miss DC by 10+ OR natural 1: Critical Failure
    
    Special: Natural 20 upgrades one degree (Failure → Success)
    Special: Natural 1 downgrades one degree (Success → Failure)
    """
    difference = total - dc
    
    # Start with base outcome
    if difference >= 10:
        outcome = "critical_success"
    elif difference >= 0:
        outcome = "success"
    elif difference >= -9:
        outcome = "failure"
    else:
        outcome = "critical_failure"
    
    # Apply natural 20/1 adjustments
    if natural_roll == 20:
        if outcome == "failure":
            outcome = "success"
        elif outcome == "success":
            outcome = "critical_success"
    elif natural_roll == 1:
        if outcome == "success":
            outcome = "failure"
        elif outcome == "failure":
            outcome = "critical_failure"
    
    return outcome
```

**Frontend Display:**
```typescript
// Show visual flair for crits/fumbles

interface RollResultProps {
  result: RollResult;
}

export const RollResultDisplay: React.FC<RollResultProps> = ({ result }) => {
  const getCriticalityStyle = () => {
    if (result.is_critical) {
      return "border-4 border-green-500 animate-pulse bg-green-900";
    }
    if (result.is_fumble) {
      return "border-4 border-red-500 animate-pulse bg-red-900";
    }
    return "border border-gray-600";
  };

  const getDegreeEmoji = (degree: string) => {
    switch (degree) {
      case "critical_success": return "🎉";
      case "success": return "✅";
      case "failure": return "❌";
      case "critical_failure": return "💀";
      default: return "";
    }
  };

  return (
    <div className={`p-4 rounded-lg ${getCriticalityStyle()}`}>
      <div className="flex justify-between items-center">
        <div className="text-4xl font-bold">
          {result.total}
          {result.is_critical && " 🎉"}
          {result.is_fumble && " 💀"}
        </div>
        
        {result.degree_of_success && (
          <div className="text-2xl">
            {getDegreeEmoji(result.degree_of_success)}
            <span className="text-sm ml-2">
              {result.degree_of_success.replace("_", " ").toUpperCase()}
            </span>
          </div>
        )}
      </div>
      
      <div className="text-sm text-gray-400 mt-2">
        Rolled: {result.rolls.join(", ")}
        {result.modifier !== 0 && ` + ${result.modifier}`}
      </div>
    </div>
  );
};
```

---

#### 3. Roll Macros System (Medium - 2 days)

**What it is:** Save common rolls as shortcuts (e.g., "Longsword Attack" = 1d20+7, "Fireball Damage" = 8d6)

**Backend:**
```python
# backend/app/models/macro.py

class RollMacro(Base):
    __tablename__ = "roll_macros"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # Future: multi-user
    name = Column(String(100))  # "Longsword Attack"
    dice_expression = Column(String(50))  # "1d20+7"
    description = Column(String(255))  # "Melee attack vs AC"
    target_dc = Column(Integer, nullable=True)  # Optional DC
    created_at = Column(DateTime, default=datetime.utcnow)

# backend/app/api/dice.py

@router.post("/macros", response_model=RollMacro)
async def create_macro(
    macro: RollMacroCreate,
    db: Session = Depends(get_db)
):
    """Save a new roll macro"""
    db_macro = RollMacro(**macro.dict())
    db.add(db_macro)
    db.commit()
    return db_macro

@router.post("/macros/{macro_id}/execute")
async def execute_macro(
    macro_id: int,
    db: Session = Depends(get_db)
):
    """Roll a saved macro"""
    macro = db.query(RollMacro).filter(RollMacro.id == macro_id).first()
    if not macro:
        raise HTTPException(status_code=404, detail="Macro not found")
    
    result = roll_with_analysis(macro.dice_expression, macro.target_dc)
    return result
```

**Frontend - Macro UI:**
```typescript
// Quick access macro buttons

export const MacroBar: React.FC = () => {
  const [macros, setMacros] = useState<Macro[]>([]);
  
  useEffect(() => {
    // Load user's macros
    fetch("/api/dice/macros")
      .then(res => res.json())
      .then(setMacros);
  }, []);

  const executeMacro = async (macroId: number) => {
    const response = await fetch(`/api/dice/macros/${macroId}/execute`, {
      method: "POST"
    });
    const result = await response.json();
    // Display result...
  };

  return (
    <div className="macro-bar flex gap-2 overflow-x-auto p-4">
      {macros.map(macro => (
        <button
          key={macro.id}
          onClick={() => executeMacro(macro.id)}
          className="macro-button px-4 py-2 bg-purple-700 hover:bg-purple-600 
                     rounded-lg whitespace-nowrap"
          title={macro.description}
        >
          🎲 {macro.name}
        </button>
      ))}
      
      <button
        onClick={() => setShowMacroEditor(true)}
        className="px-4 py-2 bg-gray-700 hover:bg-gray-600 rounded-lg"
      >
        + New Macro
      </button>
    </div>
  );
};
```

---

## Feature 2: Interactive Character Sheet 📋

**Complexity:** ●●● (High)  
**Time Estimate:** 1-2 weeks  
**Owner:** GrumbleBee (Frontend) + StrayDogSyn (Backend API)

This is the big one. The character sheet is the **core** of any TTRPG app.

### Data Model (Backend First!)

```python
# backend/app/models/character.py

class Character(Base):
    __tablename__ = "characters"
    
    # Basic Info
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    ancestry = Column(String(50))  # Human, Elf, etc.
    heritage = Column(String(50))  # Half-elf, etc.
    background = Column(String(50))
    character_class = Column(String(50))
    level = Column(Integer, default=1)
    
    # Ability Scores
    strength = Column(Integer, default=10)
    dexterity = Column(Integer, default=10)
    constitution = Column(Integer, default=10)
    intelligence = Column(Integer, default=10)
    wisdom = Column(Integer, default=10)
    charisma = Column(Integer, default=10)
    
    # Combat Stats
    max_hp = Column(Integer)
    current_hp = Column(Integer)
    temp_hp = Column(Integer, default=0)
    armor_class = Column(Integer, default=10)
    
    # Derived Stats (calculated, not stored)
    @property
    def str_modifier(self) -> int:
        return (self.strength - 10) // 2
    
    @property
    def dex_modifier(self) -> int:
        return (self.dexterity - 10) // 2
    
    # ... etc for all abilities
    
    # Complex Data (JSON)
    skills = Column(JSON)  # {"acrobatics": {"trained": true, "bonus": 5}}
    feats = Column(JSON)  # [{"name": "Power Attack", "level": 1}]
    inventory = Column(JSON)  # [{"name": "Longsword", "quantity": 1}]
    spells = Column(JSON)  # Spell slots, prepared spells, etc.
```

### Frontend Component Architecture

```
CharacterSheet/ (main component)
├── CharacterHeader.tsx (name, level, class, portrait)
├── AbilityScores.tsx (the six main stats)
├── CombatStats.tsx (HP, AC, saves, initiative)
├── SkillsPanel.tsx (all skills with checkboxes)
├── FeatsPanel.tsx (feat list with descriptions)
├── InventoryPanel.tsx (items, weight, currency)
├── SpellsPanel.tsx (spell slots, prepared spells)
└── NotesPanel.tsx (free-form character notes)
```

### Key Frontend Challenge: Live Calculations

Everything in PF2e is interconnected. When you change your DEX score, it affects:
- Reflex saves
- AC (if wearing light armor)
- Stealth, Acrobatics, Thievery skills
- Initiative
- Ranged attack rolls

**Solution: Centralized calculation hook**

```typescript
// frontend/src/hooks/useCharacterCalculations.ts

export const useCharacterCalculations = (character: Character) => {
  // Memoize expensive calculations
  const abilityModifiers = useMemo(() => ({
    str: Math.floor((character.strength - 10) / 2),
    dex: Math.floor((character.dexterity - 10) / 2),
    con: Math.floor((character.constitution - 10) / 2),
    int: Math.floor((character.intelligence - 10) / 2),
    wis: Math.floor((character.wisdom - 10) / 2),
    cha: Math.floor((character.charisma - 10) / 2),
  }), [character.strength, character.dexterity, /* ... */]);

  const saves = useMemo(() => ({
    fortitude: abilityModifiers.con + (character.level * 2), // Simplified
    reflex: abilityModifiers.dex + (character.level * 2),
    will: abilityModifiers.wis + (character.level * 2),
  }), [abilityModifiers, character.level]);

  const armorClass = useMemo(() => {
    // Base AC + DEX + armor bonus + misc
    return 10 + abilityModifiers.dex + (character.armor_bonus || 0);
  }, [abilityModifiers.dex, character.armor_bonus]);

  const initiative = abilityModifiers.dex;

  return {
    abilityModifiers,
    saves,
    armorClass,
    initiative,
  };
};
```

### AbilityScores Component Example

```typescript
interface AbilityScoresProps {
  character: Character;
  onUpdate: (updates: Partial<Character>) => void;
  readOnly?: boolean;
}

export const AbilityScores: React.FC<AbilityScoresProps> = ({
  character,
  onUpdate,
  readOnly = false
}) => {
  const { abilityModifiers } = useCharacterCalculations(character);

  const abilities = [
    { key: 'strength', label: 'STR', value: character.strength },
    { key: 'dexterity', label: 'DEX', value: character.dexterity },
    { key: 'constitution', label: 'CON', value: character.constitution },
    { key: 'intelligence', label: 'INT', value: character.intelligence },
    { key: 'wisdom', label: 'WIS', value: character.wisdom },
    { key: 'charisma', label: 'CHA', value: character.charisma },
  ];

  return (
    <div className="grid grid-cols-3 gap-4">
      {abilities.map(ability => (
        <div key={ability.key} className="ability-score-card">
          <label className="text-sm text-gray-400">{ability.label}</label>
          
          {readOnly ? (
            <div className="text-3xl font-bold">{ability.value}</div>
          ) : (
            <input
              type="number"
              value={ability.value}
              onChange={(e) => onUpdate({ [ability.key]: parseInt(e.target.value) })}
              className="w-full text-3xl font-bold bg-gray-800 rounded p-2"
              min={1}
              max={30}
            />
          )}
          
          <div className="text-xl text-amber-500">
            {abilityModifiers[ability.key.slice(0, 3)] >= 0 ? '+' : ''}
            {abilityModifiers[ability.key.slice(0, 3)]}
          </div>
        </div>
      ))}
    </div>
  );
};
```

### Testing Strategy

```typescript
// Character sheet is complex, so unit test the calculations

describe('useCharacterCalculations', () => {
  it('calculates ability modifiers correctly', () => {
    const char = { strength: 18, dexterity: 14, /* ... */ };
    const { abilityModifiers } = useCharacterCalculations(char);
    
    expect(abilityModifiers.str).toBe(4);  // (18-10)/2 = 4
    expect(abilityModifiers.dex).toBe(2);  // (14-10)/2 = 2
  });

  it('updates AC when DEX changes', () => {
    const char1 = { dexterity: 14, armor_bonus: 2 };
    const calc1 = useCharacterCalculations(char1);
    expect(calc1.armorClass).toBe(14);  // 10 + 2 + 2

    const char2 = { dexterity: 16, armor_bonus: 2 };
    const calc2 = useCharacterCalculations(char2);
    expect(calc2.armorClass).toBe(15);  // 10 + 3 + 2
  });
});
```

---

## Feature 3: Initiative Tracker ⚔️

**Complexity:** ●●○ (Medium)  
**Time Estimate:** 3-5 days  
**Owner:** Both (Pair Programming Recommended)

Initiative tracking is where backend and frontend dance together.

### Data Model

```python
# backend/app/models/combat.py

class Combat(Base):
    """A single combat encounter instance"""
    __tablename__ = "combats"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))  # "Goblin Ambush"
    current_round = Column(Integer, default=1)
    current_turn = Column(Integer, default=0)  # Index in turn_order
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Combatant(Base):
    """A participant in combat (PC or NPC)"""
    __tablename__ = "combatants"
    
    id = Column(Integer, primary_key=True)
    combat_id = Column(Integer, ForeignKey("combats.id"))
    
    name = Column(String(100))
    initiative = Column(Integer)
    current_hp = Column(Integer)
    max_hp = Column(Integer)
    armor_class = Column(Integer)
    
    # Conditions (e.g., "Stunned 1", "Frightened 2")
    conditions = Column(JSON)  # [{"name": "Frightened", "value": 2}]
    
    # Is this a PC or NPC?
    is_player = Column(Boolean, default=False)
    
    # If PC, link to character
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
```

### API Endpoints

```python
# backend/app/api/combat.py

@router.post("/combat/start")
async def start_combat(
    participants: List[CombatantCreate],
    db: Session = Depends(get_db)
):
    """
    Start a new combat encounter.
    Rolls initiative for all participants.
    """
    combat = Combat(name=f"Combat {datetime.now()}")
    db.add(combat)
    db.flush()
    
    combatants = []
    for p in participants:
        initiative_roll = roll_dice(20, 1)[0] + p.initiative_modifier
        
        combatant = Combatant(
            combat_id=combat.id,
            name=p.name,
            initiative=initiative_roll,
            current_hp=p.max_hp,
            max_hp=p.max_hp,
            armor_class=p.armor_class,
            is_player=p.is_player
        )
        combatants.append(combatant)
        db.add(combatant)
    
    # Sort by initiative (descending)
    combatants.sort(key=lambda c: c.initiative, reverse=True)
    
    db.commit()
    return {"combat": combat, "turn_order": combatants}

@router.post("/combat/{combat_id}/next-turn")
async def advance_turn(
    combat_id: int,
    db: Session = Depends(get_db)
):
    """Move to the next combatant's turn"""
    combat = db.query(Combat).filter(Combat.id == combat_id).first()
    combatants = db.query(Combatant).filter(
        Combatant.combat_id == combat_id
    ).order_by(Combatant.initiative.desc()).all()
    
    combat.current_turn += 1
    
    # If we've gone through everyone, start a new round
    if combat.current_turn >= len(combatants):
        combat.current_turn = 0
        combat.current_round += 1
        
        # Decrement condition values
        for c in combatants:
            for condition in c.conditions:
                if condition.get("value", 0) > 0:
                    condition["value"] -= 1
    
    db.commit()
    
    current_combatant = combatants[combat.current_turn]
    return {
        "current_round": combat.current_round,
        "current_combatant": current_combatant
    }
```

### Frontend - Initiative Tracker UI

```typescript
export const InitiativeTracker: React.FC = () => {
  const [combat, setCombat] = useState<Combat | null>(null);
  const [combatants, setCombatants] = useState<Combatant[]>([]);

  const startCombat = async (participants: CombatantInput[]) => {
    const response = await fetch("/api/combat/start", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ participants })
    });
    const data = await response.json();
    setCombat(data.combat);
    setCombatants(data.turn_order);
  };

  const nextTurn = async () => {
    const response = await fetch(`/api/combat/${combat.id}/next-turn`, {
      method: "POST"
    });
    const data = await response.json();
    setCombat(prev => ({
      ...prev,
      current_round: data.current_round,
      current_turn: data.current_combatant.initiative
    }));
  };

  return (
    <div className="initiative-tracker bg-gray-800 rounded-lg p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold">
          Round {combat?.current_round || 0}
        </h2>
        <button
          onClick={nextTurn}
          className="px-4 py-2 bg-green-600 hover:bg-green-700 rounded"
        >
          Next Turn ▶
        </button>
      </div>

      <div className="space-y-2">
        {combatants.map((combatant, index) => (
          <div
            key={combatant.id}
            className={`
              p-4 rounded flex items-center justify-between
              ${index === combat?.current_turn 
                ? 'bg-amber-600 border-2 border-amber-400' 
                : 'bg-gray-700'}
            `}
          >
            <div className="flex items-center gap-4">
              <div className="text-2xl font-bold w-12 text-center">
                {combatant.initiative}
              </div>
              
              <div>
                <div className="font-bold">{combatant.name}</div>
                <div className="text-sm text-gray-400">
                  HP: {combatant.current_hp}/{combatant.max_hp}
                </div>
              </div>
            </div>

            <div className="flex gap-2">
              {combatant.conditions?.map(cond => (
                <span key={cond.name} className="px-2 py-1 bg-red-600 rounded text-xs">
                  {cond.name} {cond.value}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
```

---

## Testing Your Implementation

### Unit Tests (Backend)
```bash
cd backend
pytest tests/test_dice.py -v
pytest tests/test_combat.py -v
```

### Integration Tests (Full Stack)
```bash
# Start backend
cd backend && uvicorn app.main:app --reload

# Start frontend
cd frontend && npm start

# Manual testing checklist:
# [ ] Roll d3 - should only show 1, 2, or 3
# [ ] Roll 1d20 - check for crit/fumble highlighting
# [ ] Create macro - should save and be reusable
# [ ] Create character - all stats calculate correctly
# [ ] Start combat - initiative order is correct
# [ ] Advance turns - round counter increments
```

---

## Common Pitfalls & Solutions

### Pitfall 1: "It works on my machine"
**Problem:** Hardcoded localhost URLs  
**Solution:** Environment variables

```typescript
// frontend/.env.development
REACT_APP_API_URL=http://localhost:8000

// frontend/.env.production
REACT_APP_API_URL=https://api.yourdomain.com

// Use it:
const API_URL = process.env.REACT_APP_API_URL;
```

### Pitfall 2: Race conditions in combat turns
**Problem:** Two users click "Next Turn" simultaneously  
**Solution:** Optimistic locking

```python
class Combat(Base):
    version = Column(Integer, default=0)  # Add this

@router.post("/combat/{combat_id}/next-turn")
async def advance_turn(combat_id: int, expected_version: int, db: Session):
    combat = db.query(Combat).filter(
        Combat.id == combat_id,
        Combat.version == expected_version  # Check version!
    ).first()
    
    if not combat:
        raise HTTPException(409, "Combat state changed, please refresh")
    
    combat.version += 1  # Increment version
    # ... rest of logic
```

### Pitfall 3: Character sheet state getting out of sync
**Problem:** Local state doesn't match database  
**Solution:** Single source of truth pattern

```typescript
// Use React Query or SWR for server state management
import { useQuery, useMutation, useQueryClient } from 'react-query';

const useCharacter = (characterId: number) => {
  const queryClient = useQueryClient();

  const { data: character } = useQuery(
    ['character', characterId],
    () => fetch(`/api/characters/${characterId}`).then(r => r.json())
  );

  const updateCharacter = useMutation(
    (updates) => fetch(`/api/characters/${characterId}`, {
      method: 'PUT',
      body: JSON.stringify(updates)
    }),
    {
      onSuccess: () => {
        // Invalidate and refetch
        queryClient.invalidateQueries(['character', characterId]);
      }
    }
  );

  return { character, updateCharacter };
};
```

---

## Next Steps After Phase 1

Once these features are solid, you're ready for Phase 2: API integrations.

**Celebration checklist:**
- [ ] Can roll all dice types including d3
- [ ] Crits and fumbles are visually obvious
- [ ] Character sheet calculates modifiers automatically
- [ ] Initiative tracker manages turn order
- [ ] All tests pass
- [ ] Deployed to staging environment
- [ ] James approves of UI/UX

**Then:** Start researching Archives of Nethys API and plan your integration strategy!

---

*May your builds be bug-free and your deployments successful!* 🎲
