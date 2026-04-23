"""
Input handling module - collects and validates user input for circle calculations.
Supports multiple input methods: radius, diameter, circumference, or area.
"""

import error_handling
import convert
import math


def get_radius_direct():
    """
    Get radius input directly from user.

    Returns:
        float: Validated radius

    Raises:
        ValueError: If input cannot be parsed as float
        InvalidRadiusError: If radius is invalid
    """
    radius = float(input("Enter radius: "))
    error_handling.validate_input("radius", radius)
    return radius


def get_radius_from_diameter():
    """
    Get radius from diameter input.

    Returns:
        float: Radius calculated from diameter

    Raises:
        ValueError: If input cannot be parsed as float
        InvalidValueError: If diameter is invalid
    """
    diameter = float(input("Enter diameter: "))
    return convert.diameter_to_radius(diameter)


def get_radius_from_circumference():
    """
    Get radius from circumference input.

    Returns:
        float: Radius calculated from circumference

    Raises:
        ValueError: If input cannot be parsed as float
        InvalidValueError: If circumference is invalid
    """
    circumference = float(input("Enter circumference: "))
    return convert.circumference_to_radius(circumference)


def get_radius_from_area():
    """
    Get radius from area input.

    Returns:
        float: Radius calculated from area

    Raises:
        ValueError: If input cannot be parsed as float
        InvalidValueError: If area is invalid
    """
    area = float(input("Enter area: "))
    return convert.area_to_radius(area)


def get_angle_in_radians():
    """
    Get angle input from user and convert to radians.

    Returns:
        float: Angle in radians (0, 2π]

    Raises:
        ValueError: If input cannot be parsed as float
        InvalidAngleError: If angle is invalid
    """
    print("\nEnter angle in degrees (0, 360]:")
    degrees = float(input("Enter angle (degrees): "))
    return convert.degrees_to_radians(degrees)


def input_radius():
    """
    Get radius from user with multiple input method options.

    Returns:
        float: Validated radius

    Raises:
        ValueError: If input is invalid
        error_handling.InvalidRadiusError: If radius is invalid
    """
    print("\nSelect input method:")
    print("-" * 50)
    print("1. Enter radius directly")
    print("2. Enter diameter (convert to radius)")
    print("3. Enter circumference (convert to radius)")
    print("4. Enter area (convert to radius)")

    choice = input("\nEnter choice (1-4): ").strip()

    input_methods = {
        "1": get_radius_direct,
        "2": get_radius_from_diameter,
        "3": get_radius_from_circumference,
        "4": get_radius_from_area,
    }

    if choice not in input_methods:
        raise ValueError("Invalid choice! Please enter 1, 2, 3, or 4.")

    return input_methods[choice]()
