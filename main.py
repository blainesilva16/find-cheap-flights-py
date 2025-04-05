from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

flight_search = FlightSearch()
data_manager = DataManager(flight_search)
flight_data = FlightData(data_manager.sheety_prices, data_manager.flights)
notification_manager = NotificationManager(flight_data.cheaper_flights)