"""
Dice rolling API endpoints.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from app.services.dice_engine import dice_roller

router = APIRouter()


class DiceRollRequest(BaseModel):
    """Request model for dice rolling."""
    expression: str = Field(..., example="2d6+3", description="Dice expression (e.g., '2d6+3', '1d20')")
    advantage: bool = Field(False, description="Roll with advantage (d20 only)")
    disadvantage: bool = Field(False, description="Roll with disadvantage (d20 only)")


class MultipleDiceRollRequest(BaseModel):
    """Request model for multiple dice rolls."""
    expression: str = Field(..., example="4d6", description="Dice expression")
    times: int = Field(..., ge=1, le=20, example=6, description="Number of times to roll")


@router.post("/roll")
async def roll_dice(request: DiceRollRequest):
    """
    Roll dice based on expression.
    
    Supports standard dice notation:
    - Simple: "d20", "d6", "2d8"
    - With modifiers: "1d20+5", "2d6-1"
    - Advantage/Disadvantage: "1d20" with advantage=true
    
    Examples:
    - "1d20+5" - Roll a d20 and add 5
    - "2d6" - Roll two d6 dice
    - "4d6" - Roll four d6 dice (useful with "drop lowest" logic for stats)
    """
    result = dice_roller.roll(
        request.expression,
        advantage=request.advantage,
        disadvantage=request.disadvantage
    )
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result


@router.post("/roll-multiple")
async def roll_multiple(request: MultipleDiceRollRequest):
    """
    Roll the same dice expression multiple times.
    
    Useful for:
    - Rolling stats (4d6 drop lowest, done 6 times)
    - Rolling damage for multiple attacks
    - Generating random values in bulk
    """
    results = dice_roller.roll_multiple(request.expression, request.times)
    return {
        "expression": request.expression,
        "times": request.times,
        "rolls": results
    }


@router.get("/history")
async def get_history(limit: int = 10):
    """
    Get recent roll history.
    
    Args:
        limit: Number of recent rolls to return (max 50)
    """
    if limit > 50:
        limit = 50
    
    history = dice_roller.get_history(limit)
    return {
        "history": history,
        "count": len(history)
    }


@router.delete("/history")
async def clear_history():
    """Clear roll history."""
    dice_roller.clear_history()
    return {"message": "Roll history cleared"}


@router.get("/supported-dice")
async def get_supported_dice():
    """Get list of supported dice types."""
    return {
        "dice": dice_roller.VALID_DICE,
        "examples": [
            "1d20+5",
            "2d6",
            "4d6",
            "1d8+3",
            "3d10-2"
        ]
    }
