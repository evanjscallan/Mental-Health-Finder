import React, { useState } from "react";
import List from "./List";
import "./styles.css";
import MapAPI from "./Map";
import Geocode from "react-geocode";
import CssBaseline from '@mui/material/CssBaseline';
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Box from '@mui/material/Box'
import Container from '@mui/material/Container'

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
		this.clickFind = this.clickFind.bind(this);
	}



	geoCodeMe = (event, data) => {
		var lowerCase = event.target.value.toLowerCase();
		this.setState({ setInputText: lowerCase });
		event.preventDefault();
		let loc = event.target.value;

		Geocode.setApiKey("AIzaSyDXdV2zeHYYqx6hOxAnDtcWml-EFWWQ40U");

		Geocode.fromAddress(loc).then((response) => {
			let geoLat = response.results[0].geometry.location.lat;
			let geoLng = response.results[0].geometry.location.lng;
			this.setState({
				lat: geoLat,
				lng: geoLng,
				address: data
			});
		});
	}

	clickFind(data) {
		console.log(data)
	}

	render() {
		const { handleInput, inputText, setInputText, lat, lng } = this.state;

		return (
			<React.Fragment>
			<div className='main'>
			
			
				<h1>Mental Health Resource Locator - California</h1>

				<form>
					<MapAPI latValue={Number(lat)} lngValue={Number(lng)} />
					<TextField
						id="outlined-basic"
						label="Location"
						variant="filled"
						size="small"
						onChange={(event) => this.geoCodeMe(event)}
					/>

					<Button size='large' variant="contained">Submit</Button>
					<List onChange func={this.clickFind} location={setInputText} />
				</form>
			
			</div>

			</React.Fragment>
		);
	}
}

//NEXT STEP:
//MAKE ONCLICK FOR EACH LIST ELEMENT
