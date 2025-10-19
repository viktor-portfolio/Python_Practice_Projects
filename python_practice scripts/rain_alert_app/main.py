import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

"""MAKE YOUR OWN .ENV FILE WITH SAME VAR NAMES"""
load_dotenv()
api_call = "https://api.openweathermap.org/data/2.5/forecast"

weather_api_key = os.getenv("WEATHER_API_KEY")
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_KEY")

parameters ={
    "lat": 47.497913,
    "lon": 19.040236,
    "cnt": 4,
    "appid": weather_api_key
}

response = requests.get(api_call, params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hourly_data in weather_data["list"]:
    condition_code = int(hourly_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if not will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body="Forget the umbrella, weather is g00d",
        from_=os.getenv("TWILIO_PHONE"),
        to=os.getenv("ADDRESS_PHONE")
    )
    print(message.status)