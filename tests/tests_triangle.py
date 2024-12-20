import pytest
import math
from triangle import area, perimeter


def test_area_with_valid_triangle():
    a, b, c = 3, 4, 5
    expected_result = 6.0
    result = area(a, b, c)
    assert math.isclose(
        result, expected_result, rel_tol=1e-9
    ), f"Expected {expected_result}, got {result}"


def test_area_with_float_triangle():
    a, b, c = 2.5, 4.5, 5.5
    p = (a + b + c) / 2
    expected_result = math.sqrt(p * (p - a) * (p - b) * (p - c))
    result = area(a, b, c)
    assert math.isclose(
        result, expected_result, rel_tol=1e-9
    ), f"Expected {expected_result}, got {result}"


def test_area_with_negative_side():
    a, b, c = -3, 4, 5
    with pytest.raises(ValueError, match="Input must be greater than or equal to 0"):
        area(a, b, c)


def test_area_with_invalid_type():
    a, b, c = 3, "side", 5
    with pytest.raises(ValueError, match="Input must be a number"):
        area(a, b, c)


def test_area_with_invalid_triangle():
    a, b, c = 1, 2, 3
    with pytest.raises(
        ValueError, match="The provided sides do not form a valid triangle."
    ):
        area(a, b, c)


def test_perimeter_with_valid_triangle():
    a, b, c = 3, 4, 5
    expected_result = 12
    result = perimeter(a, b, c)
    assert result == expected_result, F"Expected {expected_result}, got {result}"


def test_perimeter_with_floats():
    a, b, c = 2.5, 4.5, 5.5
    expected_result = a + b + c
    result = perimeter(a, b, c)
    assert math.isclose(
        result, expected_result, rel_tol=1e-9
    ), f"Expected {expected_result}, got {result}"


def test_perimeter_with_negative_side():
    a, b, c = 3, -4, 5
    with pytest.raises(ValueError, match="Input must be greater than or equal to 0"):
        perimeter(a, b, c)


def test_perimeter_with_invalid_type():
    a, b, c = 3, "side", 5
    with pytest.raises(ValueError, match="Input must be a number"):
        perimeter(a, b, c)