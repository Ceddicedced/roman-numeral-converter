import re
from typing import Union

from DSL.dsl_variable import VariableStore
from roman_numerals_converter import ROMAN_REGEX, RomanNumeral


class Parser:
    """
    A class that parses values into Roman numerals, integers, or variables.

    Args:
        store (VariableStore): The variable store used for retrieving variable values.

    Attributes:
        store (VariableStore): The variable store used for retrieving variable values.
    """

    def __init__(self, store: VariableStore) -> None:
        self.store = store

    def parse(self, value: str) -> Union[RomanNumeral, int]:
        """
        Parses the given value into a Roman numeral, integer, or variable value.

        Args:
            value (str): The value to be parsed.

        Returns:
            Union[RomanNumeral, int]: The parsed value.

        Raises:
            ValueError: If the value cannot be parsed into a valid Roman numeral, integer, or variable.
        """  # noqa: E501
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
        """
        Checks if the given value is a valid Roman numeral.

        Args:
            value (str): The value to be checked.

        Returns:
            bool: True if the value is a valid Roman numeral, False otherwise.
        """
        return re.match(ROMAN_REGEX, value) is not None

    @staticmethod
    def is_valid_integer(value: str) -> bool:
        """
        Checks if the given value is a valid integer.

        Args:
            value (str): The value to be checked.

        Returns:
            bool: True if the value is a valid integer, False otherwise.
        """
        return value.isdigit()

    def is_valid_variable(self, value: str) -> bool:
        """
        Checks if the given value is a valid variable.

        Args:
            value (str): The value to be checked.

        Returns:
            bool: True if the value is a valid variable, False otherwise.
        """
        return value in self.store


class CommandError(Exception):
    pass
