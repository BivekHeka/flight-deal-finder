import time
from data_manager import DataManager
from flight_search import FlightSearch

# -----------------SET-UP FLIGHT SEARCH--------------------
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()


#------------UPDATE THE AIRPORT CODES IN GOOGLE SHEET-------------


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()





# import requests
# from datetime import datetime
# import os 
# from dotenv import load_dotenv

# # Load variables from .env
# load_dotenv()




# SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
# SHEETY_USER = os.getenv("SHEETY_USER")
# SHEETY_PASS = os.getenv("SHEETY_PASS")
# SHEETY_ENDPOINT= os.getenv("SHEETY_ENDPOINT")


# headers = {
#     "Authorization": f"Bearer {SHEETY_TOKEN}"
# }

# sheet_response = requests.post(SHEETY_ENDPOINT, headers=headers)
# print(sheet_response.text)


