#  First Exception: The Basic Safety Net

## 📝 The Concept
This file introduces the most fundamental concept of error handling: **Stopping a crash**.

Imagine you have a digital thermometer in your garden. You expect it to show a number (like `25`). But what if someone writes `"cloudy"` on it?
* **Without error handling:** The thermometer explodes (The program crashes).
* **With error handling:** The thermometer simply says, "That is not a number."

## 🔑 Keywords Used
* **`try`**: "Attempt to read the number." (This is the dangerous part).
* **`except`**: "If reading fails (because it's text, not a number), jump here and print an error message instead of crashing."



## 💡 Real World Example
You try to convert the user's input into an integer (`int`). If they type `"abc"`, Python triggers a `ValueError`. Our `except` block catches this error and saves the program.