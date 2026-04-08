# 🎯 Different Errors: The Right Tool for the Job

## 📝 The Concept
Not all problems are the same. In a garden, a missing shovel is different from a broken pipe. This file teaches you how to handle **specific** problems differently.

## 🔑 Keywords Used
* **`ValueError`**: Triggered when the *type* is right, but the *content* is wrong (like turning `"abc"` into a number).
* **`ZeroDivisionError`**: Triggered when you try to divide by zero (mathematically impossible).
* **`FileNotFoundError`**: Triggered when you try to open a file that isn't there.
* **`KeyError`**: Triggered when you look for a plant in your dictionary (e.g., `"rose"`), but it doesn't exist.

## 💡 Real World Example
* If the error is **Math**, we fix the calculation.
* If the error is **Missing File**, we create the file.
* We use multiple `except` blocks to handle each specific scenario separately, rather than a generic "Something went wrong."