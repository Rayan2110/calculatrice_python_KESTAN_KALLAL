# Calculator

A simple Python calculator that parses and evaluates infix mathematical expressions containing positive integers, floating-point numbers, and the operators `+`, `-`, and `*`, with correct operator precedence. This implementation uses the Shunting‑Yard algorithm to convert expressions to Reverse Polish Notation (RPN) and then evaluates the RPN.

## Features

* **Infix Parsing**: Supports numbers (integers and floats) and the operators `+`, `-`, and `*`.
* **Operator Precedence**: Correctly applies multiplication before addition and subtraction.
* **Parentheses**: Handles nested expressions using parentheses.
* **Clean Code**: Readable, modular design with clear method responsibilities.
* **Error Handling**: Detects malformed expressions and unknown tokens.

## Installation

1. Clone this repository:

   ```bash
   git clone  https://github.com/Rayan2110/isep-cleancode-calculator
   ```
2. Navigate to the project directory:

   ```bash
   cd isep-calculator-python
   ```
3. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. No external dependencies are required—the calculator relies only on Python’s standard library.

## Usage

Import and use the `Calculator` class in your Python code:

```python
from calculator import Calculator

calc = Calculator()
result = calc.evaluate("2 + 3 * 4 - (1 + 2)")
print(result)  # Output: 11.0
```

You can also run the provided examples directly:

```bash
python calculator.py
```

## Running Tests

A suite of unit tests using Python’s `unittest` framework is included in `test_calculator.py`.

To run the tests, execute:

```bash
python -m unittest test_calculator.py -v
```

All base tests must pass. Uncomment and enable additional tests in `test_calculator.py` to earn bonus features (negative numbers and parentheses).

## Project Structure

```
├── calculator.py       # Main Calculator implementation
├── test_calculator.py  # Unit tests for Calculator
├── README.md           # Project documentation (this file)
└── LICENSE             # License information
```

## Contributing

Feel free to open issues or submit pull requests for improvements. When contributing:

* Follow the existing code style and structure.
* Write unit tests for new features or edge cases.
* Ensure all tests pass before submitting.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
