import { React, Component } from "react";
import mhDirectory from './../utils/CaMentalHealth.json'
import './styles.css'


function List(props) {
	//filters out of the directory by facility name if the input is not empty
	//lower case makes it easier
	//includes is a true or false statement so this means whether the input includes props.input (user input in this case run through function)
	const filteredData = mhDirectory.filter((el) => {
		if (props.input === '') {
			return el;
		}
		else {
			return el.Facility_Name.toLowerCase().includes(props.location)
		}
	})
	return (
		<div>
		<p>{props.location}</p>
		
		<ul>
		
		{filteredData.map((place) => (
			<div className='listItem' key={place.Record_ID}>
			<h2>{place.Facility_Name}</h2>
			<p>{place.Physical_Address}</p>
			<p>{place.Physical_City}, {place.Physical_State} {place.Physical_Zip} </p>
			<a href={place.Facility_Phone}>{place.Facility_Phone}</a>
			</div>			
			))}
		</ul>	

		</div>		
	)
}

export default List;