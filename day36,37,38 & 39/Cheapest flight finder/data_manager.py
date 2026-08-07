import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:
 
    def __init__(self):

        self._sheet1_endpoint = os.environ.get("SHEETY_sheet1_ENDPOINT")
        self._users_endpoint = os.environ.get("SHEETY_users_ENDPOINT")
        self._user = os.environ.get("SHEETY_USERNAME")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self._sheet1_endpoint, auth=self._authorization)
        data = response.json()
        print(data)
        self.destination_data = data["sheet1"]
        return self.destination_data

    def get_customer_emails(self):
        response = requests.get(url=self._users_endpoint, auth=self._authorization)
        data = response.json()
        print(data)
        self.user_data = data["users"]
        return self.user_data

    
    # ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        
        new_data = {
            "sheet1": {
                "prices": new_price
            }
        }
        response = requests.put(
            url=f"{self._sheet1_endpoint}/{row_id}",
            json=new_data,
            auth=self._authorization
            
        )
        print(response.status_code)
        print(response.text)
