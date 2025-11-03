"""
Character management API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
import json

from app.database import get_db
from app.models.character import Character

router = APIRouter()


class CharacterCreate(BaseModel):
    """Request model for creating a character"""
    name: str
    ancestry: Optional[str] = None
    background: Optional[str] = None
    class_name: Optional[str] = None
    level: int = 1
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10
    hit_points: Optional[int] = None
    max_hit_points: int = 10
    armor_class: int = 10
    initiative: int = 0
    skills: List[str] = []
    feats: List[str] = []
    inventory: List[str] = []


class CharacterUpdate(BaseModel):
    """Request model for updating a character"""
    name: Optional[str] = None
    ancestry: Optional[str] = None
    background: Optional[str] = None
    class_name: Optional[str] = None
    level: Optional[int] = None
    strength: Optional[int] = None
    dexterity: Optional[int] = None
    constitution: Optional[int] = None
    intelligence: Optional[int] = None
    wisdom: Optional[int] = None
    charisma: Optional[int] = None
    hit_points: Optional[int] = None
    max_hit_points: Optional[int] = None
    armor_class: Optional[int] = None
    initiative: Optional[int] = None
    skills: Optional[List[str]] = None
    feats: Optional[List[str]] = None
    inventory: Optional[List[str]] = None


class DamageRequest(BaseModel):
    """Request model for applying damage"""
    damage: int


class HealRequest(BaseModel):
    """Request model for healing"""
    healing: int


@router.post("")
async def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    """Create a new character"""
    db_character = Character(
        name=character.name,
        ancestry=character.ancestry,
        background=character.background,
        class_name=character.class_name,
        level=character.level,
        strength=character.strength,
        dexterity=character.dexterity,
        constitution=character.constitution,
        intelligence=character.intelligence,
        wisdom=character.wisdom,
        charisma=character.charisma,
        hit_points=character.hit_points if character.hit_points is not None else character.max_hit_points,
        max_hit_points=character.max_hit_points,
        armor_class=character.armor_class,
        initiative=character.initiative,
        skills=json.dumps(character.skills),
        feats=json.dumps(character.feats),
        inventory=json.dumps(character.inventory)
    )
    
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    
    return db_character.to_dict()


@router.get("")
async def list_characters(db: Session = Depends(get_db)):
    """List all characters"""
    characters = db.query(Character).all()
    return [char.to_dict() for char in characters]


@router.get("/{character_id}")
async def get_character(character_id: int, db: Session = Depends(get_db)):
    """Get a specific character"""
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character.to_dict()


@router.put("/{character_id}")
async def update_character(
    character_id: int,
    character_update: CharacterUpdate,
    db: Session = Depends(get_db)
):
    """Update a character"""
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    # Update fields if provided
    update_data = character_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        if field in ["skills", "feats", "inventory"]:
            setattr(character, field, json.dumps(value))
        else:
            setattr(character, field, value)
    
    db.commit()
    db.refresh(character)
    
    return character.to_dict()


@router.delete("/{character_id}")
async def delete_character(character_id: int, db: Session = Depends(get_db)):
    """Delete a character"""
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    db.delete(character)
    db.commit()
    
    return {"message": f"Character {character.name} deleted"}


@router.post("/{character_id}/damage")
async def apply_damage(
    character_id: int,
    damage_request: DamageRequest,
    db: Session = Depends(get_db)
):
    """Apply damage to a character"""
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    character.hit_points = max(0, character.hit_points - damage_request.damage)
    db.commit()
    db.refresh(character)
    
    return {
        "message": f"Applied {damage_request.damage} damage",
        "character": character.to_dict()
    }


@router.post("/{character_id}/heal")
async def heal_character(
    character_id: int,
    heal_request: HealRequest,
    db: Session = Depends(get_db)
):
    """Heal a character"""
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    character.hit_points = min(character.max_hit_points, character.hit_points + heal_request.healing)
    db.commit()
    db.refresh(character)
    
    return {
        "message": f"Healed {heal_request.healing} hit points",
        "character": character.to_dict()
    }
