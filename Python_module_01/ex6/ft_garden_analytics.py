"""
Garden Analytics.

This script combines all concepts (Classes, Inheritance) and adds
Advanced Management tools like Static Methods and Class Methods to manage
the entire ecosystem.
"""


# ---------- Plant family ----------

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(self.name, "grew 1cm")

    def info(self):
        return self.name + ": " + str(self.height) + "cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def info(self):
        return (
            self.name + ": " +
            str(self.height) + "cm, " +
            self.color + " flowers"
        )


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def info(self):
        return (
            self.name + ": " +
            str(self.height) + "cm, " +
            self.color + " flowers, " +
            "points: " + str(self.points)
        )


# ---------- Garden Manager ----------

class GardenManager:
    total_gardens = 0

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print("Added", plant.name, "to", self.owner + "'s garden")

    def grow_all(self):
        print(self.owner, "is helping plants grow")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print("=== Garden Report for", self.owner, "===")
        for plant in self.plants:
            print("-", plant.info())
        print("Total plants:", len(self.plants))

    @staticmethod
    def is_valid_height(height):
        return height >= 0

    @classmethod
    def create_demo_garden(cls):
        return cls("Demo Owner")


# ---------- Program execution ----------

if __name__ == "__main__":
    print("=== Simple Garden Analytics Demo ===")

    garden = GardenManager.create_demo_garden()

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    garden.add_plant(oak)
    garden.add_plant(rose)
    garden.add_plant(sunflower)

    garden.grow_all()
    garden.report()

    print("Height validation test:", GardenManager.is_valid_height(-5))
    print("Total gardens created:", GardenManager.total_gardens)
