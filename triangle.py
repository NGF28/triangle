
from math import isclose, isfinite


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """Return whether three finite, positive lengths form a non-degenerate triangle."""
    sides = (a, b, c)
    if not all(isfinite(side) and side > 0 for side in sides):
        return False

    smallest, middle, largest = sorted(sides)
    return smallest + middle > largest


def classify_triangle(a: float, b: float, c: float) -> str:
    """Classify a triangle and prefix right triangles with ``Right ``."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    smallest, middle, largest = sorted((a, b, c))
    if a == b == c:
        classification = "Equilateral"
    elif a == b or a == c or b == c:
        classification = "Isosceles"
    else:
        classification = "Scalene"

    normalized_squares = (smallest / largest) ** 2 + (middle / largest) ** 2
    if isclose(normalized_squares, 1.0, rel_tol=1e-9, abs_tol=1e-9):
        return f"Right {classification}"
    return classification
