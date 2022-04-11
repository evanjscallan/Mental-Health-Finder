import React from "react";
import mhDirectory from "./../utils/CaMentalHealth.json";
import "./styles.css";
import Card from "@mui/material/Card";
import Box from "@mui/material/Box";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import Typography from "@mui/material/Typography";
import { ThemeConsumer } from "./../contexts/theme";

export default class List extends React.Component {
	constructor(props) {
		super(props);
		this.setClickedLocation = this.setClickedLocation.bind(this);
	}
	//sends up to parent
	setClickedLocation(elementIndex, func) {
		this.props.func(elementIndex);
	}

	//filters list based on facility name, physical address, city, or zip code
	render() {
		let filteredData = mhDirectory.filter((el) => {
			if (this.props.input == "") {
				return el;
			} else {
				return (
					el.Facility_Name.toLowerCase().includes(
						this.props.location
					) ||
					el.Physical_Address.toLowerCase().includes(
						this.props.location
					) ||
					el.Physical_City.toLowerCase().includes(
						this.props.location
					) ||
					String(el.Physical_Zip).includes(this.props.location)
				);
			}
		});
		if (filteredData.length == 0) {
			return (
				<div className="noResults">
					<p>No results found.</p>
				</div>
			);
		}

		const columns = [
			{ field: "id", headerName: "ID", width: 90 },
			{
				field: "facilityName",
				header: "Facility Name",
				width: 150,
			},
		];

		return (
			<ThemeConsumer>
				{({ theme }) => (
					<table className={`cards-container`}>
						<td>
							{filteredData.map(
								(
									place,
									Physical_Address,
									Physical_Zip,
									Physical_City,
									Physical_State
								) => (
									<Card
										sx={{
											maxWidth: "300px",
											minWidth: "300px",
											boxShadow:
												"1px 1px 3px 2px rgba(0,0,0,0.3)",
										}}
										onClick={(elementIndex) =>
											this.setClickedLocation(
												`${
													place.Physical_Address +
													" " +
													place.Physical_City +
													"," +
													place.Physical_State +
													" " +
													place.Physical_Zip
												}`
											)
										}
										className="listItem ctr-text"
										key={place.Record_ID}
									>
										<CardHeader
											title={place.Facility_Name}
										></CardHeader>

										<CardContent>
											<address>
												<p>{place.Physical_Address}</p>
												<p>
													{place.Physical_City},{" "}
													{place.Physical_State}{" "}
													{place.Physical_Zip}{" "}
												</p>
												{/* href phone number reformatted for mobile compatibility*/}
												<a
													href={`tel:${place.Facility_Phone.replaceAll(
														"-",
														""
													)
														.replaceAll("(", "")
														.replaceAll(")", "")
														.replaceAll(" ", "")}`}
												>
													{place.Facility_Phone}
												</a>
												<p>
													Target Population:{" "}
													{place.Target_Population}
												</p>
											</address>
										</CardContent>
									</Card>
								)
							)}
						</td>
					</table>
				)}
			</ThemeConsumer>
		);
	}
}
export { mhDirectory };