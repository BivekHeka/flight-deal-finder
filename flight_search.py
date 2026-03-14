# import requests
# from datetime import datetime
# import os
# from dotenv import load_dotenv

# load_dotenv()

# IATA_ENDPOINT = "ahiley site ma free registration banda gareko xa"
# FLIGHT_ENDPOINT = "ahiley site ma free registration banda gareko xa"
# TOKEN_ENDPOINT = "ahiley site ma free registration banda gareko xa"

# class FlightSearch :

#     def __init__(self):
#         self._api_key = os.environ["AMADEUS_API_KEY"]
#         self._api_secret = os.environ["AMADEUS_SECRET"]
#         self._token = self._get_new_token()

#     def _get_new_token(self):
#         header = {
#             'Content-Type' : 'application/x-www-form-urlencoded'
#         }
#         body = {
#             'grant_type' : 'client_credentials',
#             'client_id' : self._api_key,
#             'client_secret' : self._api_secret
#         }
#         response = requests.post(url=TOKEN_ENDPOINT, headers= header, data=body)
#         print(f"your token is {response.json()['access_token']}")
#         print(f"Your token expires in {response.json()['expire_in']} seconds")
#         return response.json()['access_token']

#     def get_destination_code(self, city_name):
#         print(f"Using this token to get destination {self._token}")
#         headers = {"Authorization": f"Bearer {self._token}"}
#         query = {
#             "keyword": city_name,
#             "max": "2",
#             "include": "AIRPORTS",

#         }
#         response = requests.get(
#             url=IATA_ENDPOINT,
#             headers=headers,
#             params= query
#         )

#         print(f"Status code {response.status_code}. Airport IATA: {response.text}")
#         try:
#             code= response.json()["data"][0]['iataCode']
#         except IndexError:
#             print(f"IndexError: No airport code found for {city_name}.")
#             return "N/A"
#         except KeyError:
#             print(f"KeyError: No airport code found for {city_name}.")
#             return "Not Found"
#         return code



class FlightSearch:

    def get_destination_code(self, city_name):

        iata_codes = {
            "Paris": "PAR",
            "Frankfurt": "FRA",
            "Tokyo": "TYO",
            "Hong Kong": "HKG",
            "Istanbul": "IST",
            "Kuala Lumpur": "KUL",
            "New York": "NYC",
            "San Francisco": "SFO",
            "Dublin": "DUB"
        }

        return iata_codes.get(city_name, "N/A")