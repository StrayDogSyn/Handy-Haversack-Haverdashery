import React, { useState } from 'react';
import axios from 'axios';

interface DiceRollResult {
  expression: string;
  num_dice: number;
  die_size: number;
  modifier: number;
  rolls: number[];
  subtotal: number;
  total: number;
  note?: string;
}

const DiceRoller: React.FC = () => {
  const [expression, setExpression] = useState<string>('1d20');
  const [advantage, setAdvantage] = useState<boolean>(false);
  const [disadvantage, setDisadvantage] = useState<boolean>(false);
  const [result, setResult] = useState<DiceRollResult | null>(null);
  const [error, setError] = useState<string>('');
  const [history, setHistory] = useState<DiceRollResult[]>([]);

  const API_BASE_URL = 'http://localhost:8000/api';

  const rollDice = async () => {
    try {
      setError('');
      const response = await axios.post(`${API_BASE_URL}/dice/roll`, {
        expression,
        advantage,
        disadvantage,
      });
      
      setResult(response.data);
      setHistory([response.data, ...history].slice(0, 10)); // Keep last 10 rolls
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to roll dice');
    }
  };

  const quickRoll = (exp: string) => {
    setExpression(exp);
    setAdvantage(false);
    setDisadvantage(false);
  };

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6 text-pathfinder-red">Dice Roller</h1>
      
      {/* Quick Roll Buttons */}
      <div className="mb-6">
        <p className="text-sm text-gray-600 mb-2">Quick Roll:</p>
        <div className="flex flex-wrap gap-2">
          {['1d4', '1d6', '1d8', '1d10', '1d12', '1d20', '1d100', '2d6', '3d6', '4d6'].map((dice) => (
            <button
              key={dice}
              onClick={() => quickRoll(dice)}
              className="px-3 py-1 bg-pathfinder-brown text-white rounded hover:bg-opacity-80 transition"
            >
              {dice}
            </button>
          ))}
        </div>
      </div>

      {/* Main Roll Section */}
      <div className="bg-white rounded-lg shadow-md p-6 mb-6">
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Dice Expression
          </label>
          <input
            type="text"
            value={expression}
            onChange={(e) => setExpression(e.target.value)}
            placeholder="e.g., 1d20+5, 2d6"
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-pathfinder-red focus:border-transparent"
          />
        </div>

        {/* Advantage/Disadvantage (d20 only) */}
        {expression.toLowerCase().includes('d20') && (
          <div className="flex gap-4 mb-4">
            <label className="flex items-center">
              <input
                type="checkbox"
                checked={advantage}
                onChange={(e) => {
                  setAdvantage(e.target.checked);
                  if (e.target.checked) setDisadvantage(false);
                }}
                className="mr-2"
              />
              <span className="text-sm">Advantage</span>
            </label>
            <label className="flex items-center">
              <input
                type="checkbox"
                checked={disadvantage}
                onChange={(e) => {
                  setDisadvantage(e.target.checked);
                  if (e.target.checked) setAdvantage(false);
                }}
                className="mr-2"
              />
              <span className="text-sm">Disadvantage</span>
            </label>
          </div>
        )}

        <button
          onClick={rollDice}
          className="w-full bg-pathfinder-red text-white py-3 rounded-lg hover:bg-opacity-90 transition font-semibold text-lg"
        >
          🎲 Roll Dice
        </button>

        {error && (
          <div className="mt-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
            {error}
          </div>
        )}
      </div>

      {/* Result Display */}
      {result && (
        <div className="bg-gradient-to-br from-pathfinder-gold to-yellow-500 rounded-lg shadow-lg p-6 mb-6">
          <div className="text-center">
            <p className="text-sm text-gray-800 mb-2">{result.expression}</p>
            <div className="text-6xl font-bold text-pathfinder-red mb-2">
              {result.total}
            </div>
            <div className="text-sm text-gray-800">
              Rolled: [{result.rolls.join(', ')}]
              {result.modifier !== 0 && ` ${result.modifier >= 0 ? '+' : ''}${result.modifier}`}
            </div>
            {result.note && (
              <div className="mt-2 text-sm italic text-gray-700">
                {result.note}
              </div>
            )}
          </div>
        </div>
      )}

      {/* Roll History */}
      {history.length > 0 && (
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-xl font-semibold mb-4">Recent Rolls</h2>
          <div className="space-y-2">
            {history.map((roll, index) => (
              <div
                key={index}
                className="flex justify-between items-center p-3 bg-gray-50 rounded border border-gray-200"
              >
                <span className="text-sm text-gray-600">{roll.expression}</span>
                <span className="font-semibold text-lg">{roll.total}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default DiceRoller;
