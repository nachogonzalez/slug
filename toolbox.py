# toolbox.py

import random
import string
import geocoder

def generateID():
    characters = string.ascii_letters + string.digits
    buzz = ''.join(random.choice(characters) for i in range(25))
    return buzz

def getGeoInfo():
    g = geocoder.ip('me')
    return str(g.latlng)
