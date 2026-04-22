import subprocess
import os
import math
from output import *
from compute import Circle
import sys
from errors import *

# ---------- CLI UTILITIES ----------


def clear():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def line():
    print("=" * 50)


def section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)


def welcome():
    clear()
    line()
    print("⚪ CIRCLE SOLVER")
    print("Compute all properties of a circle")
    line()


def pause():
    input("\nPress ENTER to continue...")


def exit_program():
    print("\n" + "=" * 50)
    print("Thanks for using Circle Solver 🙌")
    print("Exiting successfully...")
    print("=" * 50)
    sys.exit()


# ---------- MENU ----------


def menu():
    section("Select Operation")

    print("1. Area")
    print("2. Perimeter")
    print("3. Diameter")
    print("4. Chord Length")
    print("5. Distance of Chord from Centre")
    print("6. Arc Length")
    print("7. Sector Area")
    print("8. Segment Area")
    print("9. Everything")
    print("0. Exit")

    return input("\nEnter choice → ")


# ---------- OUTPUT ----------


def show_result(label, value, is_area=False):
    unit = "sq. units" if is_area else "units"
    print(f"{label:<30}: {value:.2f} {unit}")


def show_all(circle):
    section("RESULT")

    for key in sorted(operations):
        label, method_name, is_area = operations[key]
        value = getattr(circle, method_name)()
        show_result(label, value, is_area)

    line()


# ---------- MAIN RUNNER ----------


def run_circle():
    welcome()

    while True:
        choice = menu()

        if choice == "0":
            exit_program()

        if choice not in operations and choice != "9":
            print("\nInvalid choice!")
            pause()
            continue

        try:
            section("INPUT")

            r = float(input("Enter radius → "))

            if choice in ["4", "5", "6", "7", "8", "9"]:
                angle = math.radians(float(input("Enter angle (degrees) → ")))
                circle = Circle(r, angle)
            else:
                circle = Circle(r)

            # ---------- OUTPUT ----------
            if choice == "9":
                show_all(circle)
            else:
                label, method_name, is_area = operations[choice]
                section("RESULT")
                value = getattr(circle, method_name)()
                show_result(label, value, is_area)
                line()

        except (InvalidRadiusError, InvalidAngleError, ValueError) as e:
            print("\nError:", e)

        pause()
