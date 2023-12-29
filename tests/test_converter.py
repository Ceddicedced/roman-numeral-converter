import pytest

from roman_numerals_converter import (
    convert_from_roman,
    convert_to_roman,
    random_roman,
    replace_roman_numerals_in_text,
)
from roman_numerals_converter.converter import replace_integers_with_roman_numerals


# Tests for convert_to_roman
def test_convert_to_roman_valid():
    assert convert_to_roman(1) == "I"
    assert convert_to_roman(3999) == "MMMCMXCIX"


def test_convert_to_roman_invalid():
    with pytest.raises(ValueError):
        convert_to_roman(0)
    with pytest.raises(ValueError):
        convert_to_roman(4000)


# Tests for convert_from_roman
def test_convert_from_roman_valid():
    assert convert_from_roman("I") == 1
    assert convert_from_roman("MMMCMXCIX") == 3999


def test_convert_from_roman_invalid():
    with pytest.raises(ValueError):
        convert_from_roman("IIII")
    with pytest.raises(ValueError):
        convert_from_roman("MMMM")


# Tests for replace_roman_numerals_in_text
def test_replace_roman_numerals_in_text():
    assert replace_roman_numerals_in_text("XX in Roman is 20.") == "20 in Roman is 20."
    assert (
        replace_roman_numerals_in_text("No roman numerals here.")
        == "No roman numerals here."
    )
    assert (
        replace_roman_numerals_in_text(
            "In MMXVIII, the event took place on VII of June."
        )
        == "In 2018, the event took place on 7 of June."
    )
    assert (
        replace_roman_numerals_in_text("The movie title is Rocky II.")
        == "The movie title is Rocky 2."
    )


def test_replace_integers_with_roman_numerals():
    assert (
        replace_integers_with_roman_numerals("The year 2020 was challenging.")
        == "The year MMXX was challenging."
    )
    assert (
        replace_integers_with_roman_numerals("Apollo 13 is a famous mission.")
        == "Apollo XIII is a famous mission."
    )


# Tests for random_roman
def test_random_roman_valid():
    roman, number = random_roman()
    assert 1 <= number <= 3999
    assert convert_from_roman(roman) == number


def test_random_roman_invalid() -> None:
    with pytest.raises(ValueError):
        random_roman(0, 0)
    with pytest.raises(ValueError):
        random_roman(4000, 4000)
    with pytest.raises(ValueError):
        random_roman(2, 1)
