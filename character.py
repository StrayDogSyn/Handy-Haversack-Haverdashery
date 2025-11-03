"""
Character database models for Pathfinder.
"""
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Character(Base):
    """
    Pathfinder character model.
    Stores core character information and stats.
    """
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    player_name = Column(String, nullable=True)
    
    # Core identity
    race = Column(String, nullable=True)
    character_class = Column(String, nullable=True)  # 'class' is a Python keyword
    level = Column(Integer, default=1)
    alignment = Column(String, nullable=True)
    deity = Column(String, nullable=True)
    
    # Ability scores (base scores)
    strength = Column(Integer, default=10)
    dexterity = Column(Integer, default=10)
    constitution = Column(Integer, default=10)
    intelligence = Column(Integer, default=10)
    wisdom = Column(Integer, default=10)
    charisma = Column(Integer, default=10)
    
    # Combat stats
    hit_points_max = Column(Integer, default=0)
    hit_points_current = Column(Integer, default=0)
    armor_class = Column(Integer, default=10)
    initiative = Column(Integer, default=0)
    
    # Additional data stored as JSON for flexibility
    # This can include: skills, feats, inventory, spells, etc.
    skills = Column(JSON, default=dict)
    feats = Column(JSON, default=list)
    inventory = Column(JSON, default=list)
    spells = Column(JSON, default=dict)
    notes = Column(String, nullable=True)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Character(name='{self.name}', level={self.level}, class='{self.character_class}')>"
    
    def to_dict(self):
        """Convert character to dictionary for API responses."""
        return {
            "id": self.id,
            "name": self.name,
            "player_name": self.player_name,
            "race": self.race,
            "class": self.character_class,
            "level": self.level,
            "alignment": self.alignment,
            "deity": self.deity,
            "ability_scores": {
                "strength": self.strength,
                "dexterity": self.dexterity,
                "constitution": self.constitution,
                "intelligence": self.intelligence,
                "wisdom": self.wisdom,
                "charisma": self.charisma,
            },
            "combat": {
                "hit_points_max": self.hit_points_max,
                "hit_points_current": self.hit_points_current,
                "armor_class": self.armor_class,
                "initiative": self.initiative,
            },
            "skills": self.skills,
            "feats": self.feats,
            "inventory": self.inventory,
            "spells": self.spells,
            "notes": self.notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
