# convert all to SSS
import math
import error_handling


def ascending_order(s1, s2, s3):
    return tuple(sorted([s1, s2, s3]))


"""CONVERT TO SSS"""


def ssa_to_sss(side1, side2, angle3):
    # angle3 (in degrees) -> angle between the sides
    side3 = math.sqrt(
        side1**2 + side2**2 - 2 * side1 * side2 * math.cos(math.radians(angle3))
    )

    # error_handling.validate_triangle(side1, side2, side3) -> validating in Triangle class directly

    return ascending_order(
        side1,
        side2,
        side3,
    )  # returns tuple


def saa_to_sss(side, angle1_opp, angle2):
    # angle1_opp -> angle opposite to side
    # Third angle
    angle3 = 180 - angle1_opp - angle2  # sum of angles = 180°

    angle1_opp = math.radians(angle1_opp)
    angle2 = math.radians(angle2)
    angle3 = math.radians(angle3)

    # Using Law of Sines to find the other sides
    # input 'side' is opposite angle 'angle1_opp'
    side1 = side
    side2 = side1 * math.sin(angle2) / math.sin(angle1_opp)
    side3 = side1 * math.sin(angle3) / math.sin(angle1_opp)

    # error_handling.validate_triangle(side1, side2, side3)

    return ascending_order(
        side1,
        side2,
        side3,
    )


def coordinates_to_sss(p1, p2, p3):
    # p1, p2, p3 can be 2D (x, y) or 3D (x, y, z) tuples
    # All points must be the same dimension

    # Determine dimension from first point
    dimension = len(p1)

    if dimension == 2:
        # 2D coordinates - check for collinearity
        error_handling.validate_collinearity(p1, p2, p3)

        # Getting the sides in 2D
        a = math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
        b = math.sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
        c = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    elif dimension == 3:
        # 3D coordinates - compute distances using 3D formula
        # Distance = sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
        a = math.sqrt(
            (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2 + (p2[2] - p3[2]) ** 2
        )
        b = math.sqrt(
            (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2 + (p1[2] - p3[2]) ** 2
        )
        c = math.sqrt(
            (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
        )

    else:
        raise error_handling.InvalidValueError(
            f"Invalid dimension {dimension}. Expected 2D or 3D coordinates."
        )

    # error_handling.validate_triangle(a, b, c)

    return ascending_order(a, b, c)
