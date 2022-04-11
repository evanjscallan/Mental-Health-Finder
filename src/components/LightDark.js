import React from 'react'
import { ThemeConsumer } from './../contexts/theme'
import './styles.css'



export default function LightDark() {
	return (
		<ThemeConsumer>
			{({ theme, toggleTheme }) => (
				<nav className='row space-between'>
					<button
						style={{fontSize:30}}
						className='btn-clear'
						onClick={toggleTheme}
						>
						{theme === 'light' ? '🔦' : '💡'}
					</button>
					</nav>
			)}
		</ThemeConsumer>
		)
}