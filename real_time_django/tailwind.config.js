/** @type {import('tailwindcss').Config} */
module.exports = {
	darkMode: 'class',
	content: [
		'./templates/**/*.html',
		'./templates/**/**/*.html',
		'./templates/**/**/**/*.html',
		'./node_modules/flowbite/**/*.js',
		// app templates
		'../app_documents/templates/**/*.html'
	],
	theme: {

		extend: {

		},
		extend: {
			colors: {
				transparent: 'transparent',
				current: 'currentColor',
				'white': '#ffffff',
				'tahiti': {
					100: '#cffafe',
					200: '#a5f3fc',
					300: '#67e8f9',
					400: '#22d3ee',
					500: '#06b6d4',
					600: '#0891b2',
					700: '#0e7490',
					800: '#155e75',
					900: '#164e63',
				},
				'palette': {
					'dark': '#000e11',
					'navy': '#1b3f44',
					'rose': '#ba9484',
					'sand': '#c2bf96',
					'light': '#e0e0c9'
				}
			},
		},
	},
	plugins: [
		require('flowbite/plugin'),
		require('@tailwindcss/forms')
	],
}


