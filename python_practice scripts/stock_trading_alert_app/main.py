import requests
import os
import dotenv
from twilio.rest import Client

dotenv.load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

ACCOUNT_SID=os.getenv("TWILIO_SID")
ACCOUNT_AUTH_KEY=os.getenv("TWILIO_AUTH_KEY")

VIRTUAL_PHONE=os.getenv("TWILIO_PHONE")
VERIFIED_PHONE=os.getenv("ADDRESS_PHONE")

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY =os.getenv("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = ACCOUNT_SID
auth_token = ACCOUNT_AUTH_KEY

news_parameters ={
    "apiKey":NEWS_API_KEY,
    "qInTitle":COMPANY_NAME
}

stock_parameters ={
    "apikey": STOCK_API_KEY,
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME
}


stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

stock_data = stock_response.json()
daily_stock = stock_data["Time Series (Daily)"]
daily_closing = [value for (key, value) in daily_stock.items()]

yesterdays_close = daily_closing[0]["4. close"]
day_before_yesterday_close = daily_closing[1]["4. close"]

difference_percentage = round((abs(float(yesterdays_close) - float(day_before_yesterday_close)) / float(day_before_yesterday_close)) * 100, 2)

if difference_percentage > 1:
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()
    news_articles = news_data["articles"]
    top_three_news = news_articles[:3]

    formatted_articles_sms = [
        f"\n{STOCK_NAME}: {difference_percentage}%\nHeadline: {news['title']}.\nBrief: {news['description']}" for news in
        top_three_news]

    client = Client(account_sid, auth_token)
    for article in formatted_articles_sms:
        client.messages.create(
            body=article,
            from_=VIRTUAL_PHONE,
            to=VERIFIED_PHONE
        )

else:
    print("Dont get news")













