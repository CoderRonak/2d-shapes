"""
Convert different input formats to standard circle parameters (radius, angle).
Supports conversion from: diameter, circumference, area, or direct radius input.
"""

import math
import error_handling


def diameter_to_radius(diameter):
    """Convert diameter to radius"""
    error_handling.validate_input("diameter", diameter)
    return diameter / 2


def circumference_to_radius(circumference):
    """Convert circumference to radius"""
    error_handling.validate_input("circumference", circumference)
    return circumference / (2 * math.pi)


def area_to_radius(area):
    """Convert area to radius"""
    error_handling.validate_input("radius", area)  # area must be positive
    return math.sqrt(area / math.pi)


def degrees_to_radians(degrees):
    """Convert angle from degrees to radians"""
    if not (0 < degrees <= 360):
        raise error_handling.InvalidAngleError(
            f"Invalid angle! Must be in range (0, 360] degrees. Got: {degrees}"
        )
    return math.radians(degrees)


def normalize_angle(angle_radians):
    """Ensure angle is in valid range (0, 2π]"""
    if angle_radians <= 0 or angle_radians > 2 * math.pi:
        raise error_handling.InvalidAngleError(
            f"Invalid angle! Must be in range (0, 2π] radians. Got: {angle_radians:.4f}"
        )
    return angle_radians
