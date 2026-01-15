"""
This script demonstrates how to create custom exception classes for specific
garden-related errors and how to handle them.
"""


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_level(tank_liters: int) -> None:
    if tank_liters <= 0:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant_health(True)
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("Testing WaterError...")
    try:
        check_water_level(0)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("Testing catching all garden errors...")
    try:
        check_plant_health(True)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    try:
        check_water_level(0)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
