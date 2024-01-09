from abc import ABC, abstractmethod
from typing import Any, Union

from dsl_parser import Parser

from DSL.dsl_command import Command
from DSL.dsl_variable import VariableStore
from roman_numerals_converter import RomanNumeral


class AbstractHandler(ABC):
    def __init__(self, store: VariableStore, parser: Parser) -> None:
        self.store: VariableStore = store
        self.parser: Parser = parser

    @abstractmethod
    def handle(self, command: Command) -> Any:
        pass


class HandlerError(Exception):
    def __init__(self, op: str, message: str) -> None:
        self.message = f"Error in operation '{op}': {message}"

    def __str__(self) -> str:
        return self.message


class ArithmeticHandler(AbstractHandler):
    """
    A handler for arithmetic operations.

    This handler performs arithmetic operations such as addition, subtraction,
    multiplication, and division. It takes in a command object and returns the
    result of the operation.

    Args:
        store (VariableStore): The variable store used for storing the result.
        parser (Parser): The parser used for parsing the command arguments.

    Returns:
        Union[RomanNumeral, object, int]: The result of the arithmetic operation.

    Raises:
        ValueError: If an invalid operation is specified.
        HandlerError: If the number of arguments is invalid or if an error occurs during the operation.
    """  # noqa: E501

    def __init__(self, store: VariableStore, parser: Parser) -> None:
        self.store = store
        self.parser = parser

    def handle(self, command: Command) -> Union[RomanNumeral, object, int]:
        op = command.op
        if op not in ["add", "subtract", "multiply", "divide"]:
            raise ValueError("Invalid operation")

        if 2 <= len(command.args) <= 3:  # add a b c  - add a and b and store in c
            raise HandlerError(op, "Invalid number of arguments")

        arg1 = command.args[0]
        arg2 = command.args[1]

        val1 = self.parser.parse(arg1)
        val2 = self.parser.parse(arg2)

        try:
            if op == "add":
                return val1 + val2
            elif op == "subtract":
                return val1 - val2
            elif op == "multiply":
                return val1 * val2
            elif op == "divide":
                return val1 / val2
            else:
                raise ValueError("Unknown operation")
        except TypeError as e:
            raise HandlerError(op, f"Invalid operation: {e}") from e


class AssignmentHandler(AbstractHandler):
    def __init__(self, store: VariableStore, parser: Parser) -> None:
        super().__init__(store, parser)
        self.parser = parser

    def handle(self, command: Command) -> None:
        if command.op != "set":
            raise HandlerError(command.op, "Invalid operation")

        if len(command.args) != 2:
            raise HandlerError(command.op, "Invalid number of arguments")

        var_name = command.args[0]
        value = self.parser.parse(command.args[1])
        self.store.set_variable(var_name, value)


class ConversionHandler(AbstractHandler):
    def __init__(self, store: VariableStore, parser: Parser) -> None:
        super().__init__(store, parser)

    def handle(self, command: Command) -> Union[int, RomanNumeral]:
        variable: RomanNumeral | int = self.parser.parse(command.args[0])
        if isinstance(variable, RomanNumeral):
            return variable.to_decimal()
        else:
            return RomanNumeral.from_decimal(variable)


class DisplayHandler(AbstractHandler):
    def __init__(self, store: VariableStore, parser: Parser) -> None:
        super().__init__(store, parser)

    def handle(self, command: Command) -> str:
        variable = self.parser.parse(command.args[0])
        return str(variable)
