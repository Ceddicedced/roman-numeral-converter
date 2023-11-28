import re

import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument("number", type=int)
def to_roman(number):
    """Convert NUMBER to a Roman numeral."""

    # Check that the number is in the range 1-3999
    if not 0 < number < 4000:
        raise click.BadParameter("Please enter a number between 1 and 3999.")

    roman = ""

    # M: 1000
    if number >= 1000:
        roman += "M" * (number // 1000)
        number = number % 1000

    # CM: 900
    if number >= 900:
        roman += "CM"
        number = number % 900

    # D: 500
    if number >= 500:
        roman += "D"
        number = number % 500

    # CD: 400
    if number >= 400:
        roman += "CD"
        number = number % 400

    # C: 100
    if number >= 100:
        roman += "C" * (number // 100)
        number = number % 100

    # XC: 90
    if number >= 90:
        roman += "XC"
        number = number % 90

    # L: 50
    if number >= 50:
        roman += "L"
        number = number % 50

    # XL: 40
    if number >= 40:
        roman += "XL"
        number = number % 40

    # X: 10
    if number >= 10:
        roman += "X" * (number // 10)
        number = number % 10

    # IX: 9
    if number >= 9:
        roman += "IX"
        number = number % 9

    # V: 5
    if number >= 5:
        roman += "V"
        number = number % 5

    # IV: 4
    if number >= 4:
        roman += "IV"
        number = number % 4

    # I: 1
    if number >= 1:
        roman += "I" * number

    click.echo(roman)


@cli.command()
@click.argument("roman", type=str)
def from_roman(roman):
    """Convert ROMAN to a number."""

    # Check with regex that the input is a valid Roman numeral
    roman_regex = r"^(?=.)M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
    if not re.search(roman_regex, roman):
        raise click.BadParameter("Please enter a valid Roman numeral.")

    # Initialize the counter
    counter = 0

    ### Double-letter numerals

    # CM: 900
    if "CM" in roman:
        counter += 900
        roman = roman.replace("CM", "")

    # CD: 400
    if "CD" in roman:
        counter += 400
        roman = roman.replace("CD", "")

    # XC: 90
    if "XC" in roman:
        counter += 90
        roman = roman.replace("XC", "")

    # XL: 40
    if "XL" in roman:
        counter += 40
        roman = roman.replace("XL", "")

    # IX: 9
    if "IX" in roman:
        counter += 9
        roman = roman.replace("IX", "")

    # IV: 4
    if "IV" in roman:
        counter += 4
        roman = roman.replace("IV", "")

    # M: 1000
    if "M" in roman:
        counter += 1000 * roman.count("M")
        roman = roman.replace("M", "")

    # D: 500
    if "D" in roman:
        counter += 500
        roman = roman.replace("D", "")

    # C: 100
    if "C" in roman:
        counter += 100 * roman.count("C")
        roman = roman.replace("C", "")

    # L: 50
    if "L" in roman:
        counter += 50
        roman = roman.replace("L", "")

    # X: 10
    if "X" in roman:
        counter += 10 * roman.count("X")
        roman = roman.replace("X", "")

    # V: 5
    if "V" in roman:
        counter += 5
        roman = roman.replace("V", "")

    # I: 1
    if "I" in roman:
        counter += roman.count("I")
        roman = roman.replace("I", "")

    click.echo(counter)


if __name__ == "__main__":
    cli()
