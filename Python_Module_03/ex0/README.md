# 🗣️ Command Quest: Talking to the Program

## 📝 The Concept
Usually, programs just run and do what they were told inside the code. But what if you want to give them instructions *before* they start?

**Command Line Arguments** are like whispering a secret code to the program right as you launch it.

* **Normal Run:** `python3 ft_command_quest.py` (The program runs alone).
* **With Arguments:** `python3 ft_command_quest.py sword shield potion` (The program runs carrying these items).

## 🔑 Key Concepts
* **`sys.argv`**: This is a list that catches every word you typed in the terminal.
* **`sys.argv[0]`**: The first word is always the **name of the program itself**.
* **Index 1 to End**: Everything else is what you typed.

## 💡 Real World Example
Imagine a robot waiter.
* If you just turn it on, it stands there.
* If you say "Water Burger", it catches those words in its `argv` list and knows what to serve.