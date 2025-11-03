"""
Character database model
"""

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base


class Character(Base):
    """Character model for Pathfinder 2e characters"""
    
    __tablename__ = "characters"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Basic Info
    name = Column(String(100), nullable=False, index=True)
    ancestry = Column(String(50))
    background = Column(String(50))
    class_name = Column(String(50))
    level = Column(Integer, default=1)
    
    # Ability Scores
    strength = Column(Integer, default=10)
    dexterity = Column(Integer, default=10)
    constitution = Column(Integer, default=10)
    intelligence = Column(Integer, default=10)
    wisdom = Column(Integer, default=10)
    charisma = Column(Integer, default=10)
    
    # Combat Stats
    hit_points = Column(Integer, default=10)
    max_hit_points = Column(Integer, default=10)
    armor_class = Column(Integer, default=10)
    initiative = Column(Integer, default=0)
    
    # Additional Data (stored as JSON strings)
    skills = Column(Text, default="[]")  # JSON array
    feats = Column(Text, default="[]")   # JSON array
    inventory = Column(Text, default="[]")  # JSON array
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def to_dict(self):
        """Convert model to dictionary"""
        import json
        return {
            "id": self.id,
            "name": self.name,
            "ancestry": self.ancestry,
            "background": self.background,
            "class_name": self.class_name,
            "level": self.level,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
            "hit_points": self.hit_points,
            "max_hit_points": self.max_hit_points,
            "armor_class": self.armor_class,
            "initiative": self.initiative,
            "skills": json.loads(self.skills) if self.skills else [],
            "feats": json.loads(self.feats) if self.feats else [],
            "inventory": json.loads(self.inventory) if self.inventory else [],
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
