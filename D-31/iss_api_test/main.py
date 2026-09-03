import requests 
from zoneinfo import ZoneInfo
from datetime import datetime
import smtplib
import time

my_email= "pythongmailtesting@gmail.com"
my_password = "dtsjvitqfsdhqhru"
MY_LATITUDE= 17.344089
MY_LONGITUDE= 78.461527
PARAMETERS= {
    "lat":MY_LATITUDE,
    "lng":MY_LONGITUDE,
    "formatted":0
}

def iss_is_up():
    response = requests.get(url= "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_longitude= float(response.json()["iss_position"]["longitude"])
    iss_latitude= float(response.json()["iss_position"]["latitude"])
    if MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE+5 and MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 :
        return True

def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json" ,params=PARAMETERS)
    response.raise_for_status()
    sunrise_ust= response.json()["results"]["sunrise"]
    sunrise_ist = datetime.fromisoformat(sunrise_ust).astimezone(
    ZoneInfo("Asia/Kolkata")
    )
    sunset_ust= response.json()["results"]["sunset"]
    sunset_ist = datetime.fromisoformat(sunset_ust).astimezone(
    ZoneInfo("Asia/Kolkata")
    )

    sunrise= sunrise_ist.hour
    sunset= sunset_ist.hour

    time_now= datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:

    time.sleep(60)

    if iss_is_up():
        print("ISS is nearby")
        if is_night():
            print("ISS is nearby")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                connection.sendmail(to_addrs="mohdmohiuddin1409@gmail.com",
                                    from_addr=my_email,
                                    msg="Subject:look upp in the sky!\n\nlook up in the sky ,the international space station is above your location"
                                    )
