# Import dependencies
from citipy import citipy
import requests
import numpy as np
import time
from api_keys import weather_api_key

# Output
cities_file = "data/cities.csv"

# Latitude and Longitude ranges
lat_range = (-90, 90)
lon_range = (-180, 180)


def GenerateCoords():
    # Generate the lat_lon list
    lat_lon = []
    cities = []
    np.random.seed(5)
    lats = np.random.uniform(lat_range[0], lat_range[1], size=10)
    lons = np.random.uniform(lon_range[0], lon_range[1], size=10)
    lat_lon = zip(lats, lons)
    # lat_lon_list = list(lat_lon)
    # print(lat_lon_list)

    # Make a class for the cities
    class Place:
        def __init__(self, cityname, lat, lon):
            self.cityname = cityname
            self.lat = lat
            self.lon = lon
        
        def printPlace(self):
            print(self.cityname, self.lat, self.lon)

    for pair in lat_lon:
        cities.append(Place(citipy.nearest_city(pair[0], pair[1]).city_name, pair[0], pair[1]))

    return cities

cities = GenerateCoords()

# Print the entire list of cities
for city in cities:
    city.printPlace()

# Find a way to search the cities! Loop? Next we'll need to do an API call for 1 city to try collecting weather data and loading it into the Place class.
# def SearchCities(place):
#     return np.char.chararray.find(sub=place, start=0, end=None)[cities]
#     # return cities[cities.index(place)]

# SearchCities('biak')


# API items
base_URL = 'http://ai.openweathermap.org/data/3.0/onecall?'
URL_end = '&exclude=hourly&appid='
api_key = '&appid=' + weather_api_key

# Create a function to call the API and collect data for our list of cities
# Example: https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}

# def get_city_data():
#     # Create a dictionary for city data
#     citydict = {}
#     record = 1
#     setnum = 1

#     for place in cities:
#         query = baseURL + 'lat=' + city[1] + '&lon=' + city[2] + URL_end + api_key
#         cityresponse = requests.get(query)
#         cityjson = cityresponse.json()




