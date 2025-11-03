/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        pathfinder: {
          red: '#8B0000',
          gold: '#FFD700',
          brown: '#8B4513',
        }
      }
    },
  },
  plugins: [],
}
