# The Power of Sets

## The Concept
In this exercise, we manage video game achievements. The problem is that players might unlock the same achievement, but we only want to count it **once** in the global list.

We use **Sets** because they are like magic bags that automatically throw away duplicates.

## 🔑 Key Concepts
* **Set (`{...}`)**: A collection of unique items. If you add "Winner" twice, the set only keeps one.
* **Union (`|`)**: "Combine everything." (Give me all achievements from everyone).
* **Intersection (`&`)**: "What do they share?" (What did EVERYONE unlock?).
* **Difference (`-`)**: "What is unique?" (What does Alice have that Bob does NOT have?).

## 💡 Real World Example
* **Union**: Building a list of *all* available trophies in the game.
* **Intersection**: finding which trophies are easy (because everyone has them).
* **Difference**: Finding "Rare" trophies that only one specific player has unlocked.