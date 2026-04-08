"""
Garden Security System.

This script demonstrates 'Encapsulation'. We protect our plants so nobody
can set their height or age to impossible values (like negative numbers).
"""


class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0

        print("Plant created:", self.name)
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height < 0:
            print(
                "Invalid operation attempted: height",
                f"{height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
            return
        self._height = height
        print("Height updated:", f"{self._height}cm [OK]")

    def get_height(self):
        return self._height

    def set_age(self, age):
        if age < 0:
            print(
                "Invalid operation attempted: age",
                f"{age} days [REJECTED]"
            )
            print("Security: Negative age rejected")
            return
        self._age = age
        print("Age updated:", f"{self._age} days [OK]")

    def get_age(self):
        return self._age

    def get_info(self):
        return f"{self.name} ({self._height}cm, {self._age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)

    plant.set_height(-5)

    print("Current plant:", plant.get_info())
