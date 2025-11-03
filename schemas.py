"""
Pydantic schemas for character API requests and responses.
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any
from datetime import datetime


class AbilityScores(BaseModel):
    """Character ability scores."""
    strength: int = Field(10, ge=1, le=30)
    dexterity: int = Field(10, ge=1, le=30)
    constitution: int = Field(10, ge=1, le=30)
    intelligence: int = Field(10, ge=1, le=30)
    wisdom: int = Field(10, ge=1, le=30)
    charisma: int = Field(10, ge=1, le=30)


class CombatStats(BaseModel):
    """Character combat statistics."""
    hit_points_max: int = Field(0, ge=0)
    hit_points_current: int = Field(0, ge=0)
    armor_class: int = Field(10, ge=0)
    initiative: int = Field(0)


class CharacterCreate(BaseModel):
    """Schema for creating a new character."""
    name: str = Field(..., min_length=1, max_length=100)
    player_name: Optional[str] = None
    race: Optional[str] = None
    character_class: Optional[str] = Field(None, alias="class")
    level: int = Field(1, ge=1, le=20)
    alignment: Optional[str] = None
    deity: Optional[str] = None
    
    # Ability scores
    strength: int = Field(10, ge=1, le=30)
    dexterity: int = Field(10, ge=1, le=30)
    constitution: int = Field(10, ge=1, le=30)
    intelligence: int = Field(10, ge=1, le=30)
    wisdom: int = Field(10, ge=1, le=30)
    charisma: int = Field(10, ge=1, le=30)
    
    # Combat stats
    hit_points_max: int = Field(0, ge=0)
    hit_points_current: int = Field(0, ge=0)
    armor_class: int = Field(10, ge=0)
    initiative: int = Field(0)
    
    # Additional data
    skills: Optional[Dict[str, Any]] = {}
    feats: Optional[List[str]] = []
    inventory: Optional[List[Dict[str, Any]]] = []
    spells: Optional[Dict[str, Any]] = {}
    notes: Optional[str] = None
    
    class Config:
        populate_by_name = True


class CharacterUpdate(BaseModel):
    """Schema for updating an existing character."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    player_name: Optional[str] = None
    race: Optional[str] = None
    character_class: Optional[str] = Field(None, alias="class")
    level: Optional[int] = Field(None, ge=1, le=20)
    alignment: Optional[str] = None
    deity: Optional[str] = None
    
    # Ability scores (all optional for partial updates)
    strength: Optional[int] = Field(None, ge=1, le=30)
    dexterity: Optional[int] = Field(None, ge=1, le=30)
    constitution: Optional[int] = Field(None, ge=1, le=30)
    intelligence: Optional[int] = Field(None, ge=1, le=30)
    wisdom: Optional[int] = Field(None, ge=1, le=30)
    charisma: Optional[int] = Field(None, ge=1, le=30)
    
    # Combat stats
    hit_points_max: Optional[int] = Field(None, ge=0)
    hit_points_current: Optional[int] = Field(None, ge=0)
    armor_class: Optional[int] = Field(None, ge=0)
    initiative: Optional[int] = None
    
    # Additional data
    skills: Optional[Dict[str, Any]] = None
    feats: Optional[List[str]] = None
    inventory: Optional[List[Dict[str, Any]]] = None
    spells: Optional[Dict[str, Any]] = None
    notes: Optional[str] = None
    
    class Config:
        populate_by_name = True


class CharacterResponse(BaseModel):
    """Schema for character API responses."""
    id: int
    name: str
    player_name: Optional[str]
    race: Optional[str]
    character_class: Optional[str] = Field(None, alias="class")
    level: int
    alignment: Optional[str]
    deity: Optional[str]
    ability_scores: AbilityScores
    combat: CombatStats
    skills: Dict[str, Any]
    feats: List[str]
    inventory: List[Dict[str, Any]]
    spells: Dict[str, Any]
    notes: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    
    class Config:
        populate_by_name = True
        from_attributes = True
