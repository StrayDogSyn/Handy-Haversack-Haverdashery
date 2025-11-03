import React, { useState } from 'react';
import { encounterApi, EncounterResult } from '../services/api';

const EncounterGenerator: React.FC = () => {
  const [partyLevel, setPartyLevel] = useState<number>(1);
  const [numPlayers, setNumPlayers] = useState<number>(4);
  const [difficulty, setDifficulty] = useState<string>('medium');
  const [result, setResult] = useState<EncounterResult | null>(null);
  const [generating, setGenerating] = useState(false);

  const difficulties = [
    { value: 'easy', label: 'Easy', color: 'bg-green-600' },
    { value: 'medium', label: 'Medium', color: 'bg-yellow-600' },
    { value: 'hard', label: 'Hard', color: 'bg-orange-600' },
    { value: 'deadly', label: 'Deadly', color: 'bg-red-600' },
  ];

  const handleGenerate = async () => {
    setGenerating(true);
    try {
      const encounterResult = await encounterApi.generate({
        party_level: partyLevel,
        num_players: numPlayers,
        difficulty: difficulty,
      });
      setResult(encounterResult);
    } catch (error) {
      console.error('Error generating encounter:', error);
    } finally {
      setGenerating(false);
    }
  };

  const getCRColor = (cr: number): string => {
    if (cr < 1) return 'text-green-400';
    if (cr < 5) return 'text-yellow-400';
    if (cr < 10) return 'text-orange-400';
    return 'text-red-400';
  };

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-amber-400">Encounter Generator</h2>

      <div className="bg-gray-800 rounded-lg p-6 space-y-6">
        {/* Party Level */}
        <div>
          <label className="block text-sm font-medium mb-2">Party Level</label>
          <div className="flex items-center gap-4">
            <input
              type="range"
              min="1"
              max="20"
              value={partyLevel}
              onChange={(e) => setPartyLevel(parseInt(e.target.value))}
              className="flex-1"
            />
            <input
              type="number"
              min="1"
              max="20"
              value={partyLevel}
              onChange={(e) => setPartyLevel(parseInt(e.target.value))}
              className="w-20 bg-gray-700 border border-gray-600 rounded px-3 py-2 text-center"
            />
          </div>
        </div>

        {/* Number of Players */}
        <div>
          <label className="block text-sm font-medium mb-2">Number of Players</label>
          <div className="flex items-center gap-4">
            <input
              type="range"
              min="1"
              max="8"
              value={numPlayers}
              onChange={(e) => setNumPlayers(parseInt(e.target.value))}
              className="flex-1"
            />
            <input
              type="number"
              min="1"
              max="12"
              value={numPlayers}
              onChange={(e) => setNumPlayers(parseInt(e.target.value))}
              className="w-20 bg-gray-700 border border-gray-600 rounded px-3 py-2 text-center"
            />
          </div>
        </div>

        {/* Difficulty */}
        <div>
          <label className="block text-sm font-medium mb-2">Difficulty</label>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
            {difficulties.map((diff) => (
              <button
                key={diff.value}
                onClick={() => setDifficulty(diff.value)}
                className={`p-3 rounded-lg transition-all ${
                  difficulty === diff.value
                    ? `${diff.color} text-white scale-105 shadow-lg`
                    : 'bg-gray-700 hover:bg-gray-600'
                }`}
              >
                <div className="font-semibold">{diff.label}</div>
              </button>
            ))}
          </div>
        </div>

        {/* Generate Button */}
        <button
          onClick={handleGenerate}
          disabled={generating}
          className={`w-full py-4 rounded-lg font-bold text-xl transition-all ${
            generating
              ? 'bg-gray-600 cursor-not-allowed'
              : 'bg-amber-600 hover:bg-amber-700 hover:scale-105 shadow-lg'
          }`}
        >
          {generating ? '⚔️ Generating...' : '⚔️ Generate Encounter'}
        </button>

        {/* Result Display */}
        {result && (
          <div className="space-y-4 pt-4 border-t border-gray-700">
            <div className="bg-gray-700 rounded-lg p-4">
              <div className="flex justify-between items-center">
                <span className="text-gray-400">Target CR:</span>
                <span className={`font-bold text-xl ${getCRColor(result.target_cr)}`}>
                  {result.target_cr.toFixed(1)}
                </span>
              </div>
              <div className="flex justify-between items-center mt-2">
                <span className="text-gray-400">Total Encounter CR:</span>
                <span className={`font-bold text-xl ${getCRColor(result.total_cr)}`}>
                  {result.total_cr.toFixed(1)}
                </span>
              </div>
            </div>

            <div>
              <h3 className="text-xl font-semibold mb-3 text-amber-300">Monsters</h3>
              <div className="space-y-3">
                {result.monsters.map((monster, index) => (
                  <div
                    key={`${monster.id}-${index}`}
                    className="bg-gray-700 rounded-lg p-4 hover:bg-gray-650 transition-colors"
                  >
                    <div className="flex justify-between items-start">
                      <div>
                        <h4 className="text-lg font-bold text-amber-200">{monster.name}</h4>
                        <p className="text-sm text-gray-400 capitalize">{monster.type}</p>
                      </div>
                      <div className={`text-xl font-bold ${getCRColor(monster.cr)}`}>
                        CR {monster.cr}
                      </div>
                    </div>
                    <div className="grid grid-cols-2 gap-4 mt-3">
                      <div className="flex items-center gap-2">
                        <span className="text-sm text-gray-400">HP:</span>
                        <span className="font-semibold text-red-400">{monster.hit_points}</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <span className="text-sm text-gray-400">AC:</span>
                        <span className="font-semibold text-blue-400">{monster.armor_class}</span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div className="bg-blue-900/30 border border-blue-700 rounded-lg p-4">
              <p className="text-sm text-blue-200">
                💡 <strong>Tip:</strong> Adjust monster HP or add environmental hazards to fine-tune
                the encounter difficulty.
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default EncounterGenerator;
