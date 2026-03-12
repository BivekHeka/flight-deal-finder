from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
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


