import error_handling
import convert

"""INPUT AND CONVERT"""


def input_and_convert_sas():
    side1, side2, angle3 = input_ssa()
    return convert.ssa_to_sss(side1=side1, side2=side2, angle3=angle3)


def input_and_convert_saa():
    side, angle1_opp, angle2 = input_saa()
    return convert.saa_to_sss(side=side, angle1_opp=angle1_opp, angle2=angle2)


def input_and_convert_coords():
    p1, p2, p3 = input_coordinates()
    return convert.coordinates_to_sss(p1, p2, p3)


"""INPUT AND VALIDATE INPUT"""


def input_sss():
    s1 = float(input("Enter side 1: "))
    s2 = float(input("Enter side 2: "))
    s3 = float(input("Enter side 3: "))
    # if input isn't parsable, it will automatically raise ValueError

    error_handling.validate_input("side", s1, s2, s3)
    # will raise InvalidValueError & InvalidAngleError

    # catch exception in main.py only ! :D

    sort = sorted([s1, s2, s3])
    return (
        sort[0],
        sort[1],
        sort[2],
    )  # returns SORTED tuple instead of returning the above list :D


def input_ssa():
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))

    angle3 = float(
        input("Enter the angle (in degrees) enclosed by the sides 1 and 2: ")
    )

    error_handling.validate_input("side", side1, side2)
    error_handling.validate_input("angle", angle3)

    return (side1, side2, angle3)  # returning ssa as tuple


def input_saa():
    side = float(input("Enter the side (opp. to known angle): "))
    angle1_opp = float(input("Enter the angle (degrees) opposite to the given side: "))
    angle2 = float(input("Enter the other angle(degrees): "))

    error_handling.validate_input("side", side)
    error_handling.validate_input("angle", angle1_opp, angle2)

    return (
        side,
        angle1_opp,
        angle2,
    )  # returning saa as tuple, where 2nd a is the opposite angle


def input_coordinates():
    print("Enter coordinates (2D or 3D, comma separated) of 3 points:")
    print("Format: x,y for 2D or x,y,z for 3D (all 3 points must be same dimension)\n")
    
    point1 = (
        input("Enter point 1 (e.g., 1,2 or 1,2,3): ").replace(" ", "").split(",")
    )
    point2 = input("Enter point 2 (e.g., 1,2 or 1,2,3): ").replace(" ", "").split(",")
    point3 = input("Enter point 3 (e.g., 1,2 or 1,2,3): ").replace(" ", "").split(",")

    # Validate that each point has 2 or 3 coordinates (all same dimension)
    coord_counts = {len(point1), len(point2), len(point3)}
    
    if len(coord_counts) > 1:
        raise error_handling.InvalidValueError(
            "Invalid coordinates! All 3 points must have the same dimension (all 2D or all 3D)."
        )
    
    dimension = list(coord_counts)[0]
    
    if dimension not in [2, 3]:
        raise error_handling.InvalidValueError(
            f"Invalid coordinates! Each point must have 2 values (2D) or 3 values (3D), got {dimension}."
        )
    
    # Convert all coordinates to floats
    try:
        if dimension == 2:
            x1, y1 = float(point1[0]), float(point1[1])
            x2, y2 = float(point2[0]), float(point2[1])
            x3, y3 = float(point3[0]), float(point3[1])
            return ((x1, y1), (x2, y2), (x3, y3))
        else:  # dimension == 3
            x1, y1, z1 = float(point1[0]), float(point1[1]), float(point1[2])
            x2, y2, z2 = float(point2[0]), float(point2[1]), float(point2[2])
            x3, y3, z3 = float(point3[0]), float(point3[1]), float(point3[2])
            return ((x1, y1, z1), (x2, y2, z2), (x3, y3, z3))
    except (ValueError, IndexError) as e:
        raise error_handling.InvalidValueError(f"Invalid coordinates! Could not parse: {e}")
