from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import requests

load_dotenv()

TOMORROW = (datetime.now()+timedelta(days = 1)).strftime("%Y-%m-%d")
DATE_SIX_MONTHS_LATER = (datetime.now()+timedelta(days = 180)).strftime("%Y-%m-%d")
TODAY = datetime.now().strftime("%Y-%m-%d")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("api_key")

        self.flight_endpoint = "https://serpapi.com/search"
        self.parameters = {
            "engine": "google_flights",
            "departure_id": "LON",
            "arrival_id": "TOK",
            "outbound_date": TOMORROW,
            "return_date": DATE_SIX_MONTHS_LATER, 
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.api_key,
            }
        self.run_flight_api()

    def run_flight_api(self):
        response = requests.get(url=self.flight_endpoint, params= self.parameters)
        print(response.status_code)
        print(response.json())

