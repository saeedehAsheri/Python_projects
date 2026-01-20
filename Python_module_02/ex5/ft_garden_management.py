"""
This script combines all error handling concepts into a class-based garden
manager that adds plants, waters them, and checks their health.
"""


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        """
        Starts the garden manager with an empty list to hold plant names.
        """
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        """
        Adds a new plant name. Raises error if name is empty.
        """
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        """
        Waters plants. Always runs cleanup code (finally) even if errors occur.
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self,
        plant_name: str,
        water_level: int,
        sun_level: int
    ) -> None:
        """
        Checks plant health. Complains if water is too high or sun too low.
        """
        if water_level > 10:
            raise PlantError(
                f"Water level {water_level} is too high (max 10)"
            )
        if sun_level < 2:
            raise PlantError(f"Sun level {sun_level} is too low (min 2)")

        print(
            f"{plant_name}: healthy "
            f"(water: {water_level}, sun: {sun_level})"
        )

    def verify_tank_status(self, liters: int) -> None:
        """
        Checks the water tank. Complains if the tank is empty.
        """
        if liters <= 0:
            raise WaterError("Not enough water in tank")


def main():
    """
    Runs the garden system to test adding, watering, and error handling.
    """
    manager = GardenManager()
    print("=== Garden Management System ===")
    print("Adding plants to garden...")
    plants_to_add = ["tomato", "lettuce", ""]

    for p in plants_to_add:
        try:
            manager.add_plant(p)
        except PlantError as e:
            print(f"Error adding plant: {e}")

    print("Watering plants...")
    manager.water_plants()

    print("Checking plant health...")
    test_cases = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8)
    ]

    for name, water, sun in test_cases:
        try:
            manager.check_plant_health(name, water, sun)
        except PlantError as e:
            print(f"Error checking {name}: {e}")

    print("Testing error recovery...")
    try:
        manager.verify_tank_status(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    main()
