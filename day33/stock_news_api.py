import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "use api key here"
NEWS_API_KEY= "use api key here"
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
symbol = None

url = 'https://www.alphavantage.co/query'
news_url = "https://newsapi.org/v2/everything"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
}
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}
response = requests.get(news_url, params=news_parameters)
news_data = response.json()

headline = news_data["articles"][0]["title"]
brief = news_data["articles"][0]["description"]

def send_mail(measure,symbol):

    client = Client(account_sid,auth_token)

    message = client.messages.create(
            body= f"{STOCK}: {symbol}{measure}% \nHeadline: {headline} \nBrief: {brief}",
            from_="+17407300618",
            to= "+917893409867"
    )

r = requests.get(url,params=parameters)
data = r.json()
print(data)

yesterday = (data["Time Series (Daily)"]["2026-07-24"]["4. close"])
yesterday= round(float(yesterday))

day_before_yesterday = (data["Time Series (Daily)"]["2026-07-23"]["4. close"])
day_before_yesterday= round(float(day_before_yesterday))

if day_before_yesterday > yesterday:
    loss = ((day_before_yesterday - yesterday)/day_before_yesterday)*100
    if loss >= 5:
        symbol = "🔻"
        send_mail(loss,symbol)
        print("messgae sent")
elif yesterday > day_before_yesterday:
    profit = ((yesterday-day_before_yesterday)/day_before_yesterday)*100
    if profit >= 5:
        symbol = "🔺"
        send_mail(profit,symbol)
        print("messgae sent")
