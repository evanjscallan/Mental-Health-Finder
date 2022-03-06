import React from "react";

import {
  GoogleMap,
  useJsApiLoader,
  Marker,
  LoadScript,
} from "@react-google-maps/api";

const containerStyle = {
  width: "800px",
  height: "400px",
};



const center = {
  lat: 35.1611,
  lng: 241.0522,
};

class MapAPI extends React.Component {
  render(lat, lng, props) {
    const onLoad = (marker) => {
      console.log("marker: ", marker);
    };
    const position = {
      lat: this.props.latValue,
      lng: this.props.lngValue,
    };



    return (
      <div>

        <LoadScript googleMapsApiKey="AIzaSyDXdV2zeHYYqx6hOxAnDtcWml-EFWWQ40U">
          <GoogleMap
            mapContainerStyle={containerStyle}
            center={center}
            zoom={3}
          >
            <Marker onLoad={onLoad} position={position} />

            {/* Child components, such as markers, info windows, etc. */}
            <></>
          </GoogleMap>
        </LoadScript>
      </div>
    );
  }
}

export default React.memo(MapAPI);
