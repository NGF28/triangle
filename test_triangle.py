from math import sqrt

import pytest

from triangle import classify_triangle, is_valid_triangle


@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        ((0, 2, 2), "Invalid"),
        ((1, 2, 3), "Invalid"),
        ((3, 3, 3), "Equilateral"),
        ((3, 3, 4), "Isosceles"),
        ((4, 5, 6), "Scalene"),
        ((3, 4, 5), "Right Scalene"),
        ((5, 5, 5 * sqrt(2)), "Right Isosceles"),
    ],
)
def test_classifies_triangle_cases(sides, expected):
    assert classify_triangle(*sides) == expected


def test_degenerate_boundary_is_invalid():
    assert not is_valid_triangle(1, 2, 3)
    assert classify_triangle(1, 2, 3) == "Invalid"


@pytest.mark.parametrize(
    "sides",
    [
        (0, 1, 1),
        (-1, 2, 2),
        (1, 1, 3),
    ],
)
def test_nonpositive_or_impossible_sides_are_invalid(sides):
    assert not is_valid_triangle(*sides)
    assert classify_triangle(*sides) == "Invalid"

def test_valid_triangle_returns_true():
    # check that sides 3, 4, 5 from a valid triangle
    assert is_valid_triangle(3, 4, 5) is True

def test_right_triangle_with_non_integer_sides():
    # check legs 5 and 5 with hypotenuse 5*sqrt(2)
    assert classify_triangle(
        5, 5, 5 * sqrt(2)
        ) == "Right Isosceles"