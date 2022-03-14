import { Component } from "react";
import React from 'react'
import mhDirectory from "./../utils/CaMentalHealth.json";
import "./styles.css";
import Card from '@mui/material/Card'
import Box from '@mui/material/Box'
import Grid from '@mui/material/Grid'
import Collapse from '@mui/material/Collapse';
import CardContent from '@mui/material/CardContent'
import CardHeader from '@mui/material/CardHeader'
import Typography from '@mui/material/Typography';



function List(props) {
	
	//filters out of the directory by facility name if the input is not empty
	//lower case makes it easier
	//includes is a true or false statement so this means whether the input includes props.input (user input in this case run through function)
	const filteredData = mhDirectory.filter((el) => {
		if (props.input === "") {
			return el;
		} else {
			return el.Facility_Name.toLowerCase().includes(props.location);
		}
	});

	//passes clicked card data back up to index to plot marker
	function handleClick(elementIndex, func) {
		props.func(elementIndex)
	}
	return (

		<div className='cards-container'>
		
			<p>{props.location}</p>

			<div>
				
				{filteredData.map((place, Physical_Address) => (
					<Card
						onClick={(e) => handleClick(place.Physical_Address)}
						className='listItem '
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

export default List;
export { mhDirectory };
