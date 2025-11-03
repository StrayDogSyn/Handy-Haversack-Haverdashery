# Pydantic Schemas

This directory contains Pydantic models for request/response validation.

## Purpose

Define data validation schemas to:
- Validate API request payloads
- Define API response structures
- Provide automatic documentation
- Enable type hints and IDE support
- Separate validation from database models

## Organization

- `character_schemas.py` - Character request/response models
- `dice_schemas.py` - Dice rolling models
- `encounter_schemas.py` - Encounter generation models
- `campaign_schemas.py` - Campaign management (Phase 2)
- `base_schemas.py` - Shared base models

## Example

```python
# character_schemas.py
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, List

class CharacterBase(BaseModel):
    """Base character attributes."""
    name: str = Field(..., min_length=1, max_length=100)
    level: int = Field(..., ge=1, le=20)
    class_name: str = Field(..., max_length=50)
    race: str = Field(..., max_length=50)
    strength: int = Field(..., ge=1, le=30)
    dexterity: int = Field(..., ge=1, le=30)
    constitution: int = Field(..., ge=1, le=30)
    intelligence: int = Field(..., ge=1, le=30)
    wisdom: int = Field(..., ge=1, le=30)
    charisma: int = Field(..., ge=1, le=30)
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()

class CharacterCreate(CharacterBase):
    """Schema for creating a new character."""
    max_hp: int = Field(..., ge=1)
    armor_class: int = Field(..., ge=1)
    initiative: int
    skills: Optional[Dict] = {}
    feats: Optional[List[str]] = []
    inventory: Optional[List[Dict]] = []

class CharacterUpdate(BaseModel):
    """Schema for updating an existing character (all fields optional)."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    level: Optional[int] = Field(None, ge=1, le=20)
    current_hp: Optional[int] = Field(None, ge=0)
    # ... other optional fields

class CharacterResponse(CharacterBase):
    """Schema for character responses."""
    id: int
    current_hp: int
    max_hp: int
    armor_class: int
    initiative: int
    created_at: str
    updated_at: str
    
    class Config:
        from_attributes = True  # Allows creation from ORM models
```

```python
# dice_schemas.py
from pydantic import BaseModel, Field, validator
from typing import List
import re

class DiceRollRequest(BaseModel):
    """Request to roll dice."""
    notation: str = Field(..., description="Dice notation (e.g., '2d6+3')")
    
    @validator('notation')
    def validate_notation(cls, v):
        pattern = r'^\d+d\d+([+-]\d+)?$'
        if not re.match(pattern, v):
            raise ValueError('Invalid dice notation')
        return v

class DiceRollResponse(BaseModel):
    """Response from dice roll."""
    notation: str
    total: int
    rolls: List[int]
    modifier: int = 0
    timestamp: str
    
class DiceHistoryResponse(BaseModel):
    """Response with roll history."""
    history: List[DiceRollResponse]
    count: int
```

## Usage in API Endpoints

```python
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.character_schemas import CharacterCreate, CharacterResponse
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/characters", tags=["characters"])

@router.post("/", response_model=CharacterResponse, status_code=status.HTTP_201_CREATED)
async def create_character(
    character: CharacterCreate,  # Automatically validates request body
    db: Session = Depends(get_db)
):
    """Create a new character with validation."""
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character  # Automatically serialized to CharacterResponse
```

## Benefits

1. **Automatic Validation**: Pydantic validates all fields automatically
2. **Clear Documentation**: FastAPI uses schemas to generate API docs
3. **Type Safety**: IDE autocomplete and type checking
4. **Separation of Concerns**: Keep validation separate from database models
5. **Flexible Responses**: Different schemas for different contexts
