"""
The Plant Factory.

This script shows the difference between Instance Variables (unique to each
plant) and Class Variables (shared by all plants), allowing us to count
the total population.
"""


class Plant:
    total = 0

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.total += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunf = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print("=== Plant Factory Output ===")
    print("Created:", rose.name, f"({rose.height}cm,", rose.age, "days)")
    print("Created:", oak.name, f"({oak.height}cm,", oak.age, "days)")
    print("Created:", cactus.name, f"({cactus.height}cm,", cactus.age, "days)")
    print("Created:", sunf.name, f"({sunf.height}cm,", sunf.age, "days)")
    print("Created:", fern.name, f"({fern.height}cm,", fern.age, "days)")
    print("Total plants created:", Plant.total)
