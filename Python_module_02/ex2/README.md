# 🏷️ Custom Errors: Making Your Own Labels

## 📝 The Concept
Using generic Python errors like `ValueError` for everything can be confusing. Is it a "Value Error" because the math is wrong, or because the plant is dead?

This file shows how to create **Custom Exceptions**. Instead of a generic "Error", we can report a "PlantError" or a "WaterError".



## 🔑 Keywords Used
* **`class GardenError(Exception)`**: We create a new category of error just for our project.
* **Inheritance**: `PlantError` is a child of `GardenError`. If we catch `GardenError`, we automatically catch `PlantError` too.

## 💡 Real World Example
* **`PlantError`**: Used when a plant is wilting.
* **`WaterError`**: Used when the tank is empty.
* This makes reading logs much easier. We know exactly *where* the problem came from just by looking at the error name.