import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

NUTRITION_API_KEY = os.getenv("NUTRITION_API_KEY")
APP_ID = os.getenv("APP_ID")

print(APP_ID)
print(NUTRITION_API_KEY)

CALORIES_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
calories_config = {
    "query": input("what excersise you did?"),
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITION_API_KEY
}


response = requests.post(url= CALORIES_ENDPOINT, json= calories_config, headers= headers)
exercises= response.json()["exercises"]

now = datetime.now()
date = now.strftime("%d/%m/%Y") 
time = now.strftime("%X")

Sheety_endpoint = "https://api.sheety.co/4d8686b3cb0e7ec02e51afe4c3ddc9ca/workoutTracking/workouts"

for exercise in exercises:
    print(exercise)
    data = {
        "workout":{
            "date": date,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    response1 = requests.post(url=Sheety_endpoint, json= data)
    print(response1.text)

response2 = requests.get(Sheety_endpoint)
print(response2.json())

