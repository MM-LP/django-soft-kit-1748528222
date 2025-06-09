/** @type {import('tailwindcss').Config} */

module.exports = {
  prefix: 'tw-',
  mode: 'jit',  // This enables fast updates
  content: [
    './templates/**/*.html',               // for top-level templates/
    './**/templates/**/*.html',            // for app-level templates/
    './**/*.py',                            // optional, if using Tailwind in Python strings
    './static/src/**/*.{js,ts,jsx,tsx}',   // if using JS/TS components

  ],
  theme: {
    extend: {
      animation: {
        'spin-3s': 'spin 3s linear infinite',
        'breath': 'breath 8s ease-in-out infinite both',
      },
      keyframes: {
        spin: {
          to: { transform: 'rotate(360deg)' },
        },
        breath: {
          '0%, 100%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.05)' },
        }
      }
    },
  }, 

};


