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
import FormControl from "@mui/material/FormControl"
import InputAdornment from "@mui/material/InputAdornment"


export default class Index extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
			inputText: "",
			setInputText: "",
			lat: 0,
			lng: 0,
		};
		this.geoCodeMe = this.geoCodeMe.bind(this);
		this.listFilter = this.listFilter.bind(this);
	}
	//Responds to user card click
	geoCodeMe = (data) => {
		console.log(data);
		let loc = data;
		console.log("LOC = " + loc);

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

	listFilter(event) {
		var lowerCase = event.target.value.toLowerCase();
		this.setState({ setInputText: lowerCase });
		event.preventDefault();
	}

	render() {
		const { handleInput, inputText, setInputText, lat, lng } = this.state;

		return (
			<React.Fragment>
				<div className="main">
					<h1>Mental Health Resource Locator - California</h1>

					<form>
						<MapAPI latValue={Number(lat)} lngValue={Number(lng)} />
						 <FormControl sx={{ m: 1, width: '25ch' }} variant="standard">
						 <p>Find a location near you (click on location to display on map)</p>
						<TextField
							id="outlined-basic-adornment"
							label="Enter Location..."
							size="small"
							variant="filled"
							onChange={(event) => this.listFilter(event)}
							InputProps={{
							            startAdornment: <InputAdornment position="start"></InputAdornment>,
							          }}
						/>
						</FormControl>

						<List func={this.geoCodeMe} location={setInputText} />
					</form>
				</div>
			</React.Fragment>
		);
	}
}

Index.defaultProps = {
	data: "",
};

//NEXT STEP:
//MAKE ONCLICK FOR EACH LIST ELEMENT