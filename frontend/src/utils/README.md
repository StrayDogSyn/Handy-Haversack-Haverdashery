# Utility Functions

This directory contains reusable helper functions and utilities.

## Purpose

Centralize common operations:
- Data formatting and validation
- Mathematical calculations
- String manipulation
- Date/time formatting
- Constants and enums

## Organization

- `formatting.ts` - Text and number formatting
- `validation.ts` - Input validation helpers
- `calculations.ts` - Game mechanic calculations
- `constants.ts` - App-wide constants
- `storage.ts` - LocalStorage helpers (for offline mode)

## Examples

```typescript
// calculations.ts
export const calculateAbilityModifier = (abilityScore: number): number => {
  return Math.floor((abilityScore - 10) / 2);
};

export const calculateProficiencyBonus = (level: number): number => {
  return Math.floor((level - 1) / 4) + 2;
};

export const calculateCR = (monsterLevel: number): number => {
  // Pathfinder 2e CR calculation
  return monsterLevel - 1;
};
```

```typescript
// validation.ts
export const isDiceNotation = (notation: string): boolean => {
  const dicePattern = /^\d+d\d+([+-]\d+)?$/;
  return dicePattern.test(notation);
};

export const isValidLevel = (level: number): boolean => {
  return level >= 1 && level <= 20;
};

export const isValidAbilityScore = (score: number): boolean => {
  return score >= 1 && score <= 30;
};
```

```typescript
// formatting.ts
export const formatModifier = (modifier: number): string => {
  return modifier >= 0 ? `+${modifier}` : `${modifier}`;
};

export const formatHP = (current: number, max: number): string => {
  return `${current}/${max} HP`;
};

export const formatDate = (date: Date): string => {
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });
};
```

```typescript
// constants.ts
export const DICE_TYPES = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100'] as const;

export const ABILITY_SCORES = [
  'strength',
  'dexterity',
  'constitution',
  'intelligence',
  'wisdom',
  'charisma',
] as const;

export const DIFFICULTY_LEVELS = {
  TRIVIAL: 'trivial',
  LOW: 'low',
  MODERATE: 'moderate',
  SEVERE: 'severe',
  EXTREME: 'extreme',
} as const;

export const API_ENDPOINTS = {
  DICE: '/api/dice',
  CHARACTERS: '/api/characters',
  ENCOUNTERS: '/api/encounters',
} as const;
```

## Usage

```typescript
import { calculateAbilityModifier, formatModifier } from '../utils/calculations';

const CharacterStats: React.FC<{ strength: number }> = ({ strength }) => {
  const modifier = calculateAbilityModifier(strength);
  return <div>STR: {strength} ({formatModifier(modifier)})</div>;
};
```
