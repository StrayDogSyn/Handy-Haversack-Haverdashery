"""
Bestiary data for Pathfinder 2e monsters
Each monster has: name, CR, XP, type, and basic stats
"""

BESTIARY = [
    # CR 0-1 Creatures
    {"name": "Goblin Warrior", "cr": 0.5, "xp": 20, "type": "Humanoid", "hp": 15, "ac": 16},
    {"name": "Giant Rat", "cr": 0.25, "xp": 10, "type": "Animal", "hp": 8, "ac": 12},
    {"name": "Skeleton Guard", "cr": 0.5, "xp": 20, "type": "Undead", "hp": 16, "ac": 14},
    {"name": "Zombie Shambler", "cr": 0.5, "xp": 20, "type": "Undead", "hp": 20, "ac": 12},
    {"name": "Kobold Scout", "cr": 0.25, "xp": 10, "type": "Humanoid", "hp": 12, "ac": 15},
    
    # CR 1-2 Creatures
    {"name": "Orc Warrior", "cr": 1, "xp": 40, "type": "Humanoid", "hp": 24, "ac": 17},
    {"name": "Goblin Commando", "cr": 1, "xp": 40, "type": "Humanoid", "hp": 20, "ac": 17},
    {"name": "Giant Spider", "cr": 1, "xp": 40, "type": "Vermin", "hp": 26, "ac": 15},
    {"name": "Dire Wolf", "cr": 2, "xp": 60, "type": "Animal", "hp": 38, "ac": 16},
    {"name": "Bugbear Thug", "cr": 2, "xp": 60, "type": "Humanoid", "hp": 36, "ac": 16},
    
    # CR 3-4 Creatures
    {"name": "Ogre Brute", "cr": 3, "xp": 80, "type": "Giant", "hp": 54, "ac": 17},
    {"name": "Hell Hound", "cr": 3, "xp": 80, "type": "Fiend", "hp": 40, "ac": 18},
    {"name": "Werewolf", "cr": 3, "xp": 80, "type": "Humanoid", "hp": 48, "ac": 17},
    {"name": "Minotaur", "cr": 4, "xp": 120, "type": "Monstrosity", "hp": 76, "ac": 17},
    {"name": "Ettin", "cr": 4, "xp": 120, "type": "Giant", "hp": 85, "ac": 16},
    
    # CR 5-6 Creatures
    {"name": "Troll", "cr": 5, "xp": 160, "type": "Giant", "hp": 95, "ac": 17},
    {"name": "Young Dragon", "cr": 5, "xp": 160, "type": "Dragon", "hp": 100, "ac": 20},
    {"name": "Hill Giant", "cr": 5, "xp": 160, "type": "Giant", "hp": 110, "ac": 17},
    {"name": "Stone Golem", "cr": 6, "xp": 240, "type": "Construct", "hp": 125, "ac": 20},
    {"name": "Wyvern", "cr": 6, "xp": 240, "type": "Dragon", "hp": 95, "ac": 18},
    
    # CR 7-8 Creatures
    {"name": "Chimera", "cr": 7, "xp": 320, "type": "Monstrosity", "hp": 115, "ac": 17},
    {"name": "Frost Giant", "cr": 7, "xp": 320, "type": "Giant", "hp": 138, "ac": 18},
    {"name": "Adult Dragon", "cr": 8, "xp": 480, "type": "Dragon", "hp": 180, "ac": 22},
    {"name": "Demon Lord", "cr": 8, "xp": 480, "type": "Fiend", "hp": 170, "ac": 19},
    
    # Utility creatures
    {"name": "Animated Armor", "cr": 1, "xp": 40, "type": "Construct", "hp": 30, "ac": 18},
    {"name": "Ghoul", "cr": 1, "xp": 40, "type": "Undead", "hp": 22, "ac": 15},
    {"name": "Shadow", "cr": 2, "xp": 60, "type": "Undead", "hp": 20, "ac": 14},
    {"name": "Specter", "cr": 3, "xp": 80, "type": "Undead", "hp": 28, "ac": 13},
    {"name": "Wraith", "cr": 4, "xp": 120, "type": "Undead", "hp": 45, "ac": 15},
    {"name": "Vampire Spawn", "cr": 5, "xp": 160, "type": "Undead", "hp": 82, "ac": 16},
]


def get_monster_by_name(name: str) -> dict:
    """Get monster by name"""
    for monster in BESTIARY:
        if monster["name"].lower() == name.lower():
            return monster
    return None


def get_monsters_by_type(monster_type: str) -> list:
    """Get all monsters of a specific type"""
    return [m for m in BESTIARY if m["type"].lower() == monster_type.lower()]


def get_monsters_by_cr_range(min_cr: float, max_cr: float) -> list:
    """Get monsters within CR range"""
    return [m for m in BESTIARY if min_cr <= m["cr"] <= max_cr]
