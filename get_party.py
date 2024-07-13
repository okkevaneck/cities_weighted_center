"""
Where to meet with international friends?
Find the weighted center of their cities and make a party!
"""

from geopy.geocoders import Nominatim
from functools import partial


def _parse_input_cities():
    with open("cities.txt", "r") as fp:
        cities = fp.readlines()

    city_counts = {}
    for c in cities:
        if c in city_counts:
            city_counts[c.strip()] += 1
        else:
            city_counts[c.strip()] = 1

    return city_counts


def _get_city_coordinates(city_counts):
    geolocator = Nominatim(user_agent="get_party")
    geocode = partial(geolocator.geocode, language="en")
    coords = []
    
    for city_name, count in city_counts.items():
        geodata = geocode(city_name)
        
        for _ in range(count):
            coords.append((geodata.latitude, geodata.longitude))
    
    return coords


def main():
    # Parse input cities.
    city_counts = _parse_input_cities()
    print(city_counts)
    
    # Acquire the coordinates.
    coords = _get_city_coordinates(city_counts)
    
    # Get center.


if __name__ == "__main__":
    main()