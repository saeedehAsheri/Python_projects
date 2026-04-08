# The Lambda Sanctum

## Overview
The **Lambda Sanctum** is the introductory stage of the 7FuncMage project. It marks the transition from imperative programming (using loops and manual state management) to **Functional Programming (FP)**. This exercise focuses on processing magical data structures using anonymous functions and high-order functions in Python 3.10+.

## Technical Requirements
* **Language:** Python 3.10+
* **Coding Standard:** Flake8 (PEP 8)
* **Authorized Tools:** `map`, `filter`, `sorted`, `typing`.
* **Prohibited:** External libraries (pip), Global variables, and File I/O.

---

## Functional Programming Concepts

### 1. Lambda Expressions (Anonymous Functions)
A `lambda` is a small function defined without a name. It is used for short, one-time tasks where a full function definition (`def`) would be unnecessarily verbose.

**How to use it:**
The syntax is `lambda arguments: expression`. 
* **Logic:** It takes an input, processes it through a single expression, and returns the result.
* **When to use:** Use it as an argument for other functions like `map` or `filter` when the logic is simple enough to fit on one line.



### 2. Map (Transformation)
The `map()` function applies a specific transformation to every item in an iterable (like a list) and returns a new iterator.

**How to use it:**
`map(function, iterable)`
* **Logic:** It says: "Take this rule and apply it to every element in this collection."
* **Project Application:** In `spell_transformer`, it is used to wrap every spell name string with decorative stars without using a manual loop.

### 3. Filter (Selection)
The `filter()` function creates a new iterator from elements of an iterable for which a specific function returns `True`.

**How to use it:**
`filter(function, iterable)`
* **Logic:** It acts as a gatekeeper. If the function (usually a lambda) returns `True` for an item, that item is kept; otherwise, it is discarded.
* **Project Application:** In `power_filter`, it efficiently extracts only the mages whose power level meets a minimum threshold.



### 4. Sorted (Ordering)
The `sorted()` function returns a new sorted list from the items in an iterable. To sort complex data structures like a list of dictionaries, the `key` parameter is used.

**How to use it:**
`sorted(iterable, key=lambda, reverse=True)`
* **The Key:** The `key` tells Python exactly which attribute to look at (e.g., the 'power' value inside a dictionary).
* **Reverse:** Setting `reverse=True` changes the order from ascending (default) to descending.
* **Project Application:** In `artifact_sorter`, it ranks magical artifacts from the highest power to the lowest.



---

## Implementation Summary

| Function | Purpose | Functional Tool |
| :--- | :--- | :--- |
| `artifact_sorter` | Sorts artifacts by power (High to Low) | `sorted()` + `lambda` |
| `power_filter` | Extracts mages above a power limit | `filter()` + `lambda` |
| `spell_transformer` | Adds stars to spell names | `map()` + `lambda` |
| `mage_stats` | Calculates Max, Min, and Avg power | `max/min/sum` + `map` |

## Usage
1.  Ensure you have Python 3.10 or later installed.
2.  Execute the script to verify the transformations:
    ```bash
    python3 lambda_spells.py
    ```
3.  Check for coding standard compliance:
    ```bash
    flake8 lambda_spells.py
    ```

---

### Why Functional Programming?
By using `map`, `filter`, and `lambda`, we write **declarative** code. Instead of managing the "how" (manual counters and list appends), we describe the "what" (the logic of the transformation). This results in code that is easier to read, test, and maintain, while strictly avoiding the modification of original data (immutability).