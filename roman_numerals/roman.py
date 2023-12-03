"""Roman numerals converter.
This script provides a command-line interface to convert numbers to Roman numerals and vice versa.
"""  # noqa: E501

import re

import click

# Regular expression for validating Roman numerals
ROMAN_REGEX = r"^(?=.)M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"


@click.group()
def cli() -> None:
    """Click group for the CLI.
    This group bundles the commands for converting to and from Roman numerals.
    """
    pass


@cli.command()
@click.argument("number", type=int)
def to_roman(number: int) -> None:
    """
    Convert a number to a Roman numeral.

    Args:
        number (int): A decimal number to be converted into Roman numeral.

    This function takes an integer and converts it into its Roman numeral representation.
    It checks if the number is within the permissible range (1-3999) and then converts it
    using defined Roman numeral mappings.
    """  # noqa: E501
    # Check that the number is within the valid range
    if not 0 < number < 4000:
        raise click.BadParameter("Please enter a number between 1 and 3999.")

    # Mapping of decimal numbers to Roman numerals
    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    # Conversion process
    roman = ""
    for value, numeral in roman_numerals:
        while number >= value:
            roman += numeral
            number -= value

    click.echo(roman)


@cli.command()
@click.argument("roman", type=str)
def from_roman(roman: str) -> None:
    """
    Convert a Roman numeral to a number.

    Args:
        roman (str): A Roman numeral to be converted into a decimal number.

    This function takes a Roman numeral and converts it into its decimal representation.
    It first validates the Roman numeral using a regular expression and then performs
    the conversion using defined mappings from Roman numerals to decimal numbers.
    """
    # Validate Roman numeral input
    if not re.search(ROMAN_REGEX, roman):
        raise click.BadParameter("Please enter a valid Roman numeral.")

    # Mapping of Roman numerals to decimal numbers
    roman_numerals: dict[str, int] = {
        "CM": 900,
        "CD": 400,
        "XC": 90,
        "XL": 40,
        "IX": 9,
        "IV": 4,
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    # Conversion process
    num = 0
    for key, value in roman_numerals.items():
        if key in roman:
            num += value * roman.count(key)
            roman = roman.replace(key, "")

    click.echo(num)


if __name__ == "__main__":
    cli()
