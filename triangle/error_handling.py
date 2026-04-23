import math


# EXCEPTIONS
class InvalidValueError(Exception):
    pass


class InvalidAngleError(Exception):
    pass


class InvalidTriangleError(Exception):
    pass


def validate_input(mode="side", *args):
    # mode can be 'side' or 'angle
    for i in args:
        if math.isnan(i) or math.isinf(i):
            # i is NaN or i is INFINITE
            # NO NEED TO CHECK FOR : i is not an INT or i is not a FLOAT BECAUSE IN INPUT WE HAVE CONVERTED EVERYTHING TO FLOAT
            raise ValueError("Invalid number !")
        elif not i > 0:
            raise InvalidValueError("Invalid Value ! Should be positive !")
        elif mode == "angle" and not i < 180:
            raise InvalidAngleError("Invalid Angle ! Should be < 180° !")

    if mode == "angle" and len(args) == 2:
        # 2 angles have been entered, their sum should be < 180°
        if not args[0] + args[1] < 180:
            raise InvalidAngleError(
                "Invalid Angles ! Sum of both angle should be < 180° !"
            )


def validate_triangle(s1, s2, s3):
    if not (s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2):
        raise InvalidTriangleError("Invalid Triangle !")


def validate_collinearity(p1, p2, p3):
    """Check if three 2D points are collinear or nearly-collinear using cross product.
    If area is too small (< 1e-6), reject as degenerate triangle.
    Only works for 2D points.
    """
    if len(p1) != 2 or len(p2) != 2 or len(p3) != 2:
        # For 3D, collinearity check is more complex, rely on triangle inequality
        return
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Cross product: (p2-p1) × (p3-p1)
    cross_product = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    # If cross product is very close to 0, points are collinear/nearly-collinear
    if abs(cross_product) < 1e-10:
        raise InvalidTriangleError("Invalid Triangle ! Points are collinear or nearly collinear.")
