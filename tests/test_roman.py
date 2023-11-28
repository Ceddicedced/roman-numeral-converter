import pytest
from click.testing import CliRunner

from roman.roman import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_to_roman(runner):
    # Test conversion of a few numbers to Roman numerals
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

    for number, expected_output in test_cases:
        result = runner.invoke(cli, ["to-roman", str(number)])
        assert result.exit_code == 0
        assert result.output.strip() == expected_output


def test_from_roman(runner):
    # Test conversion of a few Roman numerals to numbers
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
        result = runner.invoke(cli, ["from-roman", roman])
        assert result.exit_code == 0
        assert result.output.strip() == str(expected_output)


def test_to_roman_invalid_input(runner):
    # Test invalid integer input
    invalid_inputs = [-1, 0, 4000, 1.5, "abc"]
    for number in invalid_inputs:
        result = runner.invoke(cli, ["to-roman", str(number)])
        assert result.exception


def test_from_roman_invalid_input(runner):
    # Test invalid Roman numeral input
    invalid_inputs = ["IIII", "VV", "LL", "DD", "MMMM", "ABC"]
    for roman in invalid_inputs:
        result = runner.invoke(cli, ["from-roman", roman])
        assert result.exception


def test_equivalence(runner):
    # Test random equivalence between to-roman and from-roman

    for number in range(1, 3999):
        result = runner.invoke(cli, ["to-roman", str(number)])
        assert result.exit_code == 0
        roman = result.output.strip()
        result = runner.invoke(cli, ["from-roman", roman])
        assert result.exit_code == 0
        assert result.output.strip() == str(number)
