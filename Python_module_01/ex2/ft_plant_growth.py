"""
Watching Plants Grow.

This script teaches how to add behavior (methods) to our plants.
Plants aren't just static data; they can change (grow and age) over time.
"""


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_one_day(self):
        self.age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)

    print("=== Day 1 ===")
    print(rose.get_info())
    print(sunflower.get_info())

    rose_start_height = rose.height
    sunflower_start_height = sunflower.height

    rose.grow()
    rose.age_one_day()
    sunflower.grow()
    sunflower.age_one_day()

    rose.grow()
    rose.age_one_day()
    sunflower.grow()
    sunflower.age_one_day()

    rose.grow()
    rose.age_one_day()
    sunflower.grow()
    sunflower.age_one_day()

    rose.grow()
    rose.age_one_day()
    sunflower.grow()
    sunflower.age_one_day()

    rose.grow()
    rose.age_one_day()
    sunflower.grow()
    sunflower.age_one_day()

    rose.grow()
    rose.age_one_day()
    sunflower.grow()
    sunflower.age_one_day()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(sunflower.get_info())

    print("Growth this week:")
    print(rose.name, "+", rose.height - rose_start_height, "cm")
    print(sunflower.name, "+", sunflower.height - sunflower_start_height, "cm")
