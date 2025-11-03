"""
Character management API endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.character import Character
from app.models.schemas import CharacterCreate, CharacterUpdate, CharacterResponse

router = APIRouter()


@router.get("/", response_model=List[CharacterResponse])
async def list_characters(db: Session = Depends(get_db)):
    """
    Get all characters.
    """
    characters = db.query(Character).all()
    return [char.to_dict() for char in characters]


@router.post("/", response_model=CharacterResponse, status_code=201)
async def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    """
    Create a new character.
    """
    db_character = Character(
        name=character.name,
        player_name=character.player_name,
        race=character.race,
        character_class=character.character_class,
        level=character.level,
        alignment=character.alignment,
        deity=character.deity,
        strength=character.strength,
        dexterity=character.dexterity,
        constitution=character.constitution,
        intelligence=character.intelligence,
        wisdom=character.wisdom,
        charisma=character.charisma,
        hit_points_max=character.hit_points_max,
        hit_points_current=character.hit_points_current,
        armor_class=character.armor_class,
        initiative=character.initiative,
        skills=character.skills,
        feats=character.feats,
        inventory=character.inventory,
        spells=character.spells,
        notes=character.notes,
    )
    
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    
    return db_character.to_dict()


@router.get("/{character_id}", response_model=CharacterResponse)
async def get_character(character_id: int, db: Session = Depends(get_db)):
    """
    Get a specific character by ID.
    """
    character = db.query(Character).filter(Character.id == character_id).first()
    
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    return character.to_dict()


@router.put("/{character_id}", response_model=CharacterResponse)
async def update_character(
    character_id: int,
    character_update: CharacterUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing character.
    Only provided fields will be updated.
    """
    character = db.query(Character).filter(Character.id == character_id).first()
    
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    # Update only provided fields
    update_data = character_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(character, field, value)
    
    db.commit()
    db.refresh(character)
    
    return character.to_dict()


@router.delete("/{character_id}")
async def delete_character(character_id: int, db: Session = Depends(get_db)):
    """
    Delete a character.
    """
    character = db.query(Character).filter(Character.id == character_id).first()
    
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    db.delete(character)
    db.commit()
    
    return {"message": f"Character '{character.name}' deleted successfully"}


@router.post("/{character_id}/damage")
async def take_damage(
    character_id: int,
    damage: int,
    db: Session = Depends(get_db)
):
    """
    Apply damage to a character.
    """
    character = db.query(Character).filter(Character.id == character_id).first()
    
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    character.hit_points_current = max(0, character.hit_points_current - damage)
    db.commit()
    db.refresh(character)
    
    return {
        "character": character.name,
        "damage_taken": damage,
        "current_hp": character.hit_points_current,
        "max_hp": character.hit_points_max,
        "status": "alive" if character.hit_points_current > 0 else "unconscious"
    }


@router.post("/{character_id}/heal")
async def heal_character(
    character_id: int,
    healing: int,
    db: Session = Depends(get_db)
):
    """
    Heal a character.
    """
    character = db.query(Character).filter(Character.id == character_id).first()
    
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    character.hit_points_current = min(
        character.hit_points_max,
        character.hit_points_current + healing
    )
    db.commit()
    db.refresh(character)
    
    return {
        "character": character.name,
        "healing_received": healing,
        "current_hp": character.hit_points_current,
        "max_hp": character.hit_points_max,
    }
