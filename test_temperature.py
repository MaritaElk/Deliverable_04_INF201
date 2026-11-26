import pytest
from temperature import Temperature


def test_temperature_initialization():
    """Test initialization with a valid value and unit."""
    temp = Temperature(25, "C")

    assert temp.value == 25.0
    assert temp.unit == "C"

@pytest.mark.parametrize("unit", [
    "X",
    "Celsius",
    "Fahrenheit",
    "Kelvin",
    "",
    "CF",
])

def test_invalid_unit(unit):
    """Test that invalid units raise ValueError."""
    with pytest.raises(ValueError):
        Temperature(25, unit)

@pytest.mark.parametrize("value, unit", [
    (-274, "C"),
    (-460, "F"),
    (-1, "K"),
])
def test_below_absolute_zero(value, unit):
    """Test that temperatures below absolute zero raise ValueError."""
    with pytest.raises(ValueError):
        Temperature(value, unit)

@pytest.mark.parametrize("value, unit", [
    (-273.15 - 1e-10, "C"),
    (-459.67 - 1e-10, "F"),
    (-1e-10, "K"),
])
def test_just_below_absolute_zero(value, unit):
    """Test that temperatures just below absolute zero raise ValueError."""
    with pytest.raises(ValueError):
        Temperature(value, unit)

def test_read_only_attributes():
    """Test that value and unit cannot be modified."""
    temp = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temp.value = 100

    with pytest.raises(AttributeError):
        temp.unit = "F"

    assert temp.value == 25.0
    assert temp.unit == "C"

def test_default_unit():
    """Test that Celsius is used as the default unit."""
    temp = Temperature(25)

    assert temp.value == 25.0
    assert temp.unit == "C"

@pytest.mark.parametrize("unit, expected", [
    ("C", "C"),
    ("c", "C"),
    ("F", "F"),
    ("f", "F"),
    ("K", "K"),
    ("k", "K"),
])
def test_case_insensitive_units(unit, expected):
    """Test that temperature units are case-insensitive."""
    temp = Temperature(25, unit)

    assert temp.unit == expected

@pytest.mark.parametrize("celsius, fahrenheit, kelvin", [
    (-273.15, -459.67, 0.0),
    (-40.0, -40.0, 233.15),
    (0.0, 32.0, 273.15),
    (37.0, 98.6, 310.15),
    (100.0, 212.0, 373.15),
])
def test_temperature_conversions(celsius, fahrenheit, kelvin):
    """Test conversions between all units at reference temperatures."""
    for value, unit in [
        (celsius, "C"),
        (fahrenheit, "F"),
        (kelvin, "K"),
    ]:
        temp = Temperature(value, unit)

        assert temp.to_celsius() == pytest.approx(celsius, abs=1e-9, rel=0)
        assert temp.to_fahrenheit() == pytest.approx(fahrenheit, abs=1e-9, rel=0)
        assert temp.to_kelvin() == pytest.approx(kelvin, abs=1e-9, rel=0)

@pytest.mark.parametrize("value", [
    -273.15,
    -40,
    0,
    25,
    37,
    100,
])
def test_round_trip_conversion(value):
    """Test that round-trip conversions preserve the original temperature."""
    original = Temperature(value, "C")

    fahrenheit = original.convert_to("F")
    kelvin = fahrenheit.convert_to("K")
    result = kelvin.convert_to("C")

    assert result == original
    assert result.unit == "C"
    assert result.value == pytest.approx(value, abs=1e-9, rel=0)

def test_cross_unit_comparisons():
    """Test comparison operators across different temperature units."""
    cold = Temperature(0, "C")
    equal = Temperature(32, "F")
    warm = Temperature(300, "K")

    assert cold == equal
    assert cold != warm

    assert cold < warm
    assert cold <= equal

    assert warm > cold
    assert equal >= cold

@pytest.mark.parametrize("value, unit, expected_str, expected_repr", [
    (25.0, "C", "25.00 °C", "Temperature(25.0, 'C')"),
    (77.0, "F", "77.00 °F", "Temperature(77.0, 'F')"),
    (298.15, "K", "298.15 K", "Temperature(298.15, 'K')"),
])
def test_temperature_formatting(value, unit, expected_str, expected_repr):
    """Test the string and representation formats of temperatures."""
    temp = Temperature(value, unit)

    assert str(temp) == expected_str
    assert repr(temp) == expected_repr

@pytest.mark.parametrize("method", [
    "__eq__",
    "__ne__",
    "__lt__",
    "__le__",
    "__gt__",
    "__ge__",
])
def test_not_implemented(method):
    """Test that comparisons with non-Temperature objects return NotImplemented."""
    temp = Temperature(25, "C")

    result = getattr(temp, method)(25)

    assert result is NotImplemented

@pytest.mark.parametrize("target_unit, expected_value, expected_unit", [
    ("C", 25.0, "C"),
    ("f", 77.0, "F"),
    ("k", 298.15, "K"),
])
def test_convert_to(target_unit, expected_value, expected_unit):
    """Test conversion to a new Temperature instance."""
    original = Temperature(25, "C")

    converted = original.convert_to(target_unit)

    assert isinstance(converted, Temperature)
    assert converted is not original

    assert converted.value == pytest.approx(expected_value, abs=1e-9, rel=0)
    assert converted.unit == expected_unit

    assert original.value == 25.0
    assert original.unit == "C"

@pytest.mark.parametrize("target_unit", [
    "X",
    "Celsius",
    "",
])
def test_convert_to_invalid_unit(target_unit):
    """Test that invalid target units raise ValueError."""
    temp = Temperature(25, "C")

    with pytest.raises(ValueError):
        temp.convert_to(target_unit)

@pytest.mark.parametrize("value, unit", [
    (-273.15, "C"),
    (-459.67, "F"),
    (0.0, "K"),
])
def test_absolute_zero(value, unit):
    """Test that absolute zero is valid in all temperature units."""
    temp = Temperature(value, unit)

    assert temp.to_kelvin() == pytest.approx(0.0, abs=1e-9, rel=0)

def test_comparison_tolerance():
    """Test temperature comparisons within the floating-point tolerance."""
    temp1 = Temperature(20.0, "C")
    temp2 = Temperature(20.0 + 1e-10, "C")

    assert temp1 == temp2
    assert not (temp1 != temp2)

    assert not (temp1 < temp2)
    assert temp1 <= temp2

    assert not (temp1 > temp2)
    assert temp1 >= temp2