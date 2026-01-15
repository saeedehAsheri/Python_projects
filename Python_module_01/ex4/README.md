# 🔒 Garden Security: Encapsulation

## 📝 The Concept
You shouldn't be able to accidentally make a plant `-5` cm tall. That defies physics!
**Encapsulation** is the practice of hiding data and only allowing access through "Security Guards" (Methods).

## 🔑 Key Concepts
* **Private Variables (`_height`)**: The underscore `_` hints to other programmers: "Don't touch this directly!"
* **Setters (`set_height`)**: A method that checks the rules (Is the height positive?) before changing the variable.
* **Getters (`get_height`)**: A method to read the variable safely.

## 💡 Real World Example
We try to set the height to `-5`. The `set_height` security guard sees this is invalid, rejects the change, and prints a warning. The plant remains safe.