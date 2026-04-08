"""
This script demonstrates how to use the finally block to ensure cleanup code,
like closing a system, runs even if an error occurs.
"""


def water_plants(plant_list: list) -> None:
    """
    Waters plants. Uses 'finally' to ensure cleanup happens after errors.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Tests that cleanup runs even when the list contains invalid data.
    """
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
