module.exports = {
  content: ["./templates/**/*.html","./static/**/*.{js,css}"],
  theme: {
    extend: {
      colors: {
        brand: {
          50:  '#f5f3ff',
          100: '#ede9fe',
          500: '#7c3aed',
          700: '#5b21b6',
        }
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui'],
      }
    }
  },
  plugins: [ require('daisyui') ],
  daisyui: {
    themes: ['light', 'dark', {
      medmatch: {
        primary: '#7c3aed',
        'primary-focus': '#5b21b6',
        secondary: '#10b981',
        accent: '#f59e0b'
      }
    }]
  }
};
