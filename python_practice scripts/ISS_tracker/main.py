import requests
import smtplib
from datetime import datetime

MY_LAT = 47.497913
MY_LONG = 19.040236
ISS_NOW_API_CALL = "http://api.open-notify.org/iss-now.json"
SUNSET_SUNRISE_API_CALL = "https://api.sunrise-sunset.org/json"

my_email = ""
my_password = ""
to_address_email = ""

def is_iss_overhead():
    response = requests.get(url=ISS_NOW_API_CALL)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT + 5 >= iss_latitude >= MY_LAT -5 and MY_LONG + 5 >= iss_longitude >= MY_LONG -5:
        return True

def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url=SUNSET_SUNRISE_API_CALL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now_hour = datetime.now().hour

    if time_now_hour >= sunset or time_now_hour <= sunrise:
        return True

if is_night_time() and is_iss_overhead():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_address_email,
                            msg="Subject:ISS_ABOVE\n\nLOOK UP!")




