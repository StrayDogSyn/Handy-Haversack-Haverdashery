"""
Encounter generation service for creating balanced combat encounters
"""

import random
from typing import List, Dict, Optional
from app.services.bestiary import BESTIARY


class EncounterService:
    """Service for generating combat encounters"""
    
    DIFFICULTY_XP_BUDGETS = {
        "trivial": 40,
        "low": 60,
        "moderate": 80,
        "severe": 120,
        "extreme": 160
    }
    
    def __init__(self):
        self.bestiary = BESTIARY
    
    def calculate_xp_budget(self, party_level: int, party_size: int, difficulty: str) -> int:
        """
        Calculate total XP budget for encounter
        
        Args:
            party_level: Average party level
            party_size: Number of characters in party
            difficulty: Difficulty level (trivial, low, moderate, severe, extreme)
            
        Returns:
            Total XP budget
        """
        if difficulty not in self.DIFFICULTY_XP_BUDGETS:
            raise ValueError(f"Invalid difficulty. Must be one of: {list(self.DIFFICULTY_XP_BUDGETS.keys())}")
        
        base_xp = self.DIFFICULTY_XP_BUDGETS[difficulty]
        return base_xp * party_size
    
    def get_monsters_by_cr(self, min_cr: float = None, max_cr: float = None) -> List[Dict]:
        """Get monsters within CR range"""
        monsters = []
        for monster in self.bestiary:
            cr = monster["cr"]
            if min_cr is not None and cr < min_cr:
                continue
            if max_cr is not None and cr > max_cr:
                continue
            monsters.append(monster)
        return monsters
    
    def generate_encounter(
        self,
        party_level: int,
        party_size: int = 4,
        difficulty: str = "moderate"
    ) -> Dict:
        """
        Generate a balanced encounter
        
        Args:
            party_level: Average party level
            party_size: Number of characters in party
            difficulty: Difficulty level
            
        Returns:
            Dictionary with encounter details
        """
        xp_budget = self.calculate_xp_budget(party_level, party_size, difficulty)
        
        # Get appropriate monsters (CR = party_level +/- 2)
        suitable_monsters = self.get_monsters_by_cr(
            min_cr=max(0, party_level - 2),
            max_cr=party_level + 3
        )
        
        if not suitable_monsters:
            raise ValueError(f"No suitable monsters found for party level {party_level}")
        
        # Generate encounter within XP budget
        encounter_monsters = []
        remaining_xp = xp_budget
        
        attempts = 0
        max_attempts = 50
        
        while remaining_xp > 20 and attempts < max_attempts:
            # Filter monsters that fit in remaining budget
            affordable_monsters = [
                m for m in suitable_monsters
                if m["xp"] <= remaining_xp
            ]
            
            if not affordable_monsters:
                break
            
            # Pick a random monster
            monster = random.choice(affordable_monsters)
            encounter_monsters.append(monster)
            remaining_xp -= monster["xp"]
            attempts += 1
        
        # Calculate actual difficulty
        total_xp = sum(m["xp"] for m in encounter_monsters)
        
        return {
            "party_level": party_level,
            "party_size": party_size,
            "difficulty": difficulty,
            "xp_budget": xp_budget,
            "total_xp": total_xp,
            "monsters": encounter_monsters,
            "monster_count": len(encounter_monsters),
            "tactics": self._generate_tactics(encounter_monsters)
        }
    
    def _generate_tactics(self, monsters: List[Dict]) -> str:
        """Generate tactical suggestions for the encounter"""
        if not monsters:
            return "No monsters in encounter"
        
        count = len(monsters)
        avg_cr = sum(m["cr"] for m in monsters) / count
        
        if count == 1:
            return f"Single {monsters[0]['name']} - Consider environmental hazards or minions"
        elif count <= 3:
            return f"Small group - Focus fire on the strongest enemy ({monsters[0]['name']})"
        else:
            return f"Large group - Use area control and prioritize high-damage targets"


# Create global instance
encounter_service = EncounterService()
