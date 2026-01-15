#  Finally Block: The Cleanup Crew

## 📝 The Concept
Sometimes, you start a task that **must** be finished, even if an error happens in the middle. The `finally` block is your guarantee that cleanup happens.

Imagine a water hose:
1.  **Try**: Turn on the water.
2.  **Error**: You slip and fall while watering.
3.  **Finally**: You **MUST** turn off the water tap. If you don't (because you were busy dealing with your fall), the garden will flood.

## 🔑 Keywords Used
* **`finally`**: A block of code that runs **no matter what**.
    * If the code succeeds? `finally` runs.
    * If the code crashes? `finally` runs.

## 💡 Real World Example
In this script, we open a "watering system". Even if we try to water a `None` plant (which causes an error), the `finally` block ensures we see the message `"Closing watering system"`.