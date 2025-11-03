"""
Dice rolling API endpoints
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.dice_service import dice_service

router = APIRouter()


class DiceRollRequest(BaseModel):
    """Request model for dice rolls"""
    notation: str


@router.post("/roll")
async def roll_dice(request: DiceRollRequest):
    """
    Roll dice with standard notation (e.g., "2d6+3", "1d20-1")
    """
    try:
        result = dice_service.roll_dice(request.notation)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/roll/advantage")
async def roll_with_advantage():
    """
    Roll d20 with advantage (roll twice, take highest)
    """
    result = dice_service.roll_with_advantage()
    return result


@router.post("/roll/disadvantage")
async def roll_with_disadvantage():
    """
    Roll d20 with disadvantage (roll twice, take lowest)
    """
    result = dice_service.roll_with_disadvantage()
    return result


@router.get("/history")
async def get_roll_history():
    """
    Get history of all rolls in current session
    """
    history = dice_service.get_history()
    return {"history": history, "count": len(history)}


@router.delete("/history")
async def clear_roll_history():
    """
    Clear roll history
    """
    dice_service.clear_history()
    return {"message": "Roll history cleared"}


@router.get("/average/{notation}")
async def calculate_average(notation: str):
    """
    Calculate average roll for given notation
    """
    try:
        avg = dice_service.calculate_average(notation)
        return {"notation": notation, "average": avg}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
