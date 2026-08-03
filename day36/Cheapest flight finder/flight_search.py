from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import requests

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("api_key")

        self.flight_endpoint = "https://serpapi.com/search"

        

    def run_flight_api(self, origin_city_code, destination_city_code, from_time, to_time):

        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.api_key,
        }

        response = requests.get(url=self.flight_endpoint, params= query)
        response.raise_for_status()
        data = response.json()

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        if "error" in data:
            print(f"API error: {data['error']}")
            return None

        return data

