"""
CIRCLE SOLVER - Main Entry Point

This is the main orchestrator that brings together all modules:
- compute: Circle class with mathematical calculations
- input_handle: User input collection and validation
- output: Result display and CLI utilities
- error_handling: Custom exceptions and validation

The program allows users to:
1. Input circle parameters (radius, diameter, circumference, or area)
2. Calculate various geometric properties
3. View results in a formatted output

Author: Ronak Wadhwani
"""

from compute import Circle
import input_handle
import output
import error_handling
import math


def needs_angle(output_choice):
    """
    Determine if the selected output requires an angle input.

    Args:
        output_choice (str): The output operation choice

    Returns:
        bool: True if angle is needed, False otherwise
    """
    # Operations that need angle: chord, distance, arc, sector, segment, everything
    angle_required_operations = {"4", "5", "6", "7", "8", "9"}
    return output_choice in angle_required_operations


def main():
    """
    Main program loop - orchestrates the entire circle solver application.
    Logical flow: Ask what to calculate → Ask for inputs → Calculate & display results
    """
    while True:
        # ========== DETERMINE REQUIRED INPUTS ==========
        while True:
            output.welcome()  # Display welcome and clear screen at the start of each output selection

            output_choice = output.output_type_choice()

            if output_choice == "10":
                output.exit_program()
            elif output_choice in output.OPERATIONS or output_choice == "9":
                break
            else:
                print("❌ Invalid choice! Please try again!")
                output.pause()
                continue

        # ========== GET RADIUS ==========
        while True:
            try:
                output.section("INPUT")
                radius = input_handle.input_radius()
                break
            except (
                ValueError,
                error_handling.InvalidValueError,
                error_handling.InvalidRadiusError,
            ) as e:
                print(f"\n❌ Error: {e}")
                output.pause()
                output.clear()
                continue

        # ========== GET ANGLE IF NEEDED ==========
        angle = 2 * math.pi  # Full circle (2π) by default

        if needs_angle(output_choice):
            while True:
                try:
                    angle = input_handle.get_angle_in_radians()
                    break
                except (ValueError, error_handling.InvalidAngleError) as e:
                    print(f"\n❌ Error: {e}")
                    output.pause()
                    output.clear()
                    continue

        # ========== CIRCLE CREATION ==========
        try:
            circle = Circle(radius, angle)
        except (
            error_handling.InvalidRadiusError,
            error_handling.InvalidAngleError,
        ) as e:
            print(f"\n❌ Error: {e}")
            output.pause()
            output.clear()
            continue

        # ========== DISPLAY RESULT ==========
        if output_choice == "9":
            output.show_all(circle)
        elif output_choice in output.OPERATIONS:
            label, func = output.OPERATIONS[output_choice]
            output.section("RESULT")
            func(circle)
            output.line()

        output.pause()


if __name__ == "__main__":
    """
    Entry point - run the main program.

    Usage:
        python main.py
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + "=" * 50)
        print("Program interrupted by user")
        print("Thanks for using Circle Solver! 🙌")
        print("=" * 50)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback

        traceback.print_exc()
