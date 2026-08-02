from flight_data import FlightData


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.city_names()

    def city_names(self):
        flightdata = FlightData()
        data = flightdata.fetch_data_from_sheety()
        data_list = data["sheet1"]
        for city in data_list:
            city_name = city["city"]
            print(city_name)
        
