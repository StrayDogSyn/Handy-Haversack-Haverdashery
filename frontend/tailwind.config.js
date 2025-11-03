/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        pathfinder: {
          red: '#8B0000',
          gold: '#FFD700',
          darkred: '#5A0000',
          lightgold: '#FFF4B7',
        }
      },
      fontFamily: {
        serif: ['Georgia', 'serif'],
        fantasy: ['Papyrus', 'fantasy'],
      }
    },
  },
  plugins: [],
}
