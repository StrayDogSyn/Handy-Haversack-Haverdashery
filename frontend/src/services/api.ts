const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export interface Character {
  id?: number;
  name: string;
  character_class: string;
  level: number;
  race: string;
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;
  hit_points: number;
  armor_class: number;
}

export interface DiceRoll {
  dice_type: number;
  num_dice: number;
  modifier: number;
}

export interface DiceRollResult {
  rolls: number[];
  total: number;
  modifier: number;
  result: number;
}

export interface EncounterRequest {
  party_level: number;
  num_players: number;
  difficulty: string;
}

export interface Monster {
  id: number;
  name: string;
  cr: number;
  type: string;
  hit_points: number;
  armor_class: number;
}

export interface EncounterResult {
  target_cr: number;
  monsters: Monster[];
  total_cr: number;
}

// Character API
export const characterApi = {
  async getAll(): Promise<Character[]> {
    const response = await fetch(`${API_BASE_URL}/api/characters/`);
    if (!response.ok) throw new Error('Failed to fetch characters');
    return response.json();
  },

  async getById(id: number): Promise<Character> {
    const response = await fetch(`${API_BASE_URL}/api/characters/${id}`);
    if (!response.ok) throw new Error('Failed to fetch character');
    return response.json();
  },

  async create(character: Character): Promise<Character> {
    const response = await fetch(`${API_BASE_URL}/api/characters/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(character),
    });
    if (!response.ok) throw new Error('Failed to create character');
    return response.json();
  },

  async update(id: number, character: Character): Promise<Character> {
    const response = await fetch(`${API_BASE_URL}/api/characters/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(character),
    });
    if (!response.ok) throw new Error('Failed to update character');
    return response.json();
  },

  async delete(id: number): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/api/characters/${id}`, {
      method: 'DELETE',
    });
    if (!response.ok) throw new Error('Failed to delete character');
  },
};

// Dice API
export const diceApi = {
  async roll(diceRoll: DiceRoll): Promise<DiceRollResult> {
    const response = await fetch(`${API_BASE_URL}/api/dice/roll`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(diceRoll),
    });
    if (!response.ok) throw new Error('Failed to roll dice');
    return response.json();
  },
};

// Encounter API
export const encounterApi = {
  async generate(request: EncounterRequest): Promise<EncounterResult> {
    const response = await fetch(`${API_BASE_URL}/api/encounters/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(request),
    });
    if (!response.ok) throw new Error('Failed to generate encounter');
    return response.json();
  },
};
