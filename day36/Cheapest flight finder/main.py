#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.4
import requests_cache
from flight_search import FlightSearch

requests_cache.install_cache(
    "flight_cache",
    expire_after=3600
)

from data_manager import DataManager
datamanager = DataManager()
flightsearch = FlightSearch()

