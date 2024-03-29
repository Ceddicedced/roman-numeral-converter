import pytest

from roman_numerals_converter import RomanError, RomanNumeral


def test_roman_numeral_to_decimal() -> None:
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


def test_roman_numeral_to_string() -> None:
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


def test_decimal_to_roman() -> None:
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


def test_invalid_roman_input() -> None:
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
            RomanNumeral.from_decimal(decimal)  # type: ignore


def test_invalid_str_input():
    # Test invalid Roman numeral input
    invalid_inputs = [1, 1.5, ["I"], {"I": 1}]
    for roman in invalid_inputs:
        with pytest.raises(RomanError):
            RomanNumeral(roman)  # type: ignore


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


def test_roman_numeral_subtraction():
    # Test subtraction of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("V")
    roman3 = RomanNumeral("L")
    assert roman3 - roman1 == 40
    assert roman3 - roman2 == 45
    assert roman3 - "X" == 40
    assert roman3 - "V" == 45
    assert roman3 - 10 == 40
    assert roman3 - 5 == 45


def test_roman_numeral_reverse_subtraction():
    # Test reverse subtraction of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("V")
    roman3 = RomanNumeral("L")
    assert 10 - roman2 == 5
    assert 10 - roman3 == -40
    assert 5 - roman1 == -5
    assert 50 - roman1 == 40


def test_roman_numeral_multiplication():
    # Test multiplication of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("V")
    roman3 = RomanNumeral("L")
    assert roman1 * roman2 == 50
    assert roman1 * roman3 == 500
    assert roman1 * "V" == 50
    assert roman1 * "L" == 500
    assert "X" * roman2 == 50
    assert "X" * roman3 == 500
    assert roman1 * 5 == 50
    assert roman1 * 50 == 500


def test_roman_numeral_reverse_multiplication():
    # Test reverse multiplication of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("V")
    roman3 = RomanNumeral("L")
    assert roman2 * roman1 == 50
    assert roman3 * roman1 == 500
    assert "V" * roman1 == 50
    assert "L" * roman1 == 500
    assert 5 * roman1 == 50
    assert 50 * roman1 == 500


def test_roman_numeral_division():
    # Test division of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("V")
    roman3 = RomanNumeral("L")
    assert roman3 / roman1 == 5
    assert roman3 / roman2 == 10
    assert roman3 / "X" == 5
    assert roman3 / "V" == 10
    assert roman3 / 10 == 5
    assert roman3 / 5 == 10


def test_roman_numeral_reverse_division():
    # Test reverse division of RomanNumeral objects
    roman1 = RomanNumeral("X")
    roman2 = RomanNumeral("V")
    roman3 = RomanNumeral("L")
    assert "X" / roman2 == 2
    assert "X" / roman3 == 0.2
    assert 10 / roman2 == 2
    assert 10 / roman3 == 0.2
    assert 5 / roman1 == 0.5
    assert 50 / roman1 == 5


def test_roman_numeral_addition_out_of_range():
    # Test addition of RomanNumeral objects that result in values outside the valid range  # noqa: E501
    roman1 = RomanNumeral("MMMCMXCIX")
    roman2 = RomanNumeral("I")
    with pytest.raises(AssertionError):
        roman1 + roman2  # type: ignore
    with pytest.raises(AssertionError):
        roman2 + roman1  # type: ignore
    with pytest.raises(AssertionError):
        roman1 + "I"  # type: ignore
    with pytest.raises(AssertionError):
        roman1 + 1  # type: ignore


def test_roman_numeral_unsupported_operations():
    # Test unsupported operations
    roman = RomanNumeral("X")
    with pytest.raises(TypeError):
        roman // roman  # type: ignore
    with pytest.raises(TypeError):
        roman // "V"  # type: ignore
    with pytest.raises(TypeError):
        roman // 5  # type: ignore
    with pytest.raises(TypeError):
        roman % roman  # type: ignore
    with pytest.raises(TypeError):
        roman % "V"  # type: ignore
    with pytest.raises(TypeError):
        roman % 5  # type: ignore
    with pytest.raises(TypeError):
        roman**roman  # type: ignore
    with pytest.raises(TypeError):
        roman ** "V"  # type: ignore
    with pytest.raises(TypeError):
        roman**5  # type: ignore


def test_roman_numeral_not_implemented():
    roman = RomanNumeral("V")
    for obj in [1.5, ["I"], {"I": 1}]:
        assert roman.__eq__(obj) is NotImplemented
        assert roman.__ne__(obj) is NotImplemented
        assert roman.__le__(obj) is NotImplemented
        assert roman.__lt__(obj) is NotImplemented
        assert roman.__ge__(obj) is NotImplemented
        assert roman.__gt__(obj) is NotImplemented
        assert roman.__add__(obj) is NotImplemented
        assert roman.__radd__(obj) is NotImplemented
        assert roman.__sub__(obj) is NotImplemented
        assert roman.__rsub__(obj) is NotImplemented
        assert roman.__mul__(obj) is NotImplemented
        assert roman.__rmul__(obj) is NotImplemented
        assert roman.__truediv__(obj) is NotImplemented
        assert roman.__rtruediv__(obj) is NotImplemented


def test_roman_numeral_representation():
    # Test string representation of RomanNumeral objects
    roman = RomanNumeral("X")
    assert str(roman) == "X"
    assert repr(roman) == "RomanNumeral('X')"
