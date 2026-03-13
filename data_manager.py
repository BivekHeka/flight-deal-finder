import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_USER = os.getenv("SHEETY_USER")
SHEETY_PASS = os.getenv("SHEETY_PASS")
SHEETY_ENDPOINT= os.getenv("SHEETY_ENDPOINT")

class DataManager:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        self.destination_data = []

# Get all rows from googlesheet
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT,headers=self.headers)
        print(response.text)

        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(
                url = f"{SHEETY_ENDPOINT}/{city['id']}",
                json = new_data,
                headers = self.headers
            )
        print(response.text)