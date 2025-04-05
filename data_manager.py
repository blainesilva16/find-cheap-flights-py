import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, flight_search):
        self.endpoint = f"https://api.sheety.co/{my_sheet_id}/flightDeals/prices"
        self.flight_search = flight_search

        # ------------------- I RAN THIS FUNCTION ONCE TO FILL THE IATA CODE FOR EACH COUNTRY IN "Copy of Flight Deals" file
        # ------------------- EXECUTE IT AGAIN IF THE GOOGLE SHEETS FILE IS A NEW ONE
        # self.fill_iata()

        response = requests.get(url=self.endpoint)
        self.sheety_prices = response.json()["prices"]
        self.flights = []
        self.get_cheaper_flights()
        # self.sheety_prices = [
        #     {'city': 'Paris','iataCode': 'PAR','lowestPrice': 170,'id': 2},
        #     {'city': 'Frankfurt','iataCode': 'FRA','lowestPrice': 285,'id': 3},
        #     {'city': 'Tokyo','iataCode': 'TYO','lowestPrice': 1263,'id': 4},
        #     {'city': 'Hong Kong','iataCode': 'HKG','lowestPrice': 890,'id': 5},
        #     {'city': 'Istanbul','iataCode': 'IST','lowestPrice': 152,'id': 6},
        #     {'city': 'Kuala Lumpur','iataCode': 'KUL','lowestPrice': 847,'id': 7},
        #     {'city': 'New York','iataCode': 'NYC','lowestPrice': 414,'id': 8},
        #     {'city': 'San Francisco','iataCode': 'SFO','lowestPrice': 799,'id': 9},
        #     {'city': 'Dublin','iataCode': 'DBN','lowestPrice': 378,'id': 10
        #     }]

        # HERE COMES THE ARRAY WITH THE BIG JSON RESPONSE, I REMOVED SOME PARTS
        # self.flights = [
        #     {'meta': ... 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=LON&destinationLocationCode=DBN&departureDate=2025-04-06&returnDate=2025-05-05&adults=1&nonStop=true&currencyCode=GBP&max=2'}}, 'data': []}
        # ]

    def fill_iata(self):
        for i in range (0, len(self.sheety_prices)):
            iata = self.flight_search.find_IATA(self.sheety_prices[i]["city"])
            body = {
                "price": {
                    "iataCode": iata
                }
            }
            response_iata = requests.put(url=f"{self.endpoint}/{i+2}", json=body)
            print(response_iata.json())

    def get_cheaper_flights(self):
        for item in self.sheety_prices:
            self.flights.append(self.flight_search.check_flights(item["iataCode"]))
