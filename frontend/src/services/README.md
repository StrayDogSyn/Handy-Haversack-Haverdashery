# API Service Layer

This directory contains API client services for backend communication.

## Purpose

Centralize API calls to:
- Provide a single source of truth for backend endpoints
- Enable easy endpoint updates
- Handle common error cases
- Provide type-safe API methods
- Enable request/response interceptors

## Organization

- `apiClient.ts` - Axios instance with base configuration
- `characterService.ts` - Character CRUD operations
- `diceService.ts` - Dice rolling endpoints
- `encounterService.ts` - Encounter generation endpoints
- `campaignService.ts` - Campaign management (Phase 2)

## Example

```typescript
// apiClient.ts
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

// Add request interceptor for auth tokens (future)
apiClient.interceptors.request.use((config) => {
  // Add auth header if token exists
  return config;
});

// Add response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);
```

```typescript
// diceService.ts
import { apiClient } from './apiClient';
import { DiceRollRequest, DiceRollResponse } from '../types/dice.types';

export const diceService = {
  roll: async (notation: string): Promise<DiceRollResponse> => {
    const response = await apiClient.post<DiceRollResponse>('/api/dice/roll', {
      notation,
    });
    return response.data;
  },

  rollWithAdvantage: async (): Promise<DiceRollResponse> => {
    const response = await apiClient.post<DiceRollResponse>(
      '/api/dice/roll/advantage'
    );
    return response.data;
  },

  getHistory: async (): Promise<DiceRollResponse[]> => {
    const response = await apiClient.get<DiceRollResponse[]>(
      '/api/dice/history'
    );
    return response.data;
  },

  clearHistory: async (): Promise<void> => {
    await apiClient.delete('/api/dice/history');
  },
};
```

## Usage

```typescript
import { diceService } from '../services/diceService';

const DiceRoller: React.FC = () => {
  const handleRoll = async () => {
    try {
      const result = await diceService.roll('1d20');
      console.log('Roll result:', result);
    } catch (error) {
      console.error('Roll failed:', error);
    }
  };

  return <button onClick={handleRoll}>Roll</button>;
};
```
