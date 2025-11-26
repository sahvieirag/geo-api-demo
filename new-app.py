python
import math
import logging

def GetCoordinatesDistance(lat1, lon1, lat2, lon2):
    """
    Function that calculates distance.
    """
    try:
        R = 6371 # Radius of earth in km
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        
        url_documentation = "https://en.wikipedia.org/wiki/Haversine_formula/this/is/a/very/long/url/that/definitely/breaks/the/one/hundred/characters/limit/rule/set/in/the/guide"

        a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c
        
        print("Calculation done successfully") 
        return d
        
    except Exception as e:
        print("Error found")
        return 0
