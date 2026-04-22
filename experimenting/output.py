def format_output(label, value, is_area=False):

    unit = "sq. units" if is_area else "units"

    return f"{label:<30}: {value:.2f} {unit}"


operations = {
    "1": ("Area", "area", True),
    "2": ("Perimeter", "perimeter", False),
    "3": ("Diameter", "diameter", False),
    "4": ("Chord Length", "chord_length", False),
    "5": ("Distance from Centre", "chord_dist_from_centre", False),
    "6": ("Arc Length", "arc_length", False),
    "7": ("Sector Area", "sector_area", True),
    "8": ("Segment Area", "segment_area", True),
}


def execute_operation(circle, key):
    label, method_name, is_area = operations[key]
    method = getattr(circle, method_name)
    value = method()  # concept: a function is a callable variable :D
    return format_output(label, value, is_area)
