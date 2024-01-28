
# DSL Interpreter for Roman Numerals

## Overview
This DSL (Domain-Specific Language) interpreter is a component of the `roman_numerals` project. It is designed to convert and manipulate Roman numerals and integers, offering a range of operations including arithmetic calculations, conversions, and variable management.

## Features
- Conversion between Roman numerals and integers.
- Arithmetic operations with Roman numerals and integers (addition, subtraction, multiplication, division).
- Variable management for storing and retrieving values.

## Usage

### Starting the Interpreter
Run the interpreter module from within the `roman_numerals` project directory:
```
python -m roman_numerals.dsl_interpreter
```

### Commands
- `set <variable_name> = <value>`: Assign a Roman numeral or an integer value to a variable.
- `add <operand1> <operand2>`: Perform addition between two values (variables, integers, or Roman numerals).
- `subtract <operand1> <operand2>`: Perform subtraction between two values.
- `multiply <operand1> <operand2>`: Perform multiplication between two values.
- `divide <operand1> <operand2>`: Perform division between two values.
- `convert <value>`: Convert a value from Roman numeral to integer or vice versa.
- `display <variable_name>`: Display the value of a variable.

### Examples
```
> set a = X
> set b = 5
> add a b
Result: XV
> convert XV
Result: 15
```

## Documentation
For more detailed documentation, refer to the in-line comments and docstrings within the code.

## License
This project and its DSL interpreter are part of the `roman_numerals` project, which is licensed under the [MIT License](https://opensource.org/licenses/MIT).
