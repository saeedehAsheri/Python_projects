"""
This script intentionally triggers and catches various specific Python errors
like ValueError, ZeroDivisionError, FileNotFoundError, and KeyError.
"""


def garden_operations(error_type: str) -> None:
    """
    Intentionally breaks code (div by zero, missing file) based on input.
    """
    if error_type == "value":
        int("abc")

    elif error_type == "zero":
        2 / 0

    elif error_type == "file":
        open("does_not_exist.txt", "r")

    elif error_type == "key":
        plants = {"rose": "red"}
        plants["missing_plant"]


def test_error_types() -> None:
    """
    Runs broken operations and catches specific error types separately.
    """
    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as error:
        print(f"Caught ValueError: {error}")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as error:
        print(f"Caught KeyError: {error}")

    print("Testing multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
