
from math import gcd

class Fraction:
    """
    A class representing mathematical fractions.

    The numerator and denominator must be integers.
    The denominator must always be positive.
    Fractions are automatically simplified.
    """

    def __init__(self, numerator, denominator):
        """
        Initialise a Fraction object.

        Args:
            numerator (int): The numerator of the fraction.
            denominator (int): The denominator of the fraction.

        Raises:
            TypeError: If numerator or denominator is not an integer.
            ValueError: If denominator is zero.
        """
        # Check that both values are integers
        if not isinstance(numerator, int) or isinstance(numerator, bool):
            raise TypeError("Numerator must be an integer")

        if not isinstance(denominator, int) or isinstance(denominator, bool):
            raise TypeError("Denominator must be an integer")

        # Denominator cannot be zero
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        # Make sure the denominator is positive
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Simplify the fraction

        common_divisor = gcd(numerator, denominator)

        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __str__(self):
        """
        Return a human-readable string representation of the fraction.

        Returns:
            str: The fraction formatted as numerator/denominator.
        """
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """
        Return an unambiguous string representation of the Fraction object.

        Returns:
            str: A string that shows how to recreate the Fraction object.
        """
        return f"Fraction({self.numerator}, {self.denominator})"
    
    def __eq__(self, other):
        """
        Check whether two fractions are equal.

        Fractions are compared by their simplified
        numerator and denominator.

        Returns:
            bool: True if the fractions are equal.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __ne__(self, other):
        """
        Check whether two fractions are not equal.

        Returns:
            bool: True if the fractions are different,
                  otherwise False.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Check whether this fraction is smaller than another fraction.

        Cross multiplication is used to compare the fractions
        without converting them to floating-point numbers.

        Returns:
            bool: True if this fraction is smaller than the other.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )

    def __le__(self, other):
        """
        Check whether this fraction is smaller than or equal to another fraction.

        Returns:
            bool: True if this fraction is smaller than or equal to the other.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        return self < other or self == other

    def __gt__(self, other):
        """
        Check whether this fraction is greater than another fraction.

        Cross multiplication is used to compare the fractions
        without converting them to floating-point numbers.

        Returns:
            bool: True if this fraction is greater than the other.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            > other.numerator * self.denominator
        )

    def __ge__(self, other):
        """
        Check whether this fraction is greater than or equal to another fraction.

        Returns:
            bool: True if this fraction is greater than or equal to the other.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        return self > other or self == other

    def __add__(self, other):
        """
        Add two fractions together.

        Returns:
            Fraction: A new Fraction object representing the sum.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        # Calculate the new numerator
        new_numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )

        # Calculate the new denominator
        new_denominator = self.denominator * other.denominator

        # Create and return the resulting fraction
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        Subtract one fraction from another.

        Returns:
            Fraction: A new Fraction object representing the difference.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        # Calculate the new numerator
        new_numerator = (
            self.numerator * other.denominator
            - other.numerator * self.denominator
        )

        # Calculate the new denominator
        new_denominator = self.denominator * other.denominator

        # Create and return the resulting fraction
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """
        Multiply two fractions.

        Returns:
            Fraction: A new Fraction object representing the product.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        # Calculate the new numerator
        new_numerator = self.numerator * other.numerator

        # Calculate the new denominator
        new_denominator = self.denominator * other.denominator

        # Create and return the resulting fraction
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """
        Divide one fraction by another.

        Returns:
            Fraction: A new Fraction object representing the quotient.

        Raises:
            ZeroDivisionError: If the other fraction is zero.
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        # Check that the other fraction is not zero
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        # Calculate the new numerator
        new_numerator = self.numerator * other.denominator

        # Calculate the new denominator
        new_denominator = self.denominator * other.numerator

        # Create and return the resulting fraction
        return Fraction(new_numerator, new_denominator)