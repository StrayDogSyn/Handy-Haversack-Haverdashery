"""
Encounter generator for Pathfinder.
Generates random encounters based on party level and CR (Challenge Rating).
"""
import random
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class Monster:
    """Represents a monster/enemy."""
    name: str
    cr: float
    hp: int
    ac: int
    description: str = ""


# Starter bestiary - will be expanded with PDF parsing later
BESTIARY = [
    # CR 1/4
    Monster("Goblin Warrior", 0.25, 6, 16, "Small, sneaky humanoid"),
    Monster("Skeleton", 0.25, 4, 15, "Undead minion"),
    
    # CR 1/2
    Monster("Hobgoblin", 0.5, 11, 18, "Disciplined warrior"),
    Monster("Orc Warrior", 0.5, 15, 13, "Brutal fighter"),
    
    # CR 1
    Monster("Bugbear", 1, 27, 16, "Hairy goblinoid"),
    Monster("Giant Spider", 1, 26, 14, "Web-spinning predator"),
    Monster("Dire Rat", 1, 5, 15, "Oversized vermin"),
    
    # CR 2
    Monster("Ogre", 2, 30, 13, "Large brutish humanoid"),
    Monster("Werewolf", 2, 58, 11, "Shapeshifting lycanthrope"),
    Monster("Ghoul", 2, 13, 14, "Flesh-eating undead"),
    
    # CR 3
    Monster("Owlbear", 3, 47, 15, "Ferocious magical beast"),
    Monster("Basilisk", 3, 45, 16, "Petrifying reptile"),
    Monster("Hell Hound", 3, 30, 16, "Fiery canine fiend"),
    
    # CR 4
    Monster("Minotaur", 4, 45, 14, "Bull-headed warrior"),
    Monster("Ettin", 4, 65, 17, "Two-headed giant"),
    
    # CR 5
    Monster("Troll", 5, 63, 16, "Regenerating monster"),
    Monster("Hill Giant", 5, 85, 19, "Massive humanoid"),
    
    # CR 7
    Monster("Stone Giant", 7, 119, 20, "Skilled rock-thrower"),
    
    # CR 9
    Monster("Fire Giant", 9, 142, 21, "Forge master giant"),
]


class EncounterGenerator:
    """Generates encounters based on party parameters."""
    
    def __init__(self):
        self.bestiary = BESTIARY
    
    def generate_encounter(
        self,
        party_level: int,
        party_size: int = 4,
        difficulty: str = "moderate"
    ) -> Dict[str, Any]:
        """
        Generate a random encounter.
        
        Args:
            party_level: Average party level (1-20)
            party_size: Number of PCs in the party
            difficulty: "easy", "moderate", "hard", "deadly"
        
        Returns:
            Dictionary with encounter details
        """
        # Calculate target CR based on difficulty
        target_cr = self._calculate_target_cr(party_level, party_size, difficulty)
        
        # Generate encounter
        monsters = self._select_monsters(target_cr)
        
        # Calculate statistics
        total_cr = sum(m.cr for m in monsters)
        total_hp = sum(m.hp for m in monsters)
        avg_ac = sum(m.ac for m in monsters) / len(monsters) if monsters else 0
        
        return {
            "party_level": party_level,
            "party_size": party_size,
            "difficulty": difficulty,
            "target_cr": target_cr,
            "total_cr": round(total_cr, 2),
            "monsters": [
                {
                    "name": m.name,
                    "cr": m.cr,
                    "hp": m.hp,
                    "ac": m.ac,
                    "description": m.description,
                }
                for m in monsters
            ],
            "statistics": {
                "total_hp": total_hp,
                "average_ac": round(avg_ac, 1),
                "monster_count": len(monsters),
            },
            "tactics": self._generate_tactics(monsters),
        }
    
    def _calculate_target_cr(
        self,
        party_level: int,
        party_size: int,
        difficulty: str
    ) -> float:
        """
        Calculate the target CR for the encounter.
        
        Simplified system:
        - Easy: CR = party_level - 2
        - Moderate: CR = party_level
        - Hard: CR = party_level + 2
        - Deadly: CR = party_level + 4
        
        Adjusted for party size (4 is baseline).
        """
        difficulty_modifiers = {
            "easy": -2,
            "moderate": 0,
            "hard": 2,
            "deadly": 4,
        }
        
        base_cr = party_level + difficulty_modifiers.get(difficulty, 0)
        
        # Adjust for party size (4 is baseline)
        size_modifier = (party_size - 4) * 0.5
        target_cr = max(0.25, base_cr + size_modifier)
        
        return target_cr
    
    def _select_monsters(self, target_cr: float) -> List[Monster]:
        """
        Select monsters that approximately match the target CR.
        
        Strategy:
        - 50% chance: Single monster near target CR
        - 50% chance: Multiple weaker monsters
        """
        available = [m for m in self.bestiary if m.cr <= target_cr]
        
        if not available:
            # If no suitable monsters, return easiest
            return [min(self.bestiary, key=lambda m: m.cr)]
        
        strategy = random.choice(["single", "multiple"])
        
        if strategy == "single" or target_cr < 1:
            # Single monster close to target CR
            suitable = [m for m in available if m.cr >= target_cr * 0.75]
            if not suitable:
                suitable = available
            return [random.choice(suitable)]
        
        else:
            # Multiple weaker monsters
            monsters = []
            remaining_cr = target_cr
            
            while remaining_cr > 0.25 and len(monsters) < 8:
                suitable = [m for m in available if m.cr <= remaining_cr]
                if not suitable:
                    break
                
                monster = random.choice(suitable)
                monsters.append(monster)
                remaining_cr -= monster.cr
            
            return monsters if monsters else [random.choice(available)]
    
    def _generate_tactics(self, monsters: List[Monster]) -> str:
        """Generate basic tactical suggestions."""
        if len(monsters) == 1:
            return "Single powerful enemy. Focus fire or use crowd control."
        elif len(monsters) <= 3:
            return "Small group. Consider area effects or divide and conquer."
        else:
            return "Large group. Area attacks are highly effective. Control the battlefield."
    
    def get_available_monsters(
        self,
        min_cr: float = 0,
        max_cr: float = 20
    ) -> List[Dict[str, Any]]:
        """Get list of available monsters within CR range."""
        return [
            {
                "name": m.name,
                "cr": m.cr,
                "hp": m.hp,
                "ac": m.ac,
                "description": m.description,
            }
            for m in self.bestiary
            if min_cr <= m.cr <= max_cr
        ]


# Singleton instance
encounter_generator = EncounterGenerator()
