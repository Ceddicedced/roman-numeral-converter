class CommandError(Exception):
    pass


class Command:
    """
    Represents a command in a domain-specific language (DSL).

    Args:
        command (str): The command string.

    Attributes:
        command (str): The original command string.
        op (str): The operation of the command.
        args (list[str]): The arguments of the command.

    Properties:
        is_assignment (bool): Indicates if the command is an assignment operation.
        is_arithmetic (bool): Indicates if the command is an arithmetic operation.
        is_conversion (bool): Indicates if the command is a conversion operation.
        is_display (bool): Indicates if the command is a display operation.
        is_valid (bool): Indicates if the command is a valid operation.
        operation (str): The type of operation.

    Raises:
        CommandError: If the command is invalid.

    Example:
        command = Command("set a = X; set b = 5; add a and b")
    """

    __commands: list[str] = [
        "set",
        "add",
        "subtract",
        "multiply",
        "divide",
        "convert",
        "display",
    ]

    def __init__(self, command: str) -> None:
        command = command.strip()
        if command.endswith(";"):
            command = command[:-1]

        parts: list[str] = command.split()
        if len(parts) < 2:
            raise CommandError("Invalid command - must have at least 2 parts")

        self.command = command
        self.op = parts[0]

        if not self.is_valid:
            raise CommandError("Invalid command - unknown operation")

        self.args = parts[1:]

    @property
    def is_assignment(self) -> bool:
        return self.op == "set"

    @property
    def is_arithmetic(self) -> bool:
        return self.op in ["add", "subtract", "multiply", "divide"]

    @property
    def is_conversion(self) -> bool:
        return self.op == "convert"

    @property
    def is_display(self) -> bool:
        return self.op == "display"

    @property
    def is_valid(self) -> bool:
        return any(
            [
                self.is_assignment,
                self.is_arithmetic,
                self.is_conversion,
                self.is_display,
            ]
        )

    @property
    def operation(self) -> str:
        if self.is_assignment:
            return "assignment"
        elif self.is_arithmetic:
            return "arithmetic"
        elif self.is_conversion:
            return "conversion"
        elif self.is_display:
            return "display"
        else:
            return "unknown"
