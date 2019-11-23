import time
import math
from geopy.distance import geodesic

class Coordinate:
    def __init__(self):
        pass

    def minDistanceBetweenLineAndPoint(self, lat1, lon1, lat2, lon2, lat3, lon3) -> float:
        #https://stackoverflow.com/questions/20231258/minimum-distance-between-a-point-and-a-line-in-latitude-longitude
        # lat1 = 3.227511
        # lon1 = 101.724318
        # lat2 = 3.222895
        # lon2 = 101.719751
        # lat3 = 3.224972 % point
        # lon3 = 101.722932 % point

        y = math.sin(lon3 - lon1) * math.cos(lat3)
        x = math.cos(lat1) * math.sin(lat3) - math.sin(lat1) * math.cos(lat3) * math.cos(lat3 - lat1)
        bearing1 = math.degrees(math.atan2(y, x))
        bearing1 = 360 - ((bearing1 + 360) % 360)

        y2 = math.sin(lon2 - lon1) * math.cos(lat2)
        x2 = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lat2 - lat1)
        bearing2 = math.degrees(math.atan2(y2, x2))
        bearing2 = 360 - ((bearing2 + 360) % 360)

        lat1Rads = math.radians(lat1)
        lat3Rads = math.radians(lat3)
        dLon = math.radians(lon3 - lon1)

        distanceAC = math.acos(math.sin(lat1Rads) * math.sin(lat3Rads)+math.cos(lat1Rads)*math.cos(lat3Rads)*math.cos(dLon)) * 6371  
        min_distance = math.fabs(math.asin(math.sin(distanceAC/6371)*math.sin(math.radians(bearing1)-math.radians(bearing2))) * 6371)

        # print(f"bearing 1: {bearing1}")  
        # print(f"bearing 2: {bearing2}")  
        # print(f"distance AC: {distanceAC}")  
        # print(f"min distance km: {min_distance}")
        #print(f"min distance to line in m: {min_distance*1000}")
        distInCm = min_distance*1000*100
        print(f"min distance to line in cm: {distInCm}")
        return distInCm
