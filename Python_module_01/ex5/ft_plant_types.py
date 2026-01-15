"""
Garden Variety.

This script demonstrates 'Inheritance'. We create a generic Plant, then create
specialized versions (Flower, Tree, Vegetable) that inherit basic traits
but add their own unique features.
"""


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def base_info(self):
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        return f"{self.name} (Flower): {self.base_info()}, {self.color} color"

    def bloom(self):
        print(self.name, "is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self):
        return (
            f"{self.name} (Tree): {self.base_info()}, "
            f"{self.trunk_diameter}cm diameter"
        )

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.56
        print(self.name, "provides", int(shade_area), "sq meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return (
            f"{self.name} (Vegetable): {self.base_info()}, "
            f"{self.harvest_season} harvest"
        )

    def show_nutrition(self):
        print(self.name, "is rich in", self.nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower1 = Flower("Rose", 25, 30, "red")
    flower2 = Flower("Tulip", 20, 18, "yellow")

    tree1 = Tree("Oak", 500, 1825, 50)
    tree2 = Tree("Pine", 450, 1500, 40)

    veg1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    veg2 = Vegetable("Carrot", 30, 60, "spring", "beta-carotene")

    print(flower1.get_info())
    flower1.bloom()
    print(flower2.get_info())
    flower2.bloom()

    print(tree1.get_info())
    tree1.produce_shade()
    print(tree2.get_info())
    tree2.produce_shade()

    print(veg1.get_info())
    veg1.show_nutrition()
    print(veg2.get_info())
    veg2.show_nutrition()
