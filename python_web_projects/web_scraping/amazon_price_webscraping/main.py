import smtplib
import requests
from bs4 import BeautifulSoup
import dotenv
import os

dotenv.load_dotenv()

email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")
address_email = os.getenv("TO_SEND_EMAIL")

AMAZON_PRACTICE_URL = ""

response = requests.get(AMAZON_PRACTICE_URL)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "html.parser")

rice_cooker_price = float(soup.find("span", class_="aok-offscreen").getText().replace("$", ""))

if rice_cooker_price <= 99.99:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=address_email,
                            msg=f"Your rice cooker is now available in the affordable price\n"
                                f"Here is the website: {AMAZON_PRACTICE_URL}")