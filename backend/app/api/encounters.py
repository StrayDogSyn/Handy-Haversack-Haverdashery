"""
Encounter generation API endpoints
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.services.encounter_service import encounter_service
from app.services.bestiary import BESTIARY, get_monster_by_name, get_monsters_by_type

router = APIRouter()


class EncounterRequest(BaseModel):
    """Request model for encounter generation"""
    party_level: int
    party_size: int = 4
    difficulty: str = "moderate"


@router.post("/generate")
async def generate_encounter(request: EncounterRequest):
    """
    Generate a balanced encounter for a party
    
    - **party_level**: Average level of the party (1-20)
    - **party_size**: Number of characters (1-10)
    - **difficulty**: One of: trivial, low, moderate, severe, extreme
    """
    try:
        encounter = encounter_service.generate_encounter(
            party_level=request.party_level,
            party_size=request.party_size,
            difficulty=request.difficulty
        )
        return encounter
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/bestiary")
async def get_bestiary():
    """
    Get all monsters in the bestiary
    """
    return {
        "monsters": BESTIARY,
        "count": len(BESTIARY)
    }


@router.get("/bestiary/{monster_name}")
async def get_monster(monster_name: str):
    """
    Get details for a specific monster
    """
    monster = get_monster_by_name(monster_name)
    if not monster:
        raise HTTPException(status_code=404, detail=f"Monster '{monster_name}' not found")
    return monster


@router.get("/bestiary/type/{monster_type}")
async def get_monsters_by_type_endpoint(monster_type: str):
    """
    Get all monsters of a specific type
    """
    monsters = get_monsters_by_type(monster_type)
    return {
        "type": monster_type,
        "monsters": monsters,
        "count": len(monsters)
    }
