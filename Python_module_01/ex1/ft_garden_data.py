"""
This script demonstrates how to create a basic Class.
Instead of writing variables
for every single plant, we create a 'Plant' template and use it to make
multiple plants easily.
"""


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height} cm, {rose.age} days old")
    print(
        f"{sunflower.name}: {sunflower.height} cm, {sunflower.age} days old"
    )
    print(f"{cactus.name}: {cactus.height} cm, {cactus.age} days old")
