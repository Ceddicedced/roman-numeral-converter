from typing import Any, List

from dsl_parser import Parser

from DSL.dsl_command import Command
from DSL.dsl_handlers import (
    AbstractHandler,
    ArithmeticHandler,
    AssignmentHandler,
    ConversionHandler,
    DisplayHandler,
)
from DSL.dsl_variable import VariableStore


class DSLInterpreter:
    """
    A class that interprets and executes DSL commands.

    Attributes:
        store (VariableStore): The variable store used to store and retrieve variables.
        parser (Parser): The parser used to parse DSL commands.
        handlers (dict[str, AbstractHandler]): A dictionary of command handlers.

    Methods:
        execute(command_line: str) -> List[Any]: Executes the DSL commands in the given command line.

    """  # noqa: E501

    def __init__(self) -> None:
        self.store = VariableStore()
        self.parser = Parser(self.store)
        self.handlers: dict[str, AbstractHandler] = {
            "assignment": AssignmentHandler(self.store, self.parser),
            "arithmetic": ArithmeticHandler(self.store, self.parser),
            "conversion": ConversionHandler(self.store, self.parser),
            "display": DisplayHandler(self.store, self.parser),
        }

    def execute(self, command_line: str) -> List[Any]:
        """
        Executes the DSL commands in the given command line.

        Args:
            command_line (str): The command line containing DSL commands.

        Returns:
            List[Any]: A list of results from executing the commands.

        """
        command_statements = command_line.split(";")
        results: List[Any] = []
        for statement in command_statements:
            try:
                command = Command(statement)
                handler: AbstractHandler = self.handlers[command.operation]  # noqa: E501
                result = handler.handle(command)
                if result is not None:
                    results.append(result)
            except ValueError as e:
                print(f"Error in command '{statement}': {e}")
        return results


def main() -> None:
    interpreter = DSLInterpreter()
    while True:
        try:
            command_line = input("> ")
            results = interpreter.execute(command_line)
            for result in results:
                if result is not None:
                    print("Result:", result)
        except Exception as e:
            print("Error:", f"{e}")


if __name__ == "__main__":
    main()
