# 🏭 Plant Factory: Shared Knowledge

## 📝 The Concept
Sometimes we need information that belongs to the **whole garden**, not just one flower.
* `self.height`: Belongs to **one** plant.
* `Plant.total`: Belongs to **all** plants.

## 🔑 Key Concepts
* **Instance Variable**: `self.name`. Every plant has its own unique name.
* **Class Variable**: `Plant.total`. There is only **one** counter shared by the entire factory.
* **Counting**: Every time `__init__` (creation) runs, we add +1 to the global counter.

## 💡 Real World Example
We create 5 different plants. At the end, we ask the `Plant` class, "How many did we make?" and it correctly answers "5".