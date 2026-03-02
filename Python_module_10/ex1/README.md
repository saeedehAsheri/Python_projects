# The Higher Realm

## Overview
The **Higher Realm** is the second stage of the 7FuncMage project. This exercise focuses on **Higher-Order Functions (HOF)**, treating functions as "First-Class Citizens." This means functions can be passed as arguments, nested within other functions, and returned as values to create dynamic spell-crafting systems.

## Technical Requirements
* **Language:** Python 3.10+
* **Coding Standard:** Flake8 (PEP 8)
* **Authorized Tools:** `callable()`, `typing.Callable`, `typing.Any`.
* **Constraint:** All functions include exception handling to ensure program stability.

---

## Functional Concepts

### 1. First-Class Citizens
In Python, functions are objects. You can assign them to variables, store them in lists, or pass them to other functions just like numbers or strings.

### 2. Higher-Order Functions (HOF)
A function that either takes another function as an input or returns a function as an output is called a Higher-Order Function.



### 3. Closures
When we define a function inside another function, the inner function "remembers" the variables of the outer function even after the outer function has finished executing. This is used to create "custom" versions of spells.



---

## Technical Guide: Syntax and Logic

### 1. Spell Combiner
**Logic:** Merges two spells into one.
* **Syntax:** Returns a new function that runs `spell1` and `spell2` with the same arguments and returns their results in a `tuple`.

### 2. Power Amplifier
**Logic:** Scales the power of a spell.
* **Syntax:** Runs a `base_spell`, takes its numerical return value, and multiplies it by a `multiplier`.

### 3. Conditional Caster
**Logic:** Adds a requirement for casting.
* **Syntax:** Runs a `condition` function first. If it returns `True`, the `spell` is executed; otherwise, it returns `"Spell fizzled"`.

### 4. Spell Sequence
**Logic:** Executes a chain of spells.
* **Syntax:** Iterates through a `list` of functions and returns their results in a single `list`.

---

## Implementation Summary

| Function | Purpose | Logic |
| :--- | :--- | :--- |
| `spell_combiner` | Combine behaviors | `return (s1(*args), s2(*args))` |
| `power_amplifier` | Scale numerical output | `return s1(*args) * multiplier` |
| `conditional_caster` | Gated execution | `if condition: return s1(*args)` |
| `spell_sequence` | Order execution | `[s(*args) for s in spells]` |

## Usage
1.  **Run Tests:**
    ```bash
    python3 higher_magic.py
    ```
2.  **Verify Standards:**
    ```bash
    flake8 higher_magic.py
    ```

---

### Why use Higher-Order Functions?
HOFs promote the **DRY (Don't Repeat Yourself)** principle. Instead of writing separate logic for every condition, you create a "wrapper" (like `conditional_caster`) that can add a condition to **any** spell in your system. This makes the code modular, reusable, and much cleaner.