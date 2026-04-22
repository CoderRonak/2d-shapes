from errors import *
from base_class import Shapes
import math


class Circle(Shapes):
    def __init__(self, r, angle=2 * math.pi):
        self.r = r
        self.angle = angle
        self.__validate_r()
        self.__validate_angle()

    def __validate_r(self):
        if not (isinstance(self.r, (int, float)) and self.r > 0):
            raise InvalidRadiusError("Invalid Radius!")

    def __validate_angle(self):
        if not (isinstance(self.angle, (int, float)) and 0 < self.angle <= 2 * math.pi):
            raise InvalidAngleError("Invalid Angle!")

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 2 * math.pi * self.r

    def diameter(self):
        return 2 * self.r

    def chord_length(self):
        return 2 * self.r * math.sin(self.angle / 2)

    def chord_dist_from_centre(self):
        return self.r * math.cos(self.angle / 2)

    def arc_length(self):
        return self.r * self.angle

    def sector_area(self):
        return 0.5 * (self.r**2) * self.angle

    def segment_area(self):
        return 0.5 * (self.r**2) * (self.angle - math.sin(self.angle))
