import requests
from twilio.rest import Client
import os

api_key="f9ac4c9c403e24dce3fe7dd3b97997d9"
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]

PARAMETERS= {
    "lat": 17.344036,
    "lon": 78.461403,
    "appid": api_key,
    "cnt":4
}

response = requests.get(url= "https://api.openweathermap.org/data/2.5/forecast",params=PARAMETERS)
response.raise_for_status()
weather = response.json()

will_rain = False

for items in weather["list"]:
    weather_id= items["weather"][0]["id"]
    if weather_id < 700:
        will_rain= True

if will_rain:

    client = Client(account_sid,auth_token)

    message = client.messages.create(
        body="It will rain today, carry your umbrella. ",
        from_="+17407300618",
        to= "+917893409867"
    )

    print(message.status)
