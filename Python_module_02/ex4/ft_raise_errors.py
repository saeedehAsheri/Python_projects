"""
This script demonstrates how to manually raise ValueError exceptions when
data does not meet specific validation rules.
"""


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    """
    Validates plant data. Raises ValueError if data is incorrect.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1 or water_level > 10:
        raise ValueError(
            f"Water level {water_level} is incorrect (min 1, max 10)"
        )

    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is incorrect (min 2, max 12)"
        )

    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Tests the validation function with good and bad data.
    """
    print("=== Garden Plant Health Checker ===")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        check_plant_health(None, 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
