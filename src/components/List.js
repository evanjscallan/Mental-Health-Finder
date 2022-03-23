import { Component } from "react";
import React, { useState } from 'react'
import mhDirectory from "./../utils/CaMentalHealth.json";
import "./styles.css";
import Card from '@mui/material/Card'
import Box from '@mui/material/Box'
import Grid from '@mui/material/Grid'
import Collapse from '@mui/material/Collapse';
import CardContent from '@mui/material/CardContent'
import CardHeader from '@mui/material/CardHeader'
import Typography from '@mui/material/Typography';



export default class List extends React.Component {
	constructor(props){
		super(props);

	this.state = {
		clickData: ''
		}
	this.setClickedLocation = this.setClickedLocation.bind(this);
	}



	setClickedLocation(elementIndex, func){	
		this.setState({ clickedData: elementIndex })
		console.log("STATE: " + this.state.clickedData)
		this.props.func(this.state.clickedData)


	}

	
	//filters list based on facility name or physical address
	render() {
		let	filteredData = mhDirectory.filter((el) => {
		if (this.props.input === "") {
			return el;
		} else {
			return el.Facility_Name.toLowerCase().includes(this.props.location) 
			|| 
			el.Physical_Address.toLowerCase().includes(this.props.location);
		}
	});

	return (

		<div className='cards-container'>
		
			<p>{this.props.location}</p>

			<div>
			
				
				{filteredData.map((place, Physical_Address) => (
					<Card
						onClick={(elementIndex) => this.setClickedLocation(place.Physical_Address) }
						className='listItem'
						key={place.Record_ID}
					>
						<CardHeader
						title={place.Facility_Name}>
						</CardHeader>
						
						<CardContent>
						
						<p>{place.Physical_Address}</p>
						<p>
							{place.Physical_City}, {place.Physical_State}{" "}
							{place.Physical_Zip}{" "}
						</p>
						<a href={place.Facility_Phone}>
							{place.Facility_Phone}
						</a>
						</CardContent>
					
					</Card>

				))}
			
			</div>

		</div>
	);
}
}
export { mhDirectory };
