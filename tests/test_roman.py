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


def test_invalid_str_input():
    # Test invalid Roman numeral input
    invalid_inputs = [1, 1.5, ["I"], {"I": 1}]
    for roman in invalid_inputs:
        with pytest.raises(RomanError):
            RomanNumeral(roman)


def test_roman_numeral_equality():
    # Test equality of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("X")
    roman3 = RomanNumeral("V")
    assert roman1 == roman2
    assert roman1 != roman3
    assert roman1 == "X"
    assert roman1 != "V"
    assert roman1 == 10
    assert roman1 != 5

    # Test comparison of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("V")
    roman3 = RomanNumeral("L")
    assert roman1 < roman3
    assert roman1 > roman2
    assert roman1 <= roman1
    assert roman1 >= roman2
    assert roman1 < "L"
    assert roman1 > "V"
    assert roman1 <= "X"
    assert roman1 >= "X"
    assert roman1 < 50
    assert roman1 > 5
    assert roman1 <= 10
    assert roman1 >= 10


def test_roman_numeral_addition():
    # Test addition of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("V")
    roman3 = RomanNumeral("L")
    assert roman1 + roman2 == 15
    assert roman1 + roman3 == 60
    assert roman1 + "V" == 15
    assert roman1 + "L" == 60
    assert "X" + roman2 == "XV"
    assert "X" + roman3 == "XL"
    assert roman1 + 5 == 15
    assert roman1 + 50 == 60


def test_roman_numeral_reverse_addition():
    # Test reverse addition of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("V")
    roman3 = RomanNumeral("L")
    assert roman2 + roman1 == 15
    assert roman3 + roman1 == 60
    assert "V" + roman1 == "VX"
    assert "L" + roman1 == "LX"
    assert 5 + roman1 == 15
    assert 50 + roman1 == 60


def test_roman_numeral_addition_out_of_range():
    # Test addition of RomanNumeral objects that result in values outside the valid range  # noqa: E501
    roman1 = RomanNumeral("MMMCMXCIX")
    roman2 = RomanNumeral("I")
    with pytest.raises(AssertionError):
        roman1 + roman2
    with pytest.raises(AssertionError):
        roman2 + roman1
    with pytest.raises(AssertionError):
        roman1 + "I"
    with pytest.raises(AssertionError):
        roman1 + 1


def test_roman_numeral_representation():
    # Test string representation of RomanNumeral objects
    roman = RomanNumeral("X")
    assert str(roman) == "X"
    assert repr(roman) == "RomanNumeral('X')"
