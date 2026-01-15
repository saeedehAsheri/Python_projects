# 📈 Plant Growth: Changing State

## 📝 The Concept
Objects in Python are "alive". They have **Attributes** (data like `height`) and **Methods** (actions like `grow`).

When we call `rose.grow()`, we are changing the data *inside* that specific rose object. The sunflower remains unchanged until we call `sunflower.grow()`.

## 🔑 Key Concepts
* **Methods**: Functions inside a class (actions the object can do).
* **State Change**: Modifying `self.height` permanently changes that number for the object.
* **`self`**: Refers to "This specific plant". When `rose` runs `grow()`, `self` is the rose.

## 💡 Real World Example
We simulate a week passing. Every day, we tell the plants to `grow()` and `age_one_day()`. At the end of the week, their numbers have changed.