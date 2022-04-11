import React, { useState } from "react";
import List from "./List";
import "./styles.css";
import MapAPI from "./Map";
import Geocode from "react-geocode";

import CssBaseline from "@mui/material/CssBaseline";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import FormControl from "@mui/material/FormControl";
import InputAdornment from "@mui/material/InputAdornment";
import PropTypes from "react";

import { ThemeConsumer } from "./../contexts/theme";

export default class FrontPage extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			inputText: "",
			setInputText: "",
			lat: 32.8370564,
			lng: -116.7685666,
		};
		this.geoCodeMe = this.geoCodeMe.bind(this);
		this.listFilter = this.listFilter.bind(this);
	}

	//Responds to user card click - requires defaultProps
	geoCodeMe = (data) => {
		let loc = data;
		Geocode.setApiKey("AIzaSyDXdV2zeHYYqx6hOxAnDtcWml-EFWWQ40U");
		Geocode.fromAddress(loc).then((response) => {
			let geoLat = response.results[0].geometry.location.lat;
			let geoLng = response.results[0].geometry.location.lng;
			this.setState({
				lat: geoLat,
				lng: geoLng,
			});
		});
	};

	//take the list Filter input and sets state based on the input
	listFilter(event) {
		var lowerCase = event.target.value.toLowerCase();
		this.setState({ setInputText: lowerCase });
		event.preventDefault();
	}

	render() {
		const { handleInput, inputText, setInputText, lat, lng } = this.state;

		return (
			<React.Fragment>
				<ThemeConsumer>
					{({ theme }) => (
						<div className="main">
							<h1 className="main-text">
								Mental Health Resource Locator - California
							</h1>
							<MapAPI
								latValue={Number(lat)}
								lngValue={Number(lng)}
							/>

							<p className="margin-bottom descriptionText">
								<strong>
									Find a location near you (click on result to
									display on map).
								</strong>
							</p>

							<form>
								<TextField
									sx={{
											marginLeft: '2rem',
											backgroundColor: 'white'
										}}
									id="outlined-basic-adornment"
									label="Enter Location..."
									size="large"
									variant="filled"
									onChange={(event) => this.listFilter(event)}
									InputProps={{
										startAdornment: (
											<InputAdornment position="start"></InputAdornment>
										),
									}}
								/>
								<List
									func={this.geoCodeMe}
									location={setInputText}
								/>
							</form>
						</div>
					)}
				</ThemeConsumer>
			</React.Fragment>
		);
	}
}

FrontPage.defaultProps = {
	data: "2120 Alpine Boulevard",
	setInputText: String,
};