import React, { useState, useEffect } from 'react';
import { characterApi, Character } from '../services/api';

const CharacterSheet: React.FC = () => {
  const [characters, setCharacters] = useState<Character[]>([]);
  const [selectedCharacter, setSelectedCharacter] = useState<Character | null>(null);
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState<Character>({
    name: '',
    character_class: '',
    level: 1,
    race: '',
    strength: 10,
    dexterity: 10,
    constitution: 10,
    intelligence: 10,
    wisdom: 10,
    charisma: 10,
    hit_points: 10,
    armor_class: 10,
  });

  useEffect(() => {
    loadCharacters();
  }, []);

  const loadCharacters = async () => {
    try {
      const chars = await characterApi.getAll();
      setCharacters(chars);
    } catch (error) {
      console.error('Error loading characters:', error);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      if (selectedCharacter?.id) {
        await characterApi.update(selectedCharacter.id, formData);
      } else {
        await characterApi.create(formData);
      }
      await loadCharacters();
      resetForm();
    } catch (error) {
      console.error('Error saving character:', error);
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('Are you sure you want to delete this character?')) {
      try {
        await characterApi.delete(id);
        await loadCharacters();
        if (selectedCharacter?.id === id) {
          resetForm();
        }
      } catch (error) {
        console.error('Error deleting character:', error);
      }
    }
  };

  const resetForm = () => {
    setFormData({
      name: '',
      character_class: '',
      level: 1,
      race: '',
      strength: 10,
      dexterity: 10,
      constitution: 10,
      intelligence: 10,
      wisdom: 10,
      charisma: 10,
      hit_points: 10,
      armor_class: 10,
    });
    setSelectedCharacter(null);
    setIsEditing(false);
  };

  const selectCharacter = (character: Character) => {
    setSelectedCharacter(character);
    setFormData(character);
    setIsEditing(true);
  };

  const calculateModifier = (score: number): string => {
    const modifier = Math.floor((score - 10) / 2);
    return modifier >= 0 ? `+${modifier}` : `${modifier}`;
  };

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-amber-400">Character Sheets</h2>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Character List */}
        <div className="lg:col-span-1 bg-gray-800 rounded-lg p-4">
          <h3 className="text-xl font-semibold mb-4 text-amber-300">Your Characters</h3>
          <div className="space-y-2">
            {characters.map((char) => (
              <div
                key={char.id}
                className={`p-3 rounded cursor-pointer transition-colors ${
                  selectedCharacter?.id === char.id
                    ? 'bg-amber-600 text-white'
                    : 'bg-gray-700 hover:bg-gray-600'
                }`}
                onClick={() => selectCharacter(char)}
              >
                <div className="font-semibold">{char.name}</div>
                <div className="text-sm opacity-75">
                  Level {char.level} {char.race} {char.character_class}
                </div>
              </div>
            ))}
            {characters.length === 0 && (
              <p className="text-gray-400 text-sm">No characters yet. Create one!</p>
            )}
          </div>
          <button
            onClick={() => {
              resetForm();
              setIsEditing(true);
            }}
            className="mt-4 w-full bg-amber-600 hover:bg-amber-700 text-white py-2 px-4 rounded transition-colors"
          >
            New Character
          </button>
        </div>

        {/* Character Form/Display */}
        <div className="lg:col-span-2 bg-gray-800 rounded-lg p-6">
          {isEditing ? (
            <form onSubmit={handleSubmit} className="space-y-4">
              <h3 className="text-xl font-semibold mb-4 text-amber-300">
                {selectedCharacter ? 'Edit Character' : 'New Character'}
              </h3>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium mb-1">Name</label>
                  <input
                    type="text"
                    value={formData.name}
                    onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">Class</label>
                  <input
                    type="text"
                    value={formData.character_class}
                    onChange={(e) => setFormData({ ...formData, character_class: e.target.value })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">Race</label>
                  <input
                    type="text"
                    value={formData.race}
                    onChange={(e) => setFormData({ ...formData, race: e.target.value })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    required
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">Level</label>
                  <input
                    type="number"
                    value={formData.level}
                    onChange={(e) => setFormData({ ...formData, level: parseInt(e.target.value) })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    min="1"
                    max="20"
                    required
                  />
                </div>
              </div>

              <div className="grid grid-cols-3 gap-4">
                <div>
                  <label className="block text-sm font-medium mb-1">STR</label>
                  <input
                    type="number"
                    value={formData.strength}
                    onChange={(e) => setFormData({ ...formData, strength: parseInt(e.target.value) })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    min="1"
                    max="30"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">DEX</label>
                  <input
                    type="number"
                    value={formData.dexterity}
                    onChange={(e) => setFormData({ ...formData, dexterity: parseInt(e.target.value) })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    min="1"
                    max="30"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">CON</label>
                  <input
                    type="number"
                    value={formData.constitution}
                    onChange={(e) => setFormData({ ...formData, constitution: parseInt(e.target.value) })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    min="1"
                    max="30"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">INT</label>
                  <input
                    type="number"
                    value={formData.intelligence}
                    onChange={(e) => setFormData({ ...formData, intelligence: parseInt(e.target.value) })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    min="1"
                    max="30"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">WIS</label>
                  <input
                    type="number"
                    value={formData.wisdom}
                    onChange={(e) => setFormData({ ...formData, wisdom: parseInt(e.target.value) })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    min="1"
                    max="30"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">CHA</label>
                  <input
                    type="number"
                    value={formData.charisma}
                    onChange={(e) => setFormData({ ...formData, charisma: parseInt(e.target.value) })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    min="1"
                    max="30"
                  />
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium mb-1">Hit Points</label>
                  <input
                    type="number"
                    value={formData.hit_points}
                    onChange={(e) => setFormData({ ...formData, hit_points: parseInt(e.target.value) })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    min="1"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">Armor Class</label>
                  <input
                    type="number"
                    value={formData.armor_class}
                    onChange={(e) => setFormData({ ...formData, armor_class: parseInt(e.target.value) })}
                    className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2"
                    min="1"
                  />
                </div>
              </div>

              <div className="flex gap-2">
                <button
                  type="submit"
                  className="flex-1 bg-amber-600 hover:bg-amber-700 text-white py-2 px-4 rounded transition-colors"
                >
                  Save Character
                </button>
                <button
                  type="button"
                  onClick={resetForm}
                  className="flex-1 bg-gray-600 hover:bg-gray-700 text-white py-2 px-4 rounded transition-colors"
                >
                  Cancel
                </button>
                {selectedCharacter && (
                  <button
                    type="button"
                    onClick={() => selectedCharacter.id && handleDelete(selectedCharacter.id)}
                    className="bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded transition-colors"
                  >
                    Delete
                  </button>
                )}
              </div>
            </form>
          ) : selectedCharacter ? (
            <div className="space-y-4">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="text-2xl font-bold text-amber-300">{selectedCharacter.name}</h3>
                  <p className="text-gray-400">
                    Level {selectedCharacter.level} {selectedCharacter.race} {selectedCharacter.character_class}
                  </p>
                </div>
                <button
                  onClick={() => setIsEditing(true)}
                  className="bg-amber-600 hover:bg-amber-700 text-white py-2 px-4 rounded transition-colors"
                >
                  Edit
                </button>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="bg-gray-700 rounded p-3 text-center">
                  <div className="text-sm text-gray-400">Hit Points</div>
                  <div className="text-2xl font-bold text-red-400">{selectedCharacter.hit_points}</div>
                </div>
                <div className="bg-gray-700 rounded p-3 text-center">
                  <div className="text-sm text-gray-400">Armor Class</div>
                  <div className="text-2xl font-bold text-blue-400">{selectedCharacter.armor_class}</div>
                </div>
              </div>

              <div className="grid grid-cols-3 gap-4">
                {[
                  { name: 'STR', value: selectedCharacter.strength },
                  { name: 'DEX', value: selectedCharacter.dexterity },
                  { name: 'CON', value: selectedCharacter.constitution },
                  { name: 'INT', value: selectedCharacter.intelligence },
                  { name: 'WIS', value: selectedCharacter.wisdom },
                  { name: 'CHA', value: selectedCharacter.charisma },
                ].map((stat) => (
                  <div key={stat.name} className="bg-gray-700 rounded p-3 text-center">
                    <div className="text-sm text-gray-400">{stat.name}</div>
                    <div className="text-xl font-bold">{stat.value}</div>
                    <div className="text-sm text-amber-400">{calculateModifier(stat.value)}</div>
                  </div>
                ))}
              </div>
            </div>
          ) : (
            <div className="text-center text-gray-400 py-12">
              Select a character or create a new one
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default CharacterSheet;
