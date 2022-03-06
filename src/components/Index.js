import React, { useState } from "react";
import List from "./List";
import "./styles.css";
import GeoCoder from "./GeoCode";
import MapAPI from "./Map";

function Index() {
	const [inputText, setInputText] = useState("");

		let handleInput = (e) => {
			e.preventDefault()
			var lowerCase = e.target.value.toLowerCase();
			setInputText(lowerCase);
		};
		let handleSubmit = (e) => {
			e.preventDefault()
		}

	//input runs inputHandler function
	return (
		<React.Fragment>	
			<form  onSubmit={handleSubmit}>
			<GeoCoder user={inputText} />
			<input onChange={handleInput} type="text"></input>
			<input  type="submit"></input>
			<List location={inputText} />
			</form>
			
		
		</React.Fragment>
	);
}

export default Index;
