class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,sheety_prices, data_flights):
        self.sheety_prices = sheety_prices
        self.flights = data_flights
        self.flight_info = []
        self.cheaper_flights = []
        for i in range(0,len(self.sheety_prices)):
            try:
                print(f"Getting flights for {self.sheety_prices[i]["city"]}: €{self.flights[i]["data"][0]["price"]["total"]}")
            except:
                print(f"No flights available for {self.sheety_prices[i]["city"]}")
            else:
                self.create_flight_info(
                    self.sheety_prices[i]["city"],
                    self.flights[i]["data"][0]["price"]["grandTotal"],
                    self.flights[i]["data"][0]["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                    self.flights[i]["data"][0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                    self.flights[i]["data"][0]["itineraries"][0]["segments"][0]["departure"]["at"].replace("T"," "),
                    self.flights[i]["data"][0]["itineraries"][1]["segments"][0]["departure"]["at"].replace("T", " ")
                )
        # for flight in self.flight_info:
        #     print(flight["info"])
        self.check_if_cheaper()

    def create_flight_info(self,city,price,origin_airport,destination_airport,out_date,return_date):
        self.flight_info.append(
            {
                "info":
                    f"Flight Information for {city}:\n"
                    f"Price: {price} (euro)\n"
                    f"Origin Airport: {origin_airport}\n"
                    f"Destionation Airport: {destination_airport}\n"
                    f"Out date: {out_date}\n"
                    f"Return date: {return_date}\n",
                "city":
                    city,
                "price":
                    price
            }
        )

    def check_if_cheaper(self):
        for i in range(0,len(self.flight_info)):
            index = next((j for j, item in enumerate(self.sheety_prices) if item['city'] == self.flight_info[i]["city"]), None)
            # print("Index of city in sheety_prices: ",index)
            if self.sheety_prices[index]["lowestPrice"] > float(self.flight_info[i]["price"]):
                # print(f"We have a cheaper flight for {self.flight_info[i]["city"]}!")
                self.cheaper_flights.append(self.flight_info[i])
