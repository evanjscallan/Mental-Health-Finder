import Geocode from "react-geocode";
import React from "react";
import MapAPI from "./Map";
import { mhDirectory } from './List'

const allAddress =


console.log(mhDirectory[0].Physical_Address)
//dummy data to pass to map

export default class GeoCoder extends React.Component {
  constructor(props) {
    super(props);
    
    this.state = {
      lat1: "",
      lng1: "",
     
    };

  }

  //brings in the data for Geocoding.
  //loc is the variable that will fill with the user input data
  //need to recieve user input as props, 
  //affect the input on the Geocode side before sending
    componentDidMount(props) {
    let loc =  this.props.user

    console.log("YOU ARE RECIEVING: " + loc)
    Geocode.setApiKey("AIzaSyDXdV2zeHYYqx6hOxAnDtcWml-EFWWQ40U");
   
    Geocode.fromAddress(loc).then((response) => {
      const { geoLat, geoLng} = response.results[0].geometry.location.lat;
    
      this.setState({
        lat: geoLat,
        lng: geoLng,

      });

    });
  }


  //need to refactor so where data can travel 2 ways rather than:
  //Index --> GeoCoder --> Map
  //THIS.PROPS.USER IS WHAT WE NEED TO PASS INTO loc
  render(props) {


    return (
      <React.Fragment>
        <h1>{this.state.user}</h1>
        <h1>{this.state.lat}</h1>
        <h1>{this.state.lng}</h1>
        <MapAPI latValue={Number(this.state.lat)} lngValue={Number(this.state.lng)}/>
        <input type="submit"></input>
      </React.Fragment>
    );
  }
}
