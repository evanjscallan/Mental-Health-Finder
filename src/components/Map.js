import React from "react";
import "./styles.css";


import {
  GoogleMap,
  useJsApiLoader,
  Marker,
  LoadScript,
} from "@react-google-maps/api";

const containerStyle = {
  width: "100%",
  height: "30rem",
};


const center = {
  lat: 36.5611,
  lng: 241.0522,
};

class MapAPI extends React.Component {
  render(lat, lng, props) {
  
    const position = {
      lat: this.props.latValue,
      lng: this.props.lngValue,
    };



    return (
      <div className='map'>
      

        <LoadScript googleMapsApiKey="AIzaSyDXdV2zeHYYqx6hOxAnDtcWml-EFWWQ40U">
        
          <GoogleMap
            mapContainerStyle={containerStyle}
            center={center}
            zoom={5.5}
          >

            <Marker position={position} />

            {/* Child components, such as markers, info windows, etc. */}
            <></>
          </GoogleMap>
       
        </LoadScript>
      
      </div>
    );
  }
}

export default React.memo(MapAPI);

/*
  const onLoad = (marker) => {
      console.log("marker: ", marker);
    }; */