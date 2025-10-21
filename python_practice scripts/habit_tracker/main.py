import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("ACCOUNT_USERNAME")
TOKEN = os.getenv("ACCOUNT_TOKEN")
GRAPH_IDENTIFICATION = os.getenv("GRAPH_ID")
GRAPH_NAME = os.getenv("GRAPH_DISPLAY_NAME")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
CREATE_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_IDENTIFICATION}"

update_delete_date = datetime(year=2025,month=7,day=23)
UPDATE_DELETE_PIXEL_ENDPOINT = f"{CREATE_PIXEL_ENDPOINT}/{update_delete_date.strftime('%Y%m%d')}"


create_quantity = "13.9"
update_quantity = "19.7"

headers ={
    "X-USER-TOKEN": TOKEN
}

# ________________________________ USER CREATION ________________________________ #

user_parameters ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#registration_response = requests.post(PIXELA_ENDPOINT, json=user_parameters)

# ________________________________ GRAPH CREATION ________________________________ #

graph_parameters ={
    "id": GRAPH_IDENTIFICATION,
    "name": GRAPH_NAME,
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

#graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_parameters, headers=headers)


# ________________________________ PIXEL CREATION ________________________________ #

today = datetime(year=2025,month=10,day=13)
create_pixel_parameters ={
    "date": today.strftime("%Y%m%d"),
    "quantity": create_quantity
}

# create_pixel_response = requests.post(url=CREATE_PIXEL_ENDPOINT,
#                                       json=create_pixel_parameters,
#                                       headers=headers)


# ________________________________ UPDATE PIXEL ________________________________ #

update_pixel_parameters ={
    "quantity": update_quantity
}

# update_pixel_response = requests.put(UPDATE_DELETE_PIXEL_ENDPOINT,
#                                      json=update_pixel_parameters,
#                                      headers=headers)


# ________________________________ DELETE PIXEL ________________________________ #

#delete_pixel_response = requests.delete(UPDATE_DELETE_PIXEL_ENDPOINT,headers=headers)


