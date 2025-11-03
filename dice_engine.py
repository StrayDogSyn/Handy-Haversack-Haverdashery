"""
Dice rolling engine for Pathfinder.
Supports standard dice notation: XdY+Z (e.g., "2d6+3", "1d20", "4d6 drop lowest")
"""
import re
import random
from typing import List, Dict, Any
from datetime import datetime


class DiceRoller:
    """
    Handles dice rolling with various modifiers and options.
    """
    
    # Standard polyhedral dice
    VALID_DICE = [4, 6, 8, 10, 12, 20, 100]
    
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
    
    def roll(self, expression: str, advantage: bool = False, disadvantage: bool = False) -> Dict[str, Any]:
        """
        Roll dice based on expression.
        
        Args:
            expression: Dice expression like "2d6+3" or "1d20"
            advantage: Roll twice, take higher (for d20)
            disadvantage: Roll twice, take lower (for d20)
        
        Returns:
            Dictionary with roll results and details
        """
        expression = expression.lower().strip()
        
        # Parse the dice expression
        parsed = self._parse_expression(expression)
        if not parsed:
            return {"error": "Invalid dice expression", "expression": expression}
        
        num_dice, die_size, modifier = parsed
        
        # Validate die size
        if die_size not in self.VALID_DICE:
            return {"error": f"Invalid die size: d{die_size}. Valid: {self.VALID_DICE}"}
        
        # Roll the dice
        rolls = [random.randint(1, die_size) for _ in range(num_dice)]
        
        # Handle advantage/disadvantage for d20
        if die_size == 20 and num_dice == 1:
            if advantage:
                second_roll = random.randint(1, 20)
                rolls = [max(rolls[0], second_roll)]
                modifier_text = f"advantage (rolled {rolls[0]} and {second_roll})"
            elif disadvantage:
                second_roll = random.randint(1, 20)
                rolls = [min(rolls[0], second_roll)]
                modifier_text = f"disadvantage (rolled {rolls[0]} and {second_roll})"
            else:
                modifier_text = None
        else:
            modifier_text = None
        
        # Calculate total
        subtotal = sum(rolls)
        total = subtotal + modifier
        
        # Build result
        result = {
            "expression": expression,
            "num_dice": num_dice,
            "die_size": die_size,
            "modifier": modifier,
            "rolls": rolls,
            "subtotal": subtotal,
            "total": total,
            "timestamp": datetime.now().isoformat(),
        }
        
        if modifier_text:
            result["note"] = modifier_text
        
        # Add to history
        self.history.append(result)
        
        return result
    
    def _parse_expression(self, expression: str) -> tuple[int, int, int] | None:
        """
        Parse dice expression into components.
        
        Args:
            expression: String like "2d6+3" or "1d20-1"
        
        Returns:
            Tuple of (num_dice, die_size, modifier) or None if invalid
        """
        # Remove spaces
        expression = expression.replace(" ", "")
        
        # Pattern: [num]d[size][+/-][modifier]
        pattern = r'^(\d+)?d(\d+)([+\-]\d+)?$'
        match = re.match(pattern, expression)
        
        if not match:
            return None
        
        num_dice = int(match.group(1)) if match.group(1) else 1
        die_size = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0
        
        return (num_dice, die_size, modifier)
    
    def roll_multiple(self, expression: str, times: int = 1) -> List[Dict[str, Any]]:
        """
        Roll the same expression multiple times.
        Useful for things like rolling stats (4d6 drop lowest, done 6 times).
        """
        return [self.roll(expression) for _ in range(times)]
    
    def get_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent roll history."""
        return self.history[-limit:]
    
    def clear_history(self):
        """Clear roll history."""
        self.history.clear()


# Create a singleton instance
dice_roller = DiceRoller()
