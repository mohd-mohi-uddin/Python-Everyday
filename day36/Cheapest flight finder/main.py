#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.4
import requests_cache
from flight_search import FlightSearch
from datetime import datetime, timedelta
from data_manager import DataManager

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

datamanager = DataManager()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

flight_search = FlightSearch()

flights = flight_search.run_flight_api("LHR","CDG",tomorrow,six_month_from_today)

print(flights)