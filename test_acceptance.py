from triangle import classify_triangle


def test_stained_glass_customer_flow():
    # Buildable pieces receive a shape; right pieces are explicitly flagged.
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(4, 4, 4) == "Equilateral"

    # A non-buildable piece returns a message instead of raising an exception.
    assert classify_triangle(0, 2, 2) == "Invalid"
    assert classify_triangle(1, 2, 3) == "Invalid"
