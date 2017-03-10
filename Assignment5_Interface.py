#!/usr/bin/python2.7
#
# Assignment5 Interface
# Name: Patrick Gaines
# This file contains all code to perform functions specified by the requirements in CSE512_Assignment5.pdf
#

from math import sin, cos, asin, sqrt, atan2
import sys

"""
FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection)
This function searches the 'collection' given to find all the business present in the
city provided in 'cityToSearch' and save it to 's aveLocation1'. For each business
you found, you should store name Full address, city, state of business in the
following format.
Each line of the saved file will contain,
Name$FullAddress$City$State. ($ is the separator and must be present)
"""

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    try:
        file = open(saveLocation1, "w")
        cityToSearch = cityToSearch.title()
        for business in collection.find({"city": cityToSearch}):
            full_address = str(business[u'full_address']).replace("\n", ",")
            file.write("{}${}${}${}\n".format(business[u'name'].upper(), full_address.upper(), business[u'city'].upper(), business[u'state'].upper()))
        file.close()
    except Exception as e:
        print('Error: {0}'.format(e))
        sys.exit(1)
    finally:
        pass

"""FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance,
saveLocation2, collection)
This function searches the 'collection' given to find name of all the business
present in the 'maxDistance' from the given 'myLocation' (please use the
distance algorithm given below) and save them to 'saveLocation2'.
Each line of the output file will contain the name of the business only.
"""

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    try:
        file = open(saveLocation2, "w")
        lat1 = float(myLocation[0])
        lon1 = float(myLocation[1])

        for business in collection.find():
            categories = business[u'categories']
            if not set(categories).isdisjoint(categoriesToSearch):
                lat2 = float(business[u'latitude'])
                lon2 = float(business[u'longitude'])
                dist = DistanceFunction(lat1, lon1, lat2, lon2)
                if dist <= maxDistance:
                    file.write("{}\n".format(business[u'name'].upper()))
        file.close()
    except Exception as e:
        print('Error: {0}'.format(e))
        sys.exit(1)
    finally:
        pass

"""Given two pairs of latitude and longitude as [lat2, lon2] and [lat1, lon1], you can calculate the
distance between them using the formula given below:"""
def DistanceFunction(lat2, lon2, lat1, lon1):
    R = 3959  # miles
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    dist = R * c
    return dist
