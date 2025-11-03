import { useState } from 'react'
import DiceRoller from './components/DiceRoller'

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-800 to-slate-900">
      {/* Header */}
      <header className="bg-pathfinder-darkred shadow-lg">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-4xl font-bold text-pathfinder-gold font-serif">
            🎲 Handy Haversack Haverdashery
          </h1>
          <p className="text-pathfinder-lightgold mt-2">
            Your Pathfinder 2e Companion App
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Dice Roller */}
          <div className="bg-slate-700 rounded-lg shadow-xl p-6">
            <h2 className="text-2xl font-bold text-pathfinder-gold mb-4">
              Dice Roller
            </h2>
            <DiceRoller />
          </div>

          {/* Info Panel */}
          <div className="bg-slate-700 rounded-lg shadow-xl p-6">
            <h2 className="text-2xl font-bold text-pathfinder-gold mb-4">
              Welcome Adventurer!
            </h2>
            <div className="text-gray-200 space-y-3">
              <p>
                Welcome to the Handy Haversack Haverdashery, your all-in-one
                companion for Pathfinder 2e adventures!
              </p>
              <div className="bg-slate-600 rounded p-4 mt-4">
                <h3 className="font-bold text-pathfinder-lightgold mb-2">
                  Current Features:
                </h3>
                <ul className="list-disc list-inside space-y-1">
                  <li>Dice roller with full notation support</li>
                  <li>Character management (via API)</li>
                  <li>Encounter generator (via API)</li>
                  <li>Roll history tracking</li>
                </ul>
              </div>
              <div className="bg-slate-600 rounded p-4 mt-4">
                <h3 className="font-bold text-pathfinder-lightgold mb-2">
                  Coming Soon:
                </h3>
                <ul className="list-disc list-inside space-y-1">
                  <li>Character sheet interface</li>
                  <li>Initiative tracker</li>
                  <li>Spell database</li>
                  <li>Campaign management</li>
                </ul>
              </div>
              <div className="mt-4 p-4 bg-pathfinder-darkred rounded">
                <p className="text-sm text-pathfinder-lightgold">
                  🎲 <strong>Tip:</strong> Try rolling dice with notation like
                  "2d6+3", "1d20", or "4d8-1"
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* API Info */}
        <div className="mt-6 bg-slate-700 rounded-lg shadow-xl p-6">
          <h2 className="text-xl font-bold text-pathfinder-gold mb-3">
            API Documentation
          </h2>
          <p className="text-gray-300">
            View the full API documentation at:{' '}
            <a
              href="http://localhost:8000/docs"
              target="_blank"
              rel="noopener noreferrer"
              className="text-pathfinder-lightgold hover:text-pathfinder-gold underline"
            >
              http://localhost:8000/docs
            </a>
          </p>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-pathfinder-darkred mt-12 py-6">
        <div className="container mx-auto px-4 text-center text-pathfinder-lightgold">
          <p>Built for Pathfinder 2e by StrayDogSyn & Team</p>
          <p className="text-sm mt-2">
            "In the beginning, there was a d20..." - Gary Gygax (probably)
          </p>
        </div>
      </footer>
    </div>
  )
}

export default App
