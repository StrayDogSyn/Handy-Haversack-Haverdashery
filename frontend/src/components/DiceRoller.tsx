import { useState } from 'react'
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

interface DiceRoll {
  notation: string
  rolls?: number[]
  modifier?: number
  total?: number
  result?: number
  type?: string
}

function DiceRoller() {
  const [notation, setNotation] = useState('2d6')
  const [result, setResult] = useState<DiceRoll | null>(null)
  const [history, setHistory] = useState<DiceRoll[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const rollDice = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await axios.post(`${API_URL}/dice/roll`, {
        notation: notation
      })
      setResult(response.data)
      // Add to history
      setHistory(prev => [response.data, ...prev].slice(0, 10))
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to roll dice')
    } finally {
      setLoading(false)
    }
  }

  const rollAdvantage = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await axios.post(`${API_URL}/dice/roll/advantage`)
      setResult(response.data)
      setHistory(prev => [response.data, ...prev].slice(0, 10))
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to roll with advantage')
    } finally {
      setLoading(false)
    }
  }

  const rollDisadvantage = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await axios.post(`${API_URL}/dice/roll/disadvantage`)
      setResult(response.data)
      setHistory(prev => [response.data, ...prev].slice(0, 10))
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to roll with disadvantage')
    } finally {
      setLoading(false)
    }
  }

  const quickRoll = (dice: string) => {
    setNotation(dice)
    setTimeout(() => {
      rollDice()
    }, 100)
  }

  return (
    <div className="space-y-4">
      {/* Input Section */}
      <div className="flex gap-2">
        <input
          type="text"
          value={notation}
          onChange={(e) => setNotation(e.target.value)}
          placeholder="e.g., 2d6+3"
          className="flex-1 px-4 py-2 bg-slate-600 text-white rounded border border-slate-500 focus:border-pathfinder-gold focus:outline-none"
          onKeyPress={(e) => e.key === 'Enter' && rollDice()}
        />
        <button
          onClick={rollDice}
          disabled={loading}
          className="px-6 py-2 bg-pathfinder-red hover:bg-pathfinder-darkred text-pathfinder-gold font-bold rounded transition disabled:opacity-50"
        >
          {loading ? '...' : 'Roll'}
        </button>
      </div>

      {/* Quick Roll Buttons */}
      <div className="flex flex-wrap gap-2">
        {['1d20', '1d12', '1d10', '1d8', '1d6', '1d4'].map(dice => (
          <button
            key={dice}
            onClick={() => quickRoll(dice)}
            className="px-3 py-1 bg-slate-600 hover:bg-slate-500 text-white rounded text-sm transition"
          >
            {dice}
          </button>
        ))}
      </div>

      {/* Advantage/Disadvantage */}
      <div className="flex gap-2">
        <button
          onClick={rollAdvantage}
          disabled={loading}
          className="flex-1 px-4 py-2 bg-green-700 hover:bg-green-600 text-white rounded transition disabled:opacity-50"
        >
          Advantage
        </button>
        <button
          onClick={rollDisadvantage}
          disabled={loading}
          className="flex-1 px-4 py-2 bg-red-700 hover:bg-red-600 text-white rounded transition disabled:opacity-50"
        >
          Disadvantage
        </button>
      </div>

      {/* Error Display */}
      {error && (
        <div className="p-3 bg-red-900 border border-red-700 rounded text-red-200">
          {error}
        </div>
      )}

      {/* Result Display */}
      {result && (
        <div className="p-6 bg-slate-800 rounded-lg border-2 border-pathfinder-gold">
          <div className="text-center">
            <div className="text-pathfinder-lightgold font-bold mb-2">
              {result.notation}
            </div>
            {result.rolls && (
              <div className="text-gray-400 mb-2">
                Rolls: {result.rolls.join(', ')}
                {result.modifier !== undefined && result.modifier !== 0 && (
                  <span> ({result.modifier > 0 ? '+' : ''}{result.modifier})</span>
                )}
              </div>
            )}
            <div className="text-5xl font-bold text-pathfinder-gold">
              {result.total !== undefined ? result.total : result.result}
            </div>
          </div>
        </div>
      )}

      {/* History */}
      {history.length > 0 && (
        <div>
          <h3 className="text-lg font-bold text-pathfinder-lightgold mb-2">
            Recent Rolls
          </h3>
          <div className="space-y-1 max-h-48 overflow-y-auto">
            {history.map((roll, idx) => (
              <div
                key={idx}
                className="px-3 py-2 bg-slate-600 rounded text-sm flex justify-between items-center"
              >
                <span className="text-gray-300">{roll.notation}</span>
                <span className="text-pathfinder-gold font-bold">
                  {roll.total !== undefined ? roll.total : roll.result}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default DiceRoller
