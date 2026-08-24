import pandas
import datetime
from pathlib import Path
import smtplib
import random
BASE_DIR = Path(__file__).parent

with open(BASE_DIR /"letter_templates"/"letter_1.txt") as content:
    letter1 = content.read()

with open(BASE_DIR /"letter_templates"/"letter_2.txt") as content:
    letter2 = content.read()

with open(BASE_DIR /"letter_templates"/"letter_3.txt") as content:
    letter3 = content.read()

all_letters = [letter1,letter2,letter3]

my_email= "pythongmailtesting@gmail.com"
my_password = "dtsjvitqfsdhqhru"

df = pandas.read_csv(BASE_DIR /"birthdays.csv")
now = datetime.datetime.now()
for index,row in df.iterrows():
    if row.day == now.day and row.month == now.month:
        random_letter = random.choice(all_letters)
        letter = random_letter.replace("[NAME]",row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            print(letter)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Birthday Wish.\n\n{letter}"
                )






