import requests, os
import datetime

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://test.api.amadeus.com/"

    def get_token(self):

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,                  # THIS IS THE API_KEY FOR THE APPLICATION
            "client_secret": API_SECRET            # THIS IS THE API_SECRET FOR THE APPLICATION
        }

        get_token = requests.post(
            f"{self.endpoint}v1/security/oauth2/token",
            headers=headers,
            data=data
        )
        self.TOKEN = f"Bearer {get_token.json()["access_token"]}"

    def find_IATA(self,keyword):
        self.get_token()
        print(f"Your token is {self.TOKEN}")
        code_endpoint = f"{self.endpoint}reference-data/locations/cities"
        code_params = {
            "keyword": keyword,
            "max": "2"
        }
        code_headers = {
            "Authorization": self.TOKEN
        }

        response = requests.get(
            url=code_endpoint,
            params=code_params,
            headers=code_headers)
        # self.airports = [item["iataCode"] for item in response.json()["data"] if "iataCode" in item]
        # print(self.airports)

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {keyword}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {keyword}.")
            return "Not Found"
        return code

    def check_flights(self, iata):
        self.get_token()
        flight_endpoint = f"{self.endpoint}v2/shopping/flight-offers"
        params = {
            "originLocationCode": "LON",
            "destinationLocationCode": iata,
            "departureDate": datetime.date.today() + datetime.timedelta(days=1),
            "returnDate": datetime.date.today() + datetime.timedelta(days=30),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "2"
        }
        headers = {
            "Authorization": self.TOKEN
        }

        response = requests.get(url=flight_endpoint,params=params,headers=headers)
        # print(response.json())

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()

