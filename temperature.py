from functools import total_ordering

@total_ordering
class Temperature:
    """Represent a temperature in Celsius, Fahrenheit, or Kelvin."""

    TOLERANCE = 1e-9

    def __init__(self, value: float, unit: str = "C"):
        """Initialize a temperature with a value and unit.

        Args:
            value (float): The temperature value.
            unit (str): Temperature unit (C, F, or K). Defaults to C.

        Raises:
            ValueError: If the unit is invalid or the temperature
                is below absolute zero.
        """
        unit = unit.upper()

        if unit not in ("C", "F", "K"):
            raise ValueError("Unit must be C, F, or K.")

        value = float(value)

        absolute_zero = {
            "C": -273.15,
            "F": -459.67,
            "K": 0.0
        }

        if value < absolute_zero[unit]:
            raise ValueError("Temperature cannot be below absolute zero.")

        self._value = value
        self._unit = unit

    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the temperature unit."""
        return self._unit

    def to_celsius(self) -> float:
        """Return the temperature converted to Celsius."""
        if self._unit == "C":
            return self._value
        elif self._unit == "F":
            return (self._value - 32) * 5 / 9
        else:
            return self._value - 273.15

    def to_fahrenheit(self) -> float:
        """Return the temperature converted to Fahrenheit."""
        if self._unit == "C":
            return (self._value * 9 / 5) + 32
        elif self._unit == "F":
            return self._value
        else:
            return (self._value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        """Return the temperature converted to Kelvin."""
        if self._unit == "C":
            return self._value + 273.15
        elif self._unit == "F":
            return (self._value - 32) * 5 / 9 + 273.15
        else:
            return self._value

    def convert_to(self, target_unit: str) -> "Temperature":
        """Convert the temperature to a new Temperature instance.

        Args:
            target_unit (str): Target unit (C, F, or K), case-insensitive.

        Returns:
            Temperature: A new instance in the target unit.

        Raises:
            ValueError: If the target unit is invalid.
        """
        target_unit = target_unit.upper()

        if target_unit not in ("C", "F", "K"):
            raise ValueError("Unit must be C, F, or K.")

        if target_unit == "C":
            value = self.to_celsius()
        elif target_unit == "F":
            value = self.to_fahrenheit()
        else:
            value = self.to_kelvin()

        return Temperature(value, target_unit)

    def __repr__(self) -> str:
        """Return an unambiguous string representation of the temperature."""
        return f"Temperature({self._value!r}, {self._unit!r})"

    def __str__(self) -> str:
        """Return the temperature formatted with two decimal places."""
        if self._unit == "K":
            return f"{self._value:.2f} K"
        return f"{self._value:.2f} °{self._unit}"

    def __eq__(self, other):
        """Compare temperatures for equality within the specified tolerance."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return abs(self.to_kelvin() - other.to_kelvin()) <= self.TOLERANCE

    def __lt__(self, other):
        """Check if this temperature is lower than another, using tolerance."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() < other.to_kelvin() - self.TOLERANCE


