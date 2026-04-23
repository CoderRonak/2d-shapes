"""
Output handling module - displays circle properties and results to the user.
Provides CLI utilities and formatted output functions.
"""

import os
import sys
import math


# ========== CLI UTILITIES ==========


def clear():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


def line():
    """Print a horizontal line separator"""
    print("=" * 50)


def section(title):
    """Print a section header with title"""
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)


def welcome():
    """Display welcome screen"""
    clear()
    line()
    print("⭕ CIRCLE SOLVER")
    print("Compute all properties of a circle")
    line()


def pause():
    """Pause and wait for user to press Enter"""
    input("\nPress ENTER to continue...")


def exit_program():
    """Display exit message and exit program"""
    print("\n" + "=" * 50)
    print("Thanks for using Circle Solver 🙌")
    print("Exiting successfully...")
    print("=" * 50)
    sys.exit()


# ========== MENU FUNCTIONS ==========


def input_type_choice():
    """
    Display input method selection menu.

    Returns:
        str: User's choice (1-4 for input methods, 5 for exit)
    """
    section("Select Input Method")

    print("1. Enter radius directly")
    print("2. Enter diameter (convert to radius)")
    print("3. Enter circumference (convert to radius)")
    print("4. Enter area (convert to radius)")
    print("5. Exit")

    return input("\nEnter choice → ")


def output_type_choice():
    """
    Display output selection menu.

    Returns:
        str: User's choice (1-9 for properties, 10 for exit)
    """
    section("Select Output Property")

    print("1. Area")
    print("2. Circumference/Perimeter")
    print("3. Diameter")
    print("4. Chord Length")
    print("5. Distance of Chord from Centre")
    print("6. Arc Length")
    print("7. Sector Area")
    print("8. Segment Area")
    print("9. Everything")
    print("10. Exit")

    return input("\nEnter choice → ")


# ========== OUTPUT FORMATTING ==========


def format_output(label, value, is_area=False):
    """
    Format a single property output line.

    Args:
        label (str): Property name
        value (float): Calculated value
        is_area (bool): Whether this is an area measurement

    Returns:
        str: Formatted output string
    """
    unit = "sq. units" if is_area else "units"
    return f"{label:<35}: {value:.4f} {unit}"


# ========== PROPERTY DISPLAY FUNCTIONS ==========


def show_area(circle):
    """Display circle area"""
    print(f"Area             : {circle.area():.4f} sq. units")


def show_circumference(circle):
    """Display circle circumference/perimeter"""
    print(f"Circumference    : {circle.perimeter():.4f} units")


def show_diameter(circle):
    """Display circle diameter"""
    print(f"Diameter         : {circle.diameter():.4f} units")


def show_chord_length(circle):
    """Display chord length"""
    print(f"Chord Length     : {circle.chord_length():.4f} units")


def show_chord_distance(circle):
    """Display distance of chord from center"""
    print(f"Chord Distance   : {circle.chord_dist_from_centre():.4f} units")


def show_arc_length(circle):
    """Display arc length"""
    print(f"Arc Length       : {circle.arc_length():.4f} units")


def show_sector_area(circle):
    """Display sector area"""
    print(f"Sector Area      : {circle.sector_area():.4f} sq. units")


def show_segment_area(circle):
    """Display segment area"""
    print(f"Segment Area     : {circle.segment_area():.4f} sq. units")


def show_all(circle):
    """Display all circle properties"""
    section("RESULTS")

    # Basic properties
    show_area(circle)
    show_circumference(circle)
    show_diameter(circle)

    # Angle-dependent properties (only if not full circle)
    if circle.angle < 2 * math.pi - 0.0001:  # Not a full circle
        print()
        show_chord_length(circle)
        show_chord_distance(circle)
        show_arc_length(circle)
        show_sector_area(circle)
        show_segment_area(circle)

    line()


# ========== PROPERTY MAPPING ==========

OPERATIONS = {
    "1": ("Area", show_area),
    "2": ("Circumference", show_circumference),
    "3": ("Diameter", show_diameter),
    "4": ("Chord Length", show_chord_length),
    "5": ("Chord Distance", show_chord_distance),
    "6": ("Arc Length", show_arc_length),
    "7": ("Sector Area", show_sector_area),
    "8": ("Segment Area", show_segment_area),
    "9": ("Everything", show_all),
}


def execute_operation(circle, choice):
    """
    Execute and display the selected operation.

    Args:
        circle: Circle object with calculated properties
        choice (str): Operation choice (1-9)
    """
    if choice not in OPERATIONS:
        print("Invalid choice!")
        return

    label, func = OPERATIONS[choice]
    section("RESULT")
    func(circle)
    line()
