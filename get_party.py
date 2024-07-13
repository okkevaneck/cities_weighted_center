"""
Where to meet with international friends?
Find the weighted center of their cities and make a party!
"""

from geopy.geocoders import Nominatim
from functools import partial

geolocator = Nominatim(user_agent="get_party")


def _parse_input_cities():
    with open("cities.txt", "r") as fp:
        cities = fp.readlines()

    city_counts = {}

    for c in cities:
        city_name = c.strip()

        if city_name in city_counts:
            city_counts[city_name] += 1
        else:
            city_counts[city_name] = 1

    return city_counts


def _get_city_coordinates(city_counts):
    geocode = partial(geolocator.geocode, language="en")
    coords = []
    
    for city_name, count in city_counts.items():
        print("Parsing: ", city_name)
        geodata = geocode(city_name)
        
        for _ in range(count):
            coords.append((geodata.latitude, geodata.longitude))
    
    return coords


def _get_center_coords(coords):
    avg_lat = sum(lat for lat, _ in coords) / len(coords)
    avg_lon = sum(lon for _, lon in coords) / len(coords)
    return avg_lat, avg_lon


def main():
    # Parse input cities.
    city_counts = _parse_input_cities()
    print(city_counts)
    
    # Acquire the coordinates.
    coords = _get_city_coordinates(city_counts)
    
    # Get center.
    center = _get_center_coords(coords)
    
    print(f"Party place: {center}\n\tWhich is: {geolocator.reverse(center)}")


if __name__ == "__main__":
    main()