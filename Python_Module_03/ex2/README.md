# Exercise 2: Position Tracker (3D Coordinate System)

## 📝 Description
This project is a simple tool for a game or simulation. It helps track a player's position in a 3D world (x, y, z). The program reads coordinates from the user, converts them into numbers, and calculates how far the player is from the center of the world (0, 0, 0).

## 🧠 Concepts Learned

### 1. Tuples `( )`
A **Tuple** is a collection of items, similar to a list.
* **Syntax:** `my_tuple = (10, 20, 5)`
* **Key Feature (Immutability):** Unlike lists, tuples **cannot be changed** after they are created. You cannot add or remove items.
* **Why use them?** In games, coordinates should be solid. We use tuples to ensure the position data stays safe and doesn't get modified by accident.

### 2. Tuple Unpacking
Unpacking is a shortcut to extract values from a tuple into separate variables.
Instead of doing this:
```python
x = pos[0]
y = pos[1]
z = pos[2]