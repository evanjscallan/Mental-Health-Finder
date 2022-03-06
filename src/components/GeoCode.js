import Geocode from "react-geocode";
import React from "react";
import MapAPI from "./Map";

//dummy data to pass to map

export default class GeoCoder extends React.Component {
  constructor(props) {
    super(props);
    
    this.state = {
      lat: "",
      lng: "",
      user: '' 
    };
  
  }

   

  //brings in the data for Geocoding
  //loc is the variable that will fill with actual data
  //need to recieve user input as props, 
  //affect the input on the Geocode side before sending
  componentDidMount(props) {
    let loc = String(this.state.user)
    console.log("YOU ARE RECIEVING: " + loc)
    Geocode.setApiKey("AIzaSyDXdV2zeHYYqx6hOxAnDtcWml-EFWWQ40U");
    Geocode.fromAddress(loc).then((response) => {
      let geoLat = response.results[0].geometry.location.lat;
      let geoLng = response.results[0].geometry.location.lng;
      this.setState({
        lat: geoLat,
        lng: geoLng,
        user: 'initial'
      });

    });
  }


  componentDidUpdate(prevProps, prevState){
    if (this.state.user !== prevState.user) {
      this.fetchData(this.state.user)
    }
  }

  //need to refactor so where data can travel 2 ways rather than:
  //Index --> GeoCoder --> Map
  //THIS.PROPS.USER IS WHAT WE NEED TO PASS INTO loc
  render(props) {
    console.log("CURRENT PROPS: " + this.props.user)

    return (
      <React.Fragment>
        <h1>{this.props.user}</h1>
        <h1>{this.state.lat}</h1>
        <h1>{this.state.lng}</h1>
        <MapAPI latValue={Number(this.state.lat)} lngValue={Number(this.state.lng)}/>
        <input type="submit"></input>
      </React.Fragment>
    );
  }
}
