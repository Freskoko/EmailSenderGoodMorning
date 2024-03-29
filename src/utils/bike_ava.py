from requests import get


def get_bike_info():

    url = "https://gbfs.urbansharing.com/bergenbysykkel.no/station_status.json"
    bike_data = get(url)
    bike_data = bike_data.json()

    greighallen_av = bike_data["data"]["stations"]

    for station in greighallen_av:

        if station["station_id"] == "3":
            return station["num_bikes_available"]

    return greighallen_av


if __name__ == "__main__":
    print(get_bike_info())
