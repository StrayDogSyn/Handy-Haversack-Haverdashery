# TypeScript Type Definitions

This directory contains TypeScript interfaces and types for the frontend application.

## Purpose

Centralize type definitions to:
- Ensure type safety across components
- Define data structures from API responses
- Document expected data shapes
- Enable better IDE autocomplete

## Organization

- `character.types.ts` - Character-related types
- `dice.types.ts` - Dice rolling types
- `encounter.types.ts` - Encounter generation types
- `api.types.ts` - Generic API response types
- `common.types.ts` - Shared utility types

## Example

```typescript
// character.types.ts
export interface Character {
  id: number;
  name: string;
  level: number;
  class_name: string;
  race: string;
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;
  max_hp: number;
  current_hp: number;
  armor_class: number;
  initiative: number;
}

export interface CharacterCreate {
  name: string;
  level: number;
  class_name: string;
  race: string;
  // ... other required fields
}
```

## Usage

```typescript
import { Character } from '../types/character.types';

const CharacterCard: React.FC<{ character: Character }> = ({ character }) => {
  // Component implementation
};
```
