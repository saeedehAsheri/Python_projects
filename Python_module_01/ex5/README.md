# 🌳 Plant Types: Inheritance

## 📝 The Concept
In nature, a Rose is a Flower, and a Flower is a Plant.
In Python, we use **Inheritance** so we don't have to repeat code.
* The `Plant` class handles the basics (height, age).
* The `Flower` class inherits those basics and adds `color`.
* The `Tree` class inherits basics and adds `trunk_diameter`.


## 🔑 Key Concepts
* **Parent Class (Superclass)**: `Plant`. The base model.
* **Child Class (Subclass)**: `Flower`, `Tree`. specialized versions.
* **`super().__init__(...)`**: The child asks the parent to handle the basic setup first.

## 💡 Real World Example
We created Trees that produce shade and Vegetables that have nutrition. They are all "Plants", but they have their own unique superpowers.