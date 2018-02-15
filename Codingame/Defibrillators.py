'''
Created on May 15, 2017

'''
from math import pi, sqrt, sin, cos, atan2


def haversine(ltA, lnA, ltB, lnB, unit):    # Haversine function to calculate distance
    lat1 = float(ltA)
    long1 = float(lnA)
    lat2 = float(ltB)
    long2 = float(lnB)

    degree_to_rad = float(pi / 180.0)

    d_lat = (lat2 - lat1) * degree_to_rad
    d_long = (long2 - long1) * degree_to_rad

    a = pow(sin(d_lat / 2), 2) + cos(lat1 * degree_to_rad) * \
        cos(lat2 * degree_to_rad) * pow(sin(d_long / 2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    if unit == 'km':
        return 6367 * c
    elif unit == 'miles':
        return 3956 * c


# lonA = "3,879483".replace(",", ".")
# latA = "43,608177".replace(",", ".")
# n = 1
# 1;Maison de la Prevention Sante;6 rue Maguelone 340000
# Montpellier;;3,87952263361082;43,6071285339217

lonA = input()  # user Longitute
latA = input()  # user Latitude
n = int(input())  # number of defibs
defibs = {}

for i in range(n):
    defib = input().split(";")
    # get defib name, defib lon, lat
    defibName, lonB, latB = defib[1], defib[-2].replace(
        ",", "."), defib[-1].replace(",", ".")

    d = haversine(latA, lonA, latB, lonB, "km")     # calc distance from user
    defibs[d] = defibName             # store distances in a dictionary

print(defibs[min(defibs)])
