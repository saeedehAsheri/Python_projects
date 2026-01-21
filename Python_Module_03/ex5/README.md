# 🌊 Data Stream: The Endless River

## 📝 The Concept
Imagine you want to count every drop of water in a river.
* **The "List" way:** You wait for the river to stop, put ALL the water in a giant bucket, and then count it. (Impossible! The bucket would be too big).
* **The "Generator" way:** You stand by the river and count each drop as it flows past you. You never hold all the water at once.

In Python, a **Generator** is a function that gives you one item at a time instead of building a whole list. This saves memory.

## 🔑 Key Concepts
* **`yield`**: This is the magic word. It pauses the function and hands over **one** value. When you ask for the next one, the function wakes up and continues.
* **Infinite Sequences**: Since we generate data on the fly, we can create infinite lists (like Prime numbers) without crashing the computer.


## 💡 Real World Example
* **Streaming Movie:** You don't download the whole 2-hour movie before watching. You download 10 seconds, watch it, then download the next 10 seconds.
* **Game Events:** We processed 1,000 game events, but at any single moment, the computer only "knew" about **one**. This means we could process 1 billion events just as easily!