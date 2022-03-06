import React from 'react'
import { Map, GoogleApiWrapper, Marker} from 'google-maps-react';
import GooglePlacesAutocomplete from 'react-google-places-autocomplete';

const mapStyles = {
	width: '50%',
	height: '50%',
}


export class MapsAPI extends React.Component{
	constructor(props){
		super(props)
		this.state = {
			loaded: true,
		}
}
	componentDidUpdate(prevProps, prevState) {
		if (prevProps.google !== this.props.google) {
			this.loadMap()
		}
	}

	loadMap() {
		return null
	}


	render() {
		var map;
		var service;
		var infowindow;
		const loaded = this.state.loaded
		if (!loaded) {
			return <div>Loading...</div>
		}
		return(
			<React.Fragment>
        <Map
			google={this.props.google}
			zoom={8}
			style={mapStyles}
			initialCenter={{ lat: 32.7767, lng:-96.7970}}
			>
			<Marker position={{lat: 32.7767, lng:-96.7970}}/>
		</Map>
		
		</React.Fragment>
			)
	}
}

export default GoogleApiWrapper({
  apiKey: 'AIzaSyDXdV2zeHYYqx6hOxAnDtcWml-EFWWQ40U'
})(MapsAPI);