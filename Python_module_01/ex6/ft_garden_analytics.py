"""
Garden Analytics System.

This module provides a system to manage gardens, track plant growth,
and calculate statistics using a nested helper class.
"""


class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(self.name + " grew 1cm")

    def info(self):
        return self.name + ": " + str(self.height) + "cm"

    def get_type(self):
        return "Plant"

    def get_points(self):
        return 0


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def info(self):
        base = super().info()
        return base + ", " + self.color + " flowers (blooming)"

    def get_type(self):
        return "FloweringPlant"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def info(self):
        return super().info() + ", Prize points: " + str(self.points)

    def get_type(self):
        return "PrizeFlower"

    def get_points(self):
        return self.points


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def calculate_growth_summary(self, plants):
            count = 0
            for _ in plants:
                count += 1
            return count

        def count_plant_types(self, plants):
            regular = 0
            flowering = 0
            prize = 0

            for p in plants:
                p_type = p.get_type()
                if p_type == "PrizeFlower":
                    prize += 1
                elif p_type == "FloweringPlant":
                    flowering += 1
                else:
                    regular += 1

            return (
                "1 regular, " + str(flowering) +
                " flowering, " + str(prize) + " prize flowers"
            )

        def calculate_score(self, plants):
            score = 0
            for p in plants:
                score += p.height
                score += p.get_points()
            return score

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print("Added " + plant.name + " to " + self.owner + "'s garden")

    def grow_all(self):
        print(self.owner + " is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print("=== " + self.owner + "'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- " + plant.info())

        growth = self.stats.calculate_growth_summary(self.plants)
        types_str = self.stats.count_plant_types(self.plants)

        count = 0
        for _ in self.plants:
            count += 1

        print(
            "Plants added: " + str(count) +
            ", Total growth: " + str(growth) + "cm"
        )
        print("Plant types: " + types_str)

    @staticmethod
    def is_valid_height(height):
        return height >= 0

    @classmethod
    def create_garden_network(cls):
        alice = cls("Alice")
        bob = cls("Bob")

        bob.add_plant(Plant("Bush", 40))
        bob.add_plant(FloweringPlant("Daisy", 30, "white"))

        return [alice, bob]


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice_garden = GardenManager("Alice")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.grow_all()
    alice_garden.report()

    print("Height validation test: " +
          str(GardenManager.is_valid_height(10)))

    alice_score = alice_garden.stats.calculate_score(alice_garden.plants)
    network = GardenManager.create_garden_network()
    bob_garden = network[1]
    bob_score = bob_garden.stats.calculate_score(bob_garden.plants)

    print(
        "Garden scores - Alice: " + str(alice_score) +
        ", Bob: " + str(bob_score)
    )
    print("Total gardens managed: " + str(GardenManager.total_gardens))
