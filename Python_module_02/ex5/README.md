# 🌳 Garden Management: The Complete System

## 📝 The Concept
This is the "Final Boss" level. It combines every concept we have learned into a single, robust Class.

It simulates a real software system where:
1.  We have a Manager (Class).
2.  We have custom rules (Raise).
3.  We have safety nets (Try/Except).
4.  We have cleanup protocols (Finally).

## 🔑 key Features
* **Robustness**: The program tries to add plants, water them, and check their health.
* **Resilience**: Even when we try to add an invalid plant or check a nonexistent tank, the program catches the specific Custom Error (`PlantError`, `WaterError`), prints a nice message, and **continues running**.

## 💡 Real World Example
This represents professional code. It doesn't crash when inputs are bad; it logs the issue, cleans up resources, and moves on to the next task.