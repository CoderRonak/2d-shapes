# 'triangle' is an object of class 'Triangle'
import os
import sys
import math

"""ALL THE CLI PART"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def line():
    print("=" * 50)


def section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)


def welcome():
    clear()
    line()
    print("🔺 TRIANGLE SOLVER")
    print("Compute all properties of a triangle")
    line()


def pause():
    input("\nPress ENTER to continue...")


def exit_program():
    print("\n" + "=" * 50)
    print("Thanks for using Triangle Solver 🙌")
    print("Exiting successfully...")
    print("=" * 50)
    sys.exit()


def input_type_choice():
    section("Select Input Type")

    print("1. Three sides (SSS)")
    print("2. Two sides + included angle (SAS)")
    print("3. One side + two angles (ASA/AAS)")
    print("4. Coordinates of vertices (2D or 3D)")
    print("5. Exit")

    return input("\nEnter choice → ")


def output_type_choice():
    section("Select Output")

    print("1. Triangle Type")
    print("2. Perimeter")
    print("3. Area")
    print("4. Angles")
    print("5. Inradius")
    print("6. Circumradius")
    print("7. Medians")
    print("8. Altitudes")
    print("9. Everything")
    print("10. Exit")

    return input("\nEnter choice → ")


# 🔺 OUTPUT DISPLAY FUNCTIONS


def show_triangle_type(t):
    print(f"Type           : {t.triangle_angle_type()} & {t.triangle_side_type()}")


def show_perimeter(t):
    print(f"Perimeter      : {t.perimeter():.2f} units")


def show_area(t):
    print(f"Area           : {t.area():.2f} sq. units")


def show_angles(t):
    a = [f"{math.degrees(x):.2f}" for x in t.angles()]
    print(f"Angles (deg)   : {', '.join(a)}")


def show_inradius(t):
    print(f"Inradius       : {t.inradius():.2f} units")


def show_circumradius(t):
    print(f"Circumradius   : {t.circumradius():.2f} units")


def show_medians(t):
    m = [f"{x:.2f}" for x in t.medians()]
    # t.medians() will return sorted list of floats
    print(f"Medians        : {', '.join(m)} units")


def show_altitudes(t):
    h = [f"{x:.2f}" for x in t.altitudes()]
    # t.altitudes() will return sorted list of floats
    print(f"Altitudes      : {', '.join(h)} units")


def show_all(t):
    section("RESULT")

    show_triangle_type(t)
    show_perimeter(t)
    show_area(t)
    show_angles(t)
    show_inradius(t)
    show_circumradius(t)
    show_medians(t)
    show_altitudes(t)

    line()
