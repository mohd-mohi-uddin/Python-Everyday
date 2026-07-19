import smtplib
import random
import datetime as dt
from pathlib import Path

PARENT_DIR = Path(__file__).parent
with open(PARENT_DIR /"quotes.txt", mode="r") as data:
    quote_list= data.readlines()
    quote= random.choice(quote_list)
  
my_email= "pythongmailtesting@gmail.com"
my_password = "dtsjvitqfsdhqhru"

now = dt.datetime.now()
day_of_week= now.weekday()
if day_of_week == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mohdmohiuddin1409@gmail.com",
            msg=f"Subject:Quote of the day.\n\n{quote}"
            )

