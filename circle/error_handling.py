import math


# CUSTOM EXCEPTIONS
class InvalidValueError(Exception):
    """Raised when a value is invalid (negative, NaN, or Inf)"""

    pass


class InvalidRadiusError(Exception):
    """Raised when radius is invalid"""

    pass


class InvalidAngleError(Exception):
    """Raised when angle is invalid"""

    pass


class InvalidDiameterError(Exception):
    """Raised when diameter is invalid"""

    pass


class InvalidCircumferenceError(Exception):
    """Raised when circumference is invalid"""

    pass


# VALIDATION FUNCTIONS
def validate_input(mode="radius", *args):
    """
    Validate input values based on mode.

    Args:
        mode (str): Type of input - 'radius', 'diameter', 'circumference', or 'angle'
        *args: Values to validate

    Raises:
        ValueError: If value is NaN or infinite
        InvalidValueError: If value is not positive
        InvalidAngleError: If angle is not in valid range (0, 2π]
    """
    for i in args:
        # Check for NaN or infinite values
        if math.isnan(i) or math.isinf(i):
            raise ValueError("Invalid number! Cannot be NaN or Infinite.")

        # Check for positive values
        if not i > 0:
            raise InvalidValueError(f"Invalid {mode}! Must be positive (> 0).")

        # Mode-specific validation
        if mode == "angle" and not (0 < i <= 2 * math.pi):
            raise InvalidAngleError(
                f"Invalid angle! Must be in range (0, 2π] radians. Got: {i:.4f}"
            )


def validate_circle_input(radius, angle=None):
    """
    Validate circle input parameters.

    Args:
        radius (float): Radius of the circle
        angle (float, optional): Angle in radians for sector/arc calculations

    Raises:
        InvalidRadiusError: If radius is invalid
        InvalidAngleError: If angle is invalid
    """
    try:
        validate_input("radius", radius)
    except (ValueError, InvalidValueError) as e:
        raise InvalidRadiusError(f"Invalid radius: {str(e)}")

    if angle is not None:
        try:
            validate_input("angle", angle)
        except (ValueError, InvalidValueError) as e:
            raise InvalidAngleError(f"Invalid angle: {str(e)}")
