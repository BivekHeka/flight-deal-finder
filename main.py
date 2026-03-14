import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

# -----------------SET-UP FLIGHT SEARCH--------------------
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()


# -----------------SET ORIGINAL AIRPORT----------------------

ORIGIN_CITY_IATA = "LON"

#------------UPDATE THE AIRPORT CODES IN GOOGLE SHEET-------------


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()


#--------------SEARCH FOR FLIGHTS-----------------------


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    print(f"Getting flights  for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time = tomorrow,
        to_time = six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: Rs{cheapest_flight.price}")
    time.sleep(2)




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


