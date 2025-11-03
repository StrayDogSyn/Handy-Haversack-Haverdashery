"""
Dice rolling service with support for Pathfinder 2e dice notation
"""

import re
import random
from typing import List, Tuple, Optional


class DiceService:
    """Service for handling dice rolls"""
    
    def __init__(self):
        self.roll_history: List[dict] = []
    
    def parse_notation(self, notation: str) -> Tuple[int, int, int]:
        """
        Parse dice notation like "2d6+3" into components
        
        Args:
            notation: Dice notation string (e.g., "2d6+3", "1d20-1")
            
        Returns:
            Tuple of (num_dice, die_size, modifier)
            
        Raises:
            ValueError: If notation is invalid
        """
        notation = notation.strip().lower().replace(" ", "")
        
        # Pattern: XdY+/-Z or XdY
        pattern = r"^(\d+)d(\d+)(([+-])(\d+))?$"
        match = re.match(pattern, notation)
        
        if not match:
            raise ValueError(f"Invalid dice notation: {notation}")
        
        num_dice = int(match.group(1))
        die_size = int(match.group(2))
        
        modifier = 0
        if match.group(3):
            sign = match.group(4)
            value = int(match.group(5))
            modifier = value if sign == "+" else -value
        
        # Validate ranges
        if num_dice < 1 or num_dice > 100:
            raise ValueError("Number of dice must be between 1 and 100")
        if die_size not in [4, 6, 8, 10, 12, 20, 100]:
            raise ValueError("Die size must be one of: d4, d6, d8, d10, d12, d20, d100")
        
        return num_dice, die_size, modifier
    
    def roll_dice(self, notation: str) -> dict:
        """
        Roll dice based on notation
        
        Args:
            notation: Dice notation string
            
        Returns:
            Dictionary with roll results
        """
        num_dice, die_size, modifier = self.parse_notation(notation)
        
        rolls = [random.randint(1, die_size) for _ in range(num_dice)]
        total = sum(rolls) + modifier
        
        result = {
            "notation": notation,
            "num_dice": num_dice,
            "die_size": die_size,
            "rolls": rolls,
            "modifier": modifier,
            "total": total
        }
        
        self.roll_history.append(result)
        
        return result
    
    def roll_with_advantage(self) -> dict:
        """Roll d20 with advantage (roll twice, take highest)"""
        roll1 = random.randint(1, 20)
        roll2 = random.randint(1, 20)
        result = {
            "notation": "1d20 (Advantage)",
            "rolls": [roll1, roll2],
            "result": max(roll1, roll2),
            "type": "advantage"
        }
        self.roll_history.append(result)
        return result
    
    def roll_with_disadvantage(self) -> dict:
        """Roll d20 with disadvantage (roll twice, take lowest)"""
        roll1 = random.randint(1, 20)
        roll2 = random.randint(1, 20)
        result = {
            "notation": "1d20 (Disadvantage)",
            "rolls": [roll1, roll2],
            "result": min(roll1, roll2),
            "type": "disadvantage"
        }
        self.roll_history.append(result)
        return result
    
    def get_history(self) -> List[dict]:
        """Get roll history"""
        return self.roll_history.copy()
    
    def clear_history(self):
        """Clear roll history"""
        self.roll_history.clear()
    
    @staticmethod
    def calculate_average(notation: str) -> float:
        """Calculate average roll for a given notation"""
        service = DiceService()
        num_dice, die_size, modifier = service.parse_notation(notation)
        avg_per_die = (die_size + 1) / 2
        return (num_dice * avg_per_die) + modifier


# Create global instance
dice_service = DiceService()
