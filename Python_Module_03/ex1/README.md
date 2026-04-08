# 📊 Score Analytics: Number Crunching

## 📝 The Concept
Data usually comes as "text" (strings), even if it looks like numbers. Before we can do math (like finding an average), we must convert this text into real numbers.

This program takes a list of scores, cleans them up, and builds a statistical report.

## 🔑 Key Concepts
* **Type Conversion (`int()`)**: Turning the text `"50"` into the number `50`.
* **Statistics**:
    * **`sum()`**: Total points.
    * **`max()` / `min()`**: Best and worst scores.
    * **`len()`**: How many players played.
* **Error Handling**: If a user types "ten" instead of "10", the program catches the `ValueError` and politely complains.

## 💡 Real World Example
The teacher feeds test scores into the computer: `90 85 100`. The computer instantly calculates the class average and finds the highest grade.