import math
import error_handling

"""VALIDATING TRIANGLE AND COMPUTING RESULTS"""


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.__area = None
        # no need to compute area again and again for different use cases

        error_handling.validate_triangle(a, b, c)
        print(f"\nCreated: {self}")

    def __str__(self):
        return f"Triangle ({self.a:.2f}, {self.b:.2f}, {self.c:.2f})"

    def semi_perimeter(self):
        return (self.a + self.b + self.c) / 2  # semi perimeter 's'

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        if self.__area is None:
            s = self.semi_perimeter()
            # no need to check for right/equilateral - unnecessary

            # heron's formula
            self.__area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

        return self.__area

    def angles(self):
        A = B = C = 0

        # calculating cos of angles
        cosA = (self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)
        cosB = (self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)
        cosC = (self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)

        # Clamp values to [-1, 1] to avoid domain errors in acos() due to floating point precision
        cosA = max(-1, min(1, cosA))
        cosB = max(-1, min(1, cosB))
        cosC = max(-1, min(1, cosC))

        # return angles A, B, C in radians
        A = math.acos(cosA)  # cos inverse
        B = math.acos(cosB)
        C = math.acos(cosC)

        return (A, B, C)
        # the input sides will already be sorted hence no need to sort the angles

    def triangle_angle_type(self):
        c2, ab2 = self.c**2, self.a**2 + self.b**2
        if math.isclose(c2, ab2):
            return "right"
        elif c2 < ab2:
            return "acute"
        else:
            return "obtuse"

    def triangle_side_type(self):
        if math.isclose(self.a, self.b) and math.isclose(self.b, self.c):
            return "equilateral"

        elif (
            math.isclose(self.a, self.b)
            or math.isclose(self.b, self.c)
            or math.isclose(self.c, self.a)
        ):
            return "isosceles"

        else:
            return "scalene"

    def inradius(self):
        return self.area() / self.semi_perimeter()

    def circumradius(self):
        return self.a * self.b * self.c / (4 * self.area())

    def altitudes(self):
        area = self.area()

        alt1 = 2 * area / self.a  # length of altitude from vertex 1 (angle1) to side 1
        alt2 = 2 * area / self.b
        alt3 = 2 * area / self.c

        return sorted([alt1, alt2, alt3])  # list

    def medians(self):
        m1 = 0.5 * math.sqrt(
            2 * self.b**2 + 2 * self.c**2 - self.a**2
        )  # median to mid of side1
        m2 = 0.5 * math.sqrt(2 * self.a**2 + 2 * self.c**2 - self.b**2)
        m3 = 0.5 * math.sqrt(2 * self.a**2 + 2 * self.b**2 - self.c**2)

        return sorted([m1, m2, m3])  # list
