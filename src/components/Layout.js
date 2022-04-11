import React from "react";
import { ThemeProvider } from "./../contexts/theme";
import FrontPage from "./FrontPage";
import LightDark from "./LightDark";
import "./styles.css";

export default class Layout extends React.PureComponent {
	constructor(props) {
		super(props);
		this.state = {
			theme: "light",
			toggleTheme: () => {
				this.setState(({ theme }) => ({
					theme: theme === "light" ? "dark" : "light",
				}));
			},
		};
	}

	render() {
		return (
			<ThemeProvider value={this.state}>
				<div className={this.state.theme}>
					<LightDark />
					<FrontPage />
				</div>
			</ThemeProvider>
		);
	}
}
