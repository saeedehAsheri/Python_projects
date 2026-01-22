# Exercise 4: Inventory Master

## 📝 Overview
This project simulates a video game inventory system. It uses **Dictionaries** to store items (like swords and potions) and their quantities. The program analyzes this data to calculate totals, percentages, and statistics, and organizes items into categories.

## 🧠 Concepts Learned

### 1. Dictionaries (`dict`)
A dictionary is a storage container that uses **Key-Value pairs**.
- **Key:** The unique name of the item (e.g., "sword").
- **Value:** The data associated with that name (e.g., `1` unit).
- **Why use it?** Unlike a list, a dictionary lets you find data instantly by its name. You don't have to search through the whole pile; you just ask for "sword".

```python
# Example
inventory = {"potion": 5, "sword": 1}
print(inventory["potion"]) # Output: 5