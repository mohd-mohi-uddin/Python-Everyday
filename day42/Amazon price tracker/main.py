from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID= os.environ.get("ACCOUNT_SID")
AUTH_TOKEN= os.environ.get("AUTH_TOKEN")
MY_EMAIL= os.environ.get("MY_EMAIL")
MY_PASSWORD= os.environ.get("MY_PASSWORD")
SENDER_EMAIL= os.environ.get("SENDER_EMAIL")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")

product_url= "https://www.amazon.in/pricehistory.app/dp/B0CD1X6YDG?tag=cuelinkss26094-21&ascsubtag=20260813cl91pwokvsf6&th=1"

browser_headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

response= requests.get(url=product_url,headers=browser_headers)
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(contents,"html.parser")
price_of_product = int(soup.find(name= "span", class_= "a-price-whole").getText().split(".")[0])

my_price = 300

if my_price >= price_of_product:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password= MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs= SENDER_EMAIL,
                            msg= f"Face wash at {price_of_product} only!\n\nYour 'DERMA CO. Face Wash' is now at {price_of_product} only. Go buy it now!",
                            )

    client = Client(ACCOUNT_SID,AUTH_TOKEN)

    message = client.messages.create(
        body=f"Your 'DERMA CO. Face Wash' is now at {price_of_product} only. Go buy it now!",
        from_=TWILIO_VIRTUAL_NUMBER,
        to= TWILIO_VERIFIED_NUMBER
    )

    print(message.status)


