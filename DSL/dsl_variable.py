import re
from typing import Union

from roman_numerals_converter import ROMAN_REGEX, RomanNumeral


class Variable:
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
        if not Variable.valid_name(name):
            raise ValueError(
                f"Invalid variable name '{name}' - cannot be a Roman numeral"
            )
        self.variables[name] = Variable(name, value)

    def get_variable(self, name: str) -> Variable:
        if name not in self.variables:
            raise ValueError(f"Variable '{name}' not found.")
        return self.variables[name]
