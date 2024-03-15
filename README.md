# JAVA-Syntax-Validator
This project aims to develop a custom lexer and parser in Python using PLY (Python Lex-Yacc) to validate common syntax in the Java programming language.

## Features

- **Custom Lexer**: Tokenizes input Java code according to defined regular expressions.
- **Custom Parser**: Parses tokenized input according to specified grammar rules to validate syntax.
- **Modular Design**: Easily extendable for adding more syntax validations.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/java-syntax-validator.git
    ```

2. Install the required Python packages:

    ```bash
    pip install ply
    ```
## Usage

### Running the Array Declaration Syntax Validation

1. Navigate to the project directory.
2. Run the following command:

    ```bash
    python code_array.py
    ```

3. Enter a sample array declaration statement when prompted, e.g. `int[] arr = new int[50];`.
4. The program will output whether the input statement is a valid Java array declaration or not.

### Running Other Syntax Validations

1. Repeat steps 2-4 from the above section, replacing `code_array.py` with the corresponding validator script (e.g., `code_construct.py`).

---

**Note:** This project is intended for educational purposes and may not cover the full spectrum of Java syntax. Use at your discretion.

