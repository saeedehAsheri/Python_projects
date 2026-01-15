# 🌻 Python OOP: The Garden Project

Welcome to the documentation for the Garden Project. This project uses the concept of building and managing a digital garden to explain **Object-Oriented Programming (OOP)** in Python.

Instead of talking about "data structures" and "algorithms," we talk about **Plants**, **Flowers**, and **Gardeners**. This guide explains every concept used in the code files.

---

## 1. The Basics: Classes and Objects

### What is a Class?
Think of a **Class** as a **Blueprint** or a **Cookie Cutter**.
It is not the object itself; it is the instructions on *how* to make the object.

* **Code Example:** `class Plant:`
* **Real World:** The biological definition of what a "Rose" is.

### What is an Object (Instance)?
If the Class is the blueprint, the **Object** is the actual **House** built from it.
You can use one blueprint (Class) to build thousands of houses (Objects).

* **Code Example:** `my_rose = Plant("Rose", 25)`
* **Real World:** The specific physical rose bush sitting in your garden right now.

### The Constructor (`__init__`)
This is the setup function. It runs automatically the moment a new object is born. It assigns the "starter data" (like giving a baby a name).

---

## 2. Variables: "Mine" vs. "Ours"

In Python classes, there are two types of storage. It is important to know the difference.

### Instance Variables (`self.variable`)
These are **Personal**. Every object has its own copy.
* **Example:** `self.height`.
* **Why?** Because my rose might be 25cm tall, but your sunflower is 80cm tall. They don't share this number.
* **Key word:** `self` (refers to "Me", this specific object).

### Class Variables
These are **Shared**. There is only one copy for the entire Class, and everyone looks at the same one.
* **Example:** `Plant.total_plants`.
* **Why?** If we want to count *how many* plants exist in the world, we need one shared counter. If I add a plant, your counter should go up too.

---

## 3. Methods: Making Things Happen

Methods are just functions that live inside a class. They define what an object **can do**.

* **Instance Method:** Requires `self`. It changes the specific object.
    * *Example:* `grow()`. When `rose.grow()` is called, only the rose gets taller. The sunflower stays the same size.

---

## 4. Inheritance: The Family Tree

**Inheritance** allows us to create specialized versions of a class without rewriting code.

* **Parent Class:** `Plant` (Has height and age).
* **Child Class:** `Flower` (Has height and age **PLUS** color).

### Why do we use it?
It stops us from repeating ourselves. Since a `Flower` is a type of `Plant`, we don't need to write the code for `height` again. We just say `class Flower(Plant):` and it automatically gets everything the Parent has.

* **`super()`**: This is how the Child calls the Parent. It says, "Hey Mom, do your setup first (name, height), and then I will do my extra setup (color)."

---

## 5. Advanced Management Tools

Sometimes we need tools that don't fit perfectly into "Instance" or "Class" logic.

### Static Methods (`@staticmethod`)
These are **Utility Tools**. They don't care about specific plants or the class itself. They are just helper functions that live inside the class for organization.

* **Example:** `is_valid_height(height)`.
* **Usage:** To check if `-5` is a valid number. It doesn't need to know *which* plant we are talking about; it just checks the math.

### Class Methods (`@classmethod`)
These are **Factory Tools**. They work on the Class itself, not on a specific object.

* **Example:** `create_demo_garden()`.
* **Usage:** Instead of you manually creating a manager and adding plants one by one, you call this method. It talks to the `GardenManager` class and says, "Build a pre-made garden for me."

---

## 6. Encapsulation: Security

This is the practice of hiding internal data to protect it.

* **The Problem:** Someone might accidentally set a plant's height to `-100`.
* **The Solution:** We make the variable "private" (by putting an underscore `_` before the name, like `_height`) and force people to use a **Setter Method** (`set_height`).
* **Usage:** The setter method acts like a security guard. It checks "Is this number positive?" before allowing the change.

---

## Summary Table

| Concept | Simple Definition | Garden Analogy |
| :--- | :--- | :--- |
| **Class** | The Template | The blueprint for a generic plant. |
| **Object** | The Instance | A specific red rose in the dirt. |
| **Instance Var** | Personal Data | The height of *that specific* rose. |
| **Class Var** | Shared Data | The total count of all plants in the world. |
| **Inheritance** | Family Traits | A "Tree" gets all features of "Plant" for free. |
| **Static Method** | Calculator/Tool | A ruler. It measures anything, doesn't care who owns it. |
| **Class Method** | Factory | A machine that builds a standard "Starter Garden" instantly. |