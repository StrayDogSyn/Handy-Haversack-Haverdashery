import React, { useState } from 'react';
import { diceApi, DiceRollResult } from '../services/api';

const DiceRoller: React.FC = () => {
  const [diceType, setDiceType] = useState<number>(20);
  const [numDice, setNumDice] = useState<number>(1);
  const [modifier, setModifier] = useState<number>(0);
  const [result, setResult] = useState<DiceRollResult | null>(null);
  const [rolling, setRolling] = useState(false);

  const diceTypes = [4, 6, 8, 10, 12, 20, 100];

  const handleRoll = async () => {
    setRolling(true);
    try {
      const rollResult = await diceApi.roll({
        dice_type: diceType,
        num_dice: numDice,
        modifier: modifier,
      });
      setResult(rollResult);
    } catch (error) {
      console.error('Error rolling dice:', error);
    } finally {
      setTimeout(() => setRolling(false), 500);
    }
  };

  const getDiceIcon = (type: number): string => {
    const icons: { [key: number]: string } = {
      4: '⬥',
      6: '⬢',
      8: '◆',
      10: '◇',
      12: '◉',
      20: '◈',
      100: '◎',
    };
    return icons[type] || '●';
  };

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-amber-400">Dice Roller</h2>

      <div className="bg-gray-800 rounded-lg p-6 space-y-6">
        {/* Dice Selection */}
        <div>
          <label className="block text-sm font-medium mb-2">Dice Type</label>
          <div className="grid grid-cols-4 md:grid-cols-7 gap-2">
            {diceTypes.map((type) => (
              <button
                key={type}
                onClick={() => setDiceType(type)}
                className={`p-4 rounded-lg transition-all ${
                  diceType === type
                    ? 'bg-amber-600 text-white scale-105 shadow-lg'
                    : 'bg-gray-700 hover:bg-gray-600'
                }`}
              >
                <div className="text-2xl">{getDiceIcon(type)}</div>
                <div className="text-sm font-semibold">d{type}</div>
              </button>
            ))}
          </div>
        </div>

        {/* Number of Dice */}
        <div>
          <label className="block text-sm font-medium mb-2">Number of Dice</label>
          <div className="flex items-center gap-4">
            <input
              type="range"
              min="1"
              max="20"
              value={numDice}
              onChange={(e) => setNumDice(parseInt(e.target.value))}
              className="flex-1"
            />
            <input
              type="number"
              min="1"
              max="100"
              value={numDice}
              onChange={(e) => setNumDice(parseInt(e.target.value))}
              className="w-20 bg-gray-700 border border-gray-600 rounded px-3 py-2 text-center"
            />
          </div>
        </div>

        {/* Modifier */}
        <div>
          <label className="block text-sm font-medium mb-2">Modifier</label>
          <div className="flex items-center gap-4">
            <input
              type="range"
              min="-10"
              max="10"
              value={modifier}
              onChange={(e) => setModifier(parseInt(e.target.value))}
              className="flex-1"
            />
            <input
              type="number"
              min="-100"
              max="100"
              value={modifier}
              onChange={(e) => setModifier(parseInt(e.target.value))}
              className="w-20 bg-gray-700 border border-gray-600 rounded px-3 py-2 text-center"
            />
          </div>
        </div>

        {/* Roll Summary */}
        <div className="bg-gray-700 rounded-lg p-4 text-center">
          <div className="text-lg font-semibold">
            Rolling: {numDice}d{diceType}
            {modifier !== 0 && (
              <span className="text-amber-400">
                {' '}
                {modifier > 0 ? '+' : ''}
                {modifier}
              </span>
            )}
          </div>
        </div>

        {/* Roll Button */}
        <button
          onClick={handleRoll}
          disabled={rolling}
          className={`w-full py-4 rounded-lg font-bold text-xl transition-all ${
            rolling
              ? 'bg-gray-600 cursor-not-allowed'
              : 'bg-amber-600 hover:bg-amber-700 hover:scale-105 shadow-lg'
          }`}
        >
          {rolling ? '🎲 Rolling...' : '🎲 Roll Dice'}
        </button>

        {/* Result Display */}
        {result && (
          <div className="space-y-4 pt-4 border-t border-gray-700">
            <div className="text-center">
              <div className="text-sm text-gray-400 mb-2">Individual Rolls</div>
              <div className="flex flex-wrap justify-center gap-2">
                {result.rolls.map((roll, index) => (
                  <div
                    key={index}
                    className={`w-12 h-12 rounded-lg flex items-center justify-center font-bold text-lg ${
                      roll === diceType
                        ? 'bg-green-600 text-white'
                        : roll === 1
                        ? 'bg-red-600 text-white'
                        : 'bg-gray-700'
                    }`}
                  >
                    {roll}
                  </div>
                ))}
              </div>
            </div>

            <div className="bg-gray-700 rounded-lg p-6 space-y-2">
              <div className="flex justify-between text-lg">
                <span className="text-gray-400">Dice Total:</span>
                <span className="font-bold">{result.total}</span>
              </div>
              {result.modifier !== 0 && (
                <div className="flex justify-between text-lg">
                  <span className="text-gray-400">Modifier:</span>
                  <span className="font-bold text-amber-400">
                    {result.modifier > 0 ? '+' : ''}
                    {result.modifier}
                  </span>
                </div>
              )}
              <div className="flex justify-between text-2xl font-bold pt-2 border-t border-gray-600">
                <span className="text-amber-400">Final Result:</span>
                <span className="text-amber-400">{result.result}</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default DiceRoller;
