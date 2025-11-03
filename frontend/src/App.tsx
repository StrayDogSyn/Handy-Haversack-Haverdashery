import React, { useState } from 'react';
import CharacterSheet from './components/CharacterSheet';
import DiceRoller from './components/DiceRoller';
import EncounterGenerator from './components/EncounterGenerator';
import './index.css';

function App() {
  const [activeTab, setActiveTab] = useState<'characters' | 'dice' | 'encounters'>('characters');

  const tabs = [
    { id: 'characters' as const, label: '📜 Characters', icon: '📜' },
    { id: 'dice' as const, label: '🎲 Dice Roller', icon: '🎲' },
    { id: 'encounters' as const, label: '⚔️ Encounters', icon: '⚔️' },
  ];

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Header */}
      <header className="bg-gray-800 border-b border-amber-600 shadow-lg">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-4xl font-bold text-amber-400 text-center">
            ⚔️ Pathfinder TTRPG Companion ⚔️
          </h1>
          <p className="text-center text-gray-400 mt-2">
            Character Management • Dice Rolling • Encounter Generation
          </p>
        </div>
      </header>

      {/* Navigation */}
      <nav className="bg-gray-800 border-b border-gray-700 sticky top-0 z-10">
        <div className="container mx-auto px-4">
          <div className="flex justify-center space-x-2 py-4">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`px-6 py-3 rounded-lg font-semibold transition-all ${
                  activeTab === tab.id
                    ? 'bg-amber-600 text-white shadow-lg scale-105'
                    : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {activeTab === 'characters' && <CharacterSheet />}
        {activeTab === 'dice' && <DiceRoller />}
        {activeTab === 'encounters' && <EncounterGenerator />}
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 border-t border-gray-700 mt-12">
        <div className="container mx-auto px-4 py-6 text-center text-gray-400">
          <p>Pathfinder TTRPG Companion • Built with FastAPI & React</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
