// tailwind.config.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#60a5fa',      // Sky blue
          DEFAULT: '#3b82f6',    // Tailwind blue-500
          dark: '#1e40af',       // Deep navy
        },
        secondary: {
          light: '#f0abfc',      // Soft purple
          DEFAULT: '#d946ef',    // Violet
          dark: '#a21caf',       // Dark purple
        },
        accent: {
          DEFAULT: '#f59e0b',    // Amber
          light: '#fcd34d',
          dark: '#b45309',
        },
        neutral: {
          50: '#f9fafb',
          100: '#f3f4f6',
          200: '#e5e7eb',
          300: '#d1d5db',
          800: '#1f2937',
          900: '#111827',
        },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui'],
        heading: ['"DM Sans"', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
