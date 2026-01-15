# 🚩 Raise Errors: The Rule Enforcer

## 📝 The Concept
Sometimes Python thinks everything is fine, but **you** know it's not. This file teaches you how to create your own rules and stop the program manually.

Example: Is `-100` a valid number? To Python, yes. But for "Sunlight Hours", `-100` is impossible.

## 🔑 Keywords Used
* **`raise`**: This is you shouting "STOP!" to Python. You are manually triggering an error because a specific rule was broken.

## 💡 Real World Example
We check the `water_level`.
* If it is `15` (which is too high), Python doesn't care.
* So we write logic: `if water > 10: raise ValueError`.
* This forces the program to stop and report that the water level is invalid, protecting the data integrity of our garden.