from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import random
from typing import List
from contextlib import asynccontextmanager

from database import get_db, init_db, Character, Monster
from schemas import (
    CharacterCreate,
    CharacterResponse,
    DiceRollRequest,
    DiceRollResponse,
    EncounterRequest,
    EncounterResponse,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    # Seed some sample monsters
    db = next(get_db())
    if db.query(Monster).count() == 0:
        sample_monsters = [
            Monster(name="Goblin", cr=0.25, type="humanoid", hit_points=6, armor_class=15),
            Monster(name="Orc", cr=0.5, type="humanoid", hit_points=15, armor_class=13),
            Monster(name="Bugbear", cr=1, type="humanoid", hit_points=27, armor_class=16),
            Monster(name="Ogre", cr=2, type="giant", hit_points=59, armor_class=11),
            Monster(name="Troll", cr=5, type="giant", hit_points=84, armor_class=15),
            Monster(name="Young Dragon", cr=7, type="dragon", hit_points=136, armor_class=18),
            Monster(name="Stone Giant", cr=8, type="giant", hit_points=126, armor_class=17),
            Monster(name="Adult Dragon", cr=13, type="dragon", hit_points=225, armor_class=19),
        ]
        for monster in sample_monsters:
            db.add(monster)
        db.commit()
    db.close()
    yield
    # Shutdown (cleanup if needed)


app = FastAPI(title="Pathfinder TTRPG Companion", lifespan=lifespan)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Character endpoints
@app.post("/api/characters/", response_model=CharacterResponse)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    db_character = Character(**character.model_dump())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


@app.get("/api/characters/", response_model=List[CharacterResponse])
def get_characters(db: Session = Depends(get_db)):
    return db.query(Character).all()


@app.get("/api/characters/{character_id}", response_model=CharacterResponse)
def get_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@app.put("/api/characters/{character_id}", response_model=CharacterResponse)
def update_character(
    character_id: int, character: CharacterCreate, db: Session = Depends(get_db)
):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    for key, value in character.model_dump().items():
        setattr(db_character, key, value)
    db.commit()
    db.refresh(db_character)
    return db_character


@app.delete("/api/characters/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    db.delete(character)
    db.commit()
    return {"message": "Character deleted"}


# Dice roller endpoint
@app.post("/api/dice/roll", response_model=DiceRollResponse)
def roll_dice(roll_request: DiceRollRequest):
    valid_dice = [4, 6, 8, 10, 12, 20, 100]
    if roll_request.dice_type not in valid_dice:
        raise HTTPException(status_code=400, detail="Invalid dice type")
    
    if roll_request.num_dice < 1 or roll_request.num_dice > 100:
        raise HTTPException(status_code=400, detail="Number of dice must be between 1 and 100")
    
    rolls = [random.randint(1, roll_request.dice_type) for _ in range(roll_request.num_dice)]
    total = sum(rolls)
    result = total + roll_request.modifier
    
    return DiceRollResponse(
        rolls=rolls,
        total=total,
        modifier=roll_request.modifier,
        result=result
    )


# Encounter generator endpoint
@app.post("/api/encounters/generate", response_model=EncounterResponse)
def generate_encounter(encounter_request: EncounterRequest, db: Session = Depends(get_db)):
    # Calculate target CR based on party level and difficulty
    difficulty_multipliers = {
        "easy": 0.5,
        "medium": 1.0,
        "hard": 1.5,
        "deadly": 2.0
    }
    
    multiplier = difficulty_multipliers.get(encounter_request.difficulty, 1.0)
    target_cr = encounter_request.party_level * multiplier
    
    # Get all monsters from database
    all_monsters = db.query(Monster).all()
    if not all_monsters:
        raise HTTPException(status_code=404, detail="No monsters in database")
    
    # Simple encounter generation: try to match target CR
    selected_monsters = []
    current_cr = 0.0
    max_attempts = 50
    
    for _ in range(max_attempts):
        if current_cr >= target_cr * 0.8:  # Within 80% of target
            break
        
        # Filter monsters that won't exceed target by too much
        suitable_monsters = [m for m in all_monsters if current_cr + m.cr <= target_cr * 1.3]
        
        if not suitable_monsters:
            break
        
        monster = random.choice(suitable_monsters)
        selected_monsters.append({
            "id": monster.id,
            "name": monster.name,
            "cr": monster.cr,
            "type": monster.type,
            "hit_points": monster.hit_points,
            "armor_class": monster.armor_class
        })
        current_cr += monster.cr
    
    if not selected_monsters:
        # Fallback: select one monster close to target CR
        monster = min(all_monsters, key=lambda m: abs(m.cr - target_cr))
        selected_monsters.append({
            "id": monster.id,
            "name": monster.name,
            "cr": monster.cr,
            "type": monster.type,
            "hit_points": monster.hit_points,
            "armor_class": monster.armor_class
        })
        current_cr = monster.cr
    
    return EncounterResponse(
        target_cr=target_cr,
        monsters=selected_monsters,
        total_cr=current_cr
    )


@app.get("/")
def root():
    return {"message": "Pathfinder TTRPG Companion API"}
