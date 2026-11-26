import pytest
from my_fraction import Fraction


def test_fraction_initialization():
    """Test that a fraction is initialized with the correct numerator and denominator."""
    fraction = Fraction(1, 2)

    assert fraction.numerator == 1
    assert fraction.denominator == 2


def test_fraction_simplification():
    """Test that fractions are automatically simplified."""
    fraction = Fraction(2, 4)

    assert fraction == Fraction(1, 2)


def test_fraction_with_negative_denominator():
    """Test that a negative denominator is converted to a positive denominator."""
    fraction = Fraction(2, -4)

    assert fraction.numerator == -1
    assert fraction.denominator == 2


def test_fraction_zero_denominator():
    """Test that creating a fraction with a zero denominator raises ValueError."""
    with pytest.raises(ValueError):
        Fraction(1, 0)

def test_fraction_str():
    """Test the user-friendly string representation of a fraction."""
    fraction = Fraction(1, 2)

    assert str(fraction) == "1/2"


def test_fraction_repr():
    """Test the unambiguous representation of a Fraction object."""
    fraction = Fraction(1, 2)

    assert repr(fraction) == "Fraction(1, 2)"

def test_fraction_equal():
    """Test whether two equal fractions are recognized as equal."""
    assert Fraction(1, 2) == Fraction(2, 4)

def test_fraction_not_equal():
    """Test whether two different fractions are recognized as not equal."""
    assert Fraction(1, 2) != Fraction(1, 3)

def test_fraction_less_than():
    """Test whether one fraction is smaller than another."""
    assert Fraction(1, 3) < Fraction(1, 2)

def test_fraction_less_than_or_equal():
    """Test whether one fraction is smaller than or equal to another."""
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)

def test_fraction_greater_than():
    """Test whether one fraction is greater than another."""
    assert Fraction(1, 2) > Fraction(1, 3)

def test_fraction_greater_than_or_equal():
    """Test whether one fraction is greater than or equal to another."""
    assert Fraction(1, 2) >= Fraction(1, 3)
    assert Fraction(1, 2) >= Fraction(1, 2)

def test_fraction_addition():
    """Test the addition of two fractions."""
    result = Fraction(1, 2) + Fraction(1, 3)

    assert result == Fraction(5, 6)

def test_fraction_subtraction():
    """Test the subtraction of two fractions."""
    result = Fraction(1, 2) - Fraction(1, 3)

    assert result == Fraction(1, 6)

def test_fraction_multiplication():
    """Test the multiplication of two fractions."""
    result = Fraction(1, 2) * Fraction(2, 3)

    assert result == Fraction(1, 3)

def test_fraction_division():
    """Test the division of two fractions."""
    result = Fraction(1, 2) / Fraction(1, 3)

    assert result == Fraction(3, 2)

def test_fraction_division_by_zero():
    """Test that division by a zero fraction raises ZeroDivisionError."""
    fraction = Fraction(1, 2)
    zero = Fraction(0, 1)

    with pytest.raises(ZeroDivisionError):
        fraction / zero

def test_fraction_invalid_numerator():
    """Test that a non-integer numerator raises TypeError."""
    with pytest.raises(TypeError):
        Fraction("1", 2)

def test_fraction_invalid_denominator():
    """Test that a non-integer denominator raises TypeError."""
    with pytest.raises(TypeError):
        Fraction(1, "2")

def test_fraction_rejects_boolean_values():
    """Test that boolean values are not accepted as integers."""
    with pytest.raises(TypeError):
        Fraction(True, 2)

    with pytest.raises(TypeError):
        Fraction(1, False)