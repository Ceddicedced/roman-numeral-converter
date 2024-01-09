import re
from typing import Union

from roman_numerals_converter import ROMAN_REGEX, RomanNumeral


class Variable:
    """
    Represents a variable with a name and a value.

    Attributes:
        name (str): The name of the variable.
        value (Union[RomanNumeral, int]): The value of the variable, which can be either a Roman numeral or an integer.
        type: The type of the value.

    Methods:
        __repr__: Returns a string representation of the variable.
        valid_name: Checks if the variable name is valid.
    """  # noqa: E501

    def __init__(self, name: str, value: Union[RomanNumeral, int]) -> None:
        self.name: str = name
        self.value: RomanNumeral | int = value
        self.type = type(value)

    def __repr__(self) -> str:
        return f"{self.name} = {self.value}"

    @staticmethod
    def valid_name(name: str) -> bool:
        return re.match(ROMAN_REGEX, name) is None


class VariableStore:
    """A class that represents a store for variables.

    Attributes:
        variables (dict[str, Variable]): A dictionary that stores variables, where the key is the variable name and the value is the Variable object.
    """  # noqa: E501

    def __init__(self) -> None:
        self.variables: dict[str, Variable] = {}

    @property
    def variable_names(self) -> list[str]:
        return list(self.variables.keys())

    @property
    def variable_values(self) -> list[Union[RomanNumeral, int]]:
        return [variable.value for variable in self.variables.values()]

    @property
    def is_empty(self) -> bool:
        return len(self.variables) == 0

    def __repr__(self) -> str:
        return "\n".join([str(variable) for variable in self.variables.values()])

    def __contains__(self, name: str) -> bool:
        return name in self.variables

    def set_variable(self, name: str, value: Union[RomanNumeral, int]) -> None:
        """Set the value of a variable.

        Args:
            name (str): The name of the variable.
            value (Union[RomanNumeral, int]): The value of the variable.

        Raises:
            ValueError: If the variable name is invalid (cannot be a Roman numeral).
        """
        if not Variable.valid_name(name):
            raise ValueError(
                f"Invalid variable name '{name}' - cannot be a Roman numeral"
            )
        self.variables[name] = Variable(name, value)

    def get_variable(self, name: str) -> Variable:
        """Get the value of a variable.

        Args:
            name (str): The name of the variable.

        Returns:
            Variable: The Variable object representing the variable.

        Raises:
            ValueError: If the variable is not found.
        """
        if name not in self.variables:
            raise ValueError(f"Variable '{name}' not found.")
        return self.variables[name]
