"""
Encounter generation API endpoints.
"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Literal
from app.services.encounter_generator import encounter_generator

router = APIRouter()


class EncounterRequest(BaseModel):
    """Request model for encounter generation."""
    party_level: int = Field(..., ge=1, le=20, example=5, description="Average party level")
    party_size: int = Field(4, ge=1, le=10, example=4, description="Number of PCs")
    difficulty: Literal["easy", "moderate", "hard", "deadly"] = Field(
        "moderate",
        description="Encounter difficulty level"
    )


@router.post("/generate")
async def generate_encounter(request: EncounterRequest):
    """
    Generate a random encounter.
    
    Generates an encounter appropriate for the party's level and size.
    
    Difficulty levels:
    - **Easy**: Party should win with minimal resource expenditure
    - **Moderate**: Challenging fight, some resource use expected
    - **Hard**: Difficult fight, significant resources required
    - **Deadly**: Life-threatening encounter, potential for casualties
    
    Example:
    ```json
    {
      "party_level": 5,
      "party_size": 4,
      "difficulty": "moderate"
    }
    ```
    """
    encounter = encounter_generator.generate_encounter(
        party_level=request.party_level,
        party_size=request.party_size,
        difficulty=request.difficulty
    )
    
    return encounter


@router.get("/monsters")
async def list_monsters(
    min_cr: float = Query(0, ge=0, le=20, description="Minimum CR"),
    max_cr: float = Query(20, ge=0, le=20, description="Maximum CR")
):
    """
    Get list of available monsters.
    
    Filter by CR range to find appropriate monsters for your party level.
    """
    if min_cr > max_cr:
        raise HTTPException(
            status_code=400,
            detail="min_cr cannot be greater than max_cr"
        )
    
    monsters = encounter_generator.get_available_monsters(min_cr, max_cr)
    
    return {
        "monsters": monsters,
        "count": len(monsters),
        "cr_range": {"min": min_cr, "max": max_cr}
    }


@router.get("/difficulty-guide")
async def get_difficulty_guide():
    """
    Get guidelines for encounter difficulty.
    
    Returns recommended CR values for different party levels and difficulties.
    """
    guide = []
    
    for level in [1, 3, 5, 7, 10, 15, 20]:
        guide.append({
            "party_level": level,
            "party_size_4": {
                "easy": max(0.25, level - 2),
                "moderate": level,
                "hard": level + 2,
                "deadly": level + 4,
            }
        })
    
    return {
        "guide": guide,
        "notes": [
            "Values are approximate and assume a party of 4",
            "Adjust up for larger parties, down for smaller parties",
            "Consider party composition and player experience",
            "Multiple weaker enemies can be more dangerous than one strong enemy"
        ]
    }
