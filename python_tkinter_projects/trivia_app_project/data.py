import requests

API_CALL = "https://opentdb.com/api.php"

api_parameters ={
    "amount" : 10,
    "type": "boolean"
}

response = requests.get(API_CALL, params=api_parameters)
response.raise_for_status()

data = response.json()
question_data = data["results"]
