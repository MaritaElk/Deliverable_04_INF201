from functools import total_ordering

@total_ordering
class Temperature:
    TOLERANCE = 1e-9

    def __init__(self, value: float, unit: str):
        unit = unit.upper()

        if unit not in ("C", "F", "K"):
            raise ValueError("Unit must be C, F, or K.")

        value = float(value)

        absolute_zero = {
            "C": -273.15,
            "F": -459.67,
            "K": 0.0
        }

        if value < absolute_zero[unit] - self.TOLERANCE:
            raise ValueError("Temperature cannot be below absolute zero.")

        self._value = value
        self._unit = unit

    @property
    def value(self) -> float:
        return self._value

    @property
    def unit(self) -> str:
        return self._unit

    def to_celsius(self) -> float:
        if self._unit == "C":
            return self._value
        elif self._unit == "F":
            return (self._value - 32) * 5 / 9
        else:
            return self._value - 273.15

    def to_fahrenheit(self) -> float:
        if self._unit == "C":
            return (self._value * 9 / 5) + 32
        elif self._unit == "F":
            return self._value
        else:
            return (self._value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        if self._unit == "C":
            return self._value + 273.15
        elif self._unit == "F":
            return (self._value - 32) * 5 / 9 + 273.15
        else:
            return self._value

    def convert_to(self, target_unit: str) -> "Temperature":
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
        return f"Temperature({self._value!r}, {self._unit!r})"

    def __str__(self) -> str:
        if self._unit == "K":
            return f"{self._value:.2f} K"
        return f"{self._value:.2f} °{self._unit}"

    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return abs(self.to_kelvin() - other.to_kelvin()) <= self.TOLERANCE

    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() < other.to_kelvin() - self.TOLERANCE


