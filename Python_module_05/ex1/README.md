#Polymorphic Data Streams

## About The Project
Imagine you have a conveyor belt carrying boxes. Some boxes have **numbers** (temperature), some have **money** (transactions), and some have **messages** (system logs).

If you try to calculate the "average" of a text message, your machine will explode! 

This project is a smart data processing system. It takes a mix of messy data, automatically filters out the bad stuff, and sends the good data to the correct processor. It uses a concept called **Polymorphism** to handle everything through one simple button.

---

##  Key Concepts (Explained Simply)

### 1. The Blueprint (Abstract Base Class)
Think of the class `DataStream` as a **Contract** or a **Rulebook**.
It doesn't do any work itself. Instead, it tells any future stream:
> *"If you want to be part of this system, you **MUST** have a function called `process_batch`."*

### 2. The Specialized Workers (Inheritance)
We created three specific workers based on that Blueprint. They inherit the basic features (like having an ID), but they do their own specific jobs:
* **SensorStream:** Loves numbers. It calculates the **average** temperature.
* **TransactionStream:** Loves money. It calculates the **total** profit or loss.
* **EventStream:** Loves text. It counts how many **errors** occurred.

### 3. The Security Guard (Type Checking)
In the past, we might have tried to add an empty string to a variable to see if it was a number. That is dangerous!
Now, we use `isinstance()`. This is like a **Security Guard** at the door of each worker:
* *Guard at SensorStream:* "Are you a number? No? Get out!"
* *Guard at EventStream:* "Are you text? No? Get out!"

This prevents the program from crashing when bad data arrives.

### 4. The Magic Trick (Polymorphism) 🎭
This is the coolest part. In the `main` function, we put the Sensor, the Transaction, and the Event processor into one list.

We loop through them and call `.process_batch()` on all of them.
* We don't need to check "Is this a sensor?".
* We just say "Process!" and the object knows exactly what to do.
* **One interface, many different behaviors.** This is Polymorphism.

---

## 🛠️ Features
* **Batch Processing:** Processes lists of data at once, not just single items.
* **Stateful Memory:** The streams remember how many items they have processed so far (`items_processed`).
* **Robust Filtering:** Uses **List Comprehensions** (a clean Python tool) to filter out invalid data instantly.
* **Error Handling:** If something goes wrong, the program catches the error instead of crashing.

