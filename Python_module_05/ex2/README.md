# Code Nexus: Enterprise Data Pipeline

## The Story: The "Nexus Kitchen"
Welcome to the final challenge! In this project, we are not just building simple machines anymore. We are building a massive **Factory** (or a Restaurant Kitchen) that handles different types of orders (Data).

To understand this code, imagine you are the **Manager** of a restaurant that serves:
1.  **JSON Pizza** 🍕
2.  **CSV Salad** 🥗
3.  **Stream Soup** 🍜

This system uses advanced architecture to prepare all these different dishes using the same "workers" and "assembly lines."

---

## Key Concepts (Explained Simply)

### 1. The "Job Description" (Protocol / Duck Typing)
In our factory, we don't care about a worker's family name or degree. We only care about one thing: **Can you do the job?**

* **In Code:** `ProcessingStage(Protocol)`
* **The Rule:** Any class that has a `process(data)` method is hired!
* **Why?** This is called **Duck Typing**. If it walks like a duck and quacks like a duck, it's a duck. If a class processes data, it's a Stage.

### 2. The "Workers" (Concrete Stages)
These are the employees who actually touch the food (data). They don't know about the whole factory; they just do their specific task.

* **InputStage:** The "Cleaner". Washes the ingredients (Validates input).
* **TransformStage:** The "Chef". Chops and cooks (Enriches/Parses data).
* **OutputStage:** The "Waiter". Plates the food for the customer (Formats output).

### 3. The "Assembly Line" (Abstract Base Class & Composition)
You can't just throw food on the floor! You need a table or a conveyor belt to move the food from one worker to the next.

* **In Code:** `ProcessingPipeline`
* **Composition (Has-a):** This class **HAS** a list of stages (`self.stages = []`). It acts like a container. It doesn't cook the food itself; it holds the workers who do.

### 4. The "Specialized Lines" (Inheritance)
Even though we have a standard assembly line, the *Pizza Line* is slightly different from the *Salad Line*.

* **In Code:** `JSONAdapter`, `CSVAdapter`, `StreamAdapter`
* **Inheritance (Is-a):** These **ARE** pipelines. They inherit the ability to hold stages from the base class, but they might start the process differently.

### 5. The "Boss" (Manager)
Someone needs to take the orders and yell "Start Line 1!".

* **In Code:** `NexusManager`
* **Role:** Holds all the pipelines in a dictionary and runs them when asked.

---

## Architecture Diagram

```mermaid
graph TD
    Manager[Nexus Manager] -->|Manages| JSON[JSON Adapter]
    Manager -->|Manages| CSV[CSV Adapter]
    Manager -->|Manages| Stream[Stream Adapter]
    
    JSON -- Inherits from --> Pipeline[ProcessingPipeline]
    CSV -- Inherits from --> Pipeline
    Stream -- Inherits from --> Pipeline
    
    Pipeline -- Contains (Composition) --> Stages[List of Stages]
    
    Stages -.-> Input[Input Stage]
    Stages -.-> Transform[Transform Stage]
    Stages -.-> Output[Output Stage]