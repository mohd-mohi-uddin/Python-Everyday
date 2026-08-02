import requests

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/4d8686b3cb0e7ec02e51afe4c3ddc9ca/flightsData/sheet1"
        self.response = requests.get(url=self.sheety_endpoint)
        self.fetch_data_from_sheety()

    def fetch_data_from_sheety(self):
        self.response.raise_for_status()
        flight_json = self.response.json()
        return flight_json
