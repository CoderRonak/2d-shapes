"""
Circle computation module - calculates all geometric properties of a circle.
"""

from base_class import Shapes
import error_handling
import math


class Circle(Shapes):
    """
    Represents a circle with radius and optional central angle.

    Attributes:
        r (float): Radius of the circle
        angle (float): Central angle in radians (0, 2π]. Default is 2π (full circle)
    """

    def __init__(self, r, angle=2 * math.pi):
        """
        Initialize a Circle object.

        Args:
            r (float): Radius of the circle (must be positive)
            angle (float): Central angle in radians (default: 2π for full circle)

        Raises:
            InvalidRadiusError: If radius is invalid
            InvalidAngleError: If angle is invalid
        """
        self.r = r
        self.angle = angle
        self._validate_inputs()
        print(f"\nCreated: {self}")

    def __str__(self):
        """String representation of the circle"""
        return f"Circle (radius={self.r:.2f})"

    def _validate_inputs(self):
        """Validate radius and angle parameters"""
        error_handling.validate_circle_input(self.r, self.angle)

    # ========== BASIC PROPERTIES ==========

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * self.r**2

    def perimeter(self):
        """Calculate the circumference (perimeter) of the circle"""
        return 2 * math.pi * self.r

    def diameter(self):
        """Calculate the diameter of the circle"""
        return 2 * self.r

    def circumference(self):
        """Alias for perimeter() - calculates circumference"""
        return self.perimeter()

    # ========== CHORD PROPERTIES ==========

    def chord_length(self):
        """
        Calculate the length of a chord subtending a central angle.

        Returns:
            float: Length of the chord
        """
        return 2 * self.r * math.sin(self.angle / 2)

    def chord_distance_from_centre(self):
        """
        Calculate the perpendicular distance from the center to a chord.

        Returns:
            float: Distance from center to the chord
        """
        return self.r * math.cos(self.angle / 2)

    # Alias for backward compatibility
    def chord_dist_from_centre(self):
        """Alias for chord_distance_from_centre()"""
        return self.chord_distance_from_centre()

    # ========== ARC PROPERTIES ==========

    def arc_length(self):
        """
        Calculate the length of an arc subtending a central angle.

        Returns:
            float: Length of the arc
        """
        return self.r * self.angle

    # ========== SECTOR PROPERTIES ==========

    def sector_area(self):
        """
        Calculate the area of a sector (pie-slice) of the circle.

        Returns:
            float: Area of the sector
        """
        return 0.5 * (self.r**2) * self.angle

    # ========== SEGMENT PROPERTIES ==========

    def segment_area(self):
        """
        Calculate the area of a segment (region between a chord and arc).

        Returns:
            float: Area of the segment
        """
        return 0.5 * (self.r**2) * (self.angle - math.sin(self.angle))
