import re
from typing import Union

from DSL.dsl_variable import VariableStore
from roman_numerals_converter import ROMAN_REGEX, RomanNumeral


class Parser:
    def __init__(self, store: VariableStore) -> None:
        self.store = store

    def parse(self, value: str) -> Union[RomanNumeral, int]:
        if self.is_valid_roman_numeral(value):
            return RomanNumeral(value)
        elif self.is_valid_integer(value):
            return int(value)
        elif self.is_valid_variable(value):
            return self.store.get_variable(value).value
        else:
            raise ValueError(
                f"Invalid value '{value}' - cannot be parsed - Make sure it is a valid Roman numeral, integer or variable"  # noqa: E501
            )

    @staticmethod
    def is_valid_roman_numeral(value: str) -> bool:
        return re.match(ROMAN_REGEX, value) is not None

    @staticmethod
    def is_valid_integer(value: str) -> bool:
        return value.isdigit()

    def is_valid_variable(self, value: str) -> bool:
        return value in self.store


class CommandError(Exception):
    pass
