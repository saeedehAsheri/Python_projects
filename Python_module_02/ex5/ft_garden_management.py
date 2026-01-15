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
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
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
        if liters <= 0:
            raise WaterError("Not enough water in tank")


def main():
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
