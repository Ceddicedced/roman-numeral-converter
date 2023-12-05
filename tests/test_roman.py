import pytest
from click.testing import CliRunner

from roman_numerals_converter import RomanError, RomanNumeral


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_roman_numeral_to_decimal():
    # Test conversion of Roman numerals to decimal numbers
    test_cases = [
        ("I", 1),
        ("IV", 4),
        ("IX", 9),
        ("XII", 12),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        ("MMMCMXCIX", 3999),
    ]

    for roman, expected_output in test_cases:
        roman_numeral = RomanNumeral(roman)
        assert roman_numeral.to_decimal() == expected_output


def test_roman_numeral_to_string():
    # Test conversion of Roman numerals to strings
    test_cases = [
        ("I", "I"),
        ("IV", "IV"),
        ("IX", "IX"),
        ("XII", "XII"),
        ("L", "L"),
        ("C", "C"),
        ("D", "D"),
        ("M", "M"),
        ("MMMCMXCIX", "MMMCMXCIX"),
    ]

    for roman, expected_output in test_cases:
        roman_numeral = RomanNumeral(roman)
        assert str(roman_numeral) == expected_output


def test_decimal_to_roman():
    # Test conversion of decimal numbers to Roman numerals
    test_cases = [
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (12, "XII"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
        (3999, "MMMCMXCIX"),
    ]

    for decimal, expected_output in test_cases:
        roman_numeral = RomanNumeral.from_decimal(decimal)
        assert str(roman_numeral) == expected_output


def test_invalid_roman_input():
    # Test invalid Roman numeral input
    invalid_inputs = ["IIII", "VV", "LL", "DD", "MMMM", "ABC"]
    for roman in invalid_inputs:
        with pytest.raises(RomanError):
            RomanNumeral(roman)


def test_invalid_decimal_input():
    # Test invalid decimal input
    invalid_inputs = [-1, 0, 4000, 1.5, "abc"]
    for decimal in invalid_inputs:
        with pytest.raises(RomanError):
            RomanNumeral.from_decimal(decimal)
