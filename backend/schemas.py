from pydantic import BaseModel
from typing import Optional


class CharacterCreate(BaseModel):
    name: str
    character_class: str
    level: int = 1
    race: str
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10
    hit_points: int = 10
    armor_class: int = 10


class CharacterResponse(CharacterCreate):
    id: int

    class Config:
        from_attributes = True


class DiceRollRequest(BaseModel):
    dice_type: int  # 4, 6, 8, 10, 12, 20, 100
    num_dice: int = 1
    modifier: int = 0


class DiceRollResponse(BaseModel):
    rolls: list[int]
    total: int
    modifier: int
    result: int


class EncounterRequest(BaseModel):
    party_level: int
    num_players: int = 4
    difficulty: str = "medium"  # easy, medium, hard, deadly


class EncounterResponse(BaseModel):
    target_cr: float
    monsters: list[dict]
    total_cr: float
