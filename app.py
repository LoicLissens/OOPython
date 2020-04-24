
import json
from math import pi
# Class agent the constructor iter on the dics caracts to have all the properties of an agent
class Person:
    
    def __init__(self, position,**caracts):
        for caract_name, caract_value in caracts.items():
            self.position = position
            setattr(self, caract_name, caract_value)
class Position:
    def __init__(self, longitude_deg, latitude_deg):
        self.longitude_deg = longitude_deg
        self.latitude_deg = latitude_deg
    @property
    def longitude(self):
        return (self.longitude_deg * pi)/180
    @property
    def latitude(sefl):
        return (self.latitude_deg * pi)/180

# Zone will represent a map in 2d with X & Y
class Zone:
    MIN_LONGITUDE_DEG = -180
    MAX_LONGITUDE_DEG = 180
    ESPACEMENT_DEG = 1
    def __init__(self, coin1, coin2):
        self.coin1 = coin1
        self.coin2 = coin2
        self.habitants = 0

    def init_zone(self):
        for longitude in range(self.MIN_LONGITUDE_DEG, self.MAX_LONGITUDE_DEG,self.ESPACEMENT_DEG):



def main():
    # take all the agent's attributes in the JSON doc and turns it into python dics
    for caracts in json.load(open("agents-100k.json")):
        latitude = caracts.pop("latitude")
        longitude = caracts.pop("longitude")
        position = Position(longitude, latitude)
        person = Person(position,**caracts)
        
        
if __name__== "__main__":
    #main()
    