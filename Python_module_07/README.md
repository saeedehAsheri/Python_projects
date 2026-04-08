# DataDeck: Abstract Card Game System

DataDeck is a modular, object-oriented framework for building card games. This project demonstrates how to use advanced Python concepts like Abstract Base Classes (ABC), Multiple Inheritance, and Design Patterns to create a flexible and scalable game engine.

##  Project Architecture

The project is built in layers, moving from basic definitions to a full tournament system:

### 1. Foundation Layer (`ex0`)
The DNA of the game. It defines the base `Card` and the first concrete card type, `CreatureCard`. Everything starts here.

### 2. Implementation Layer (`ex1`)
Building the variety. We added `SpellCard`, `ArtifactCard`, and a `Deck` management system to handle shuffling and drawing cards.

### 3. Ability Layer (`ex2`)
Mixing skills. Using **Multiple Inheritance**, we created cards like the `EliteCard` that can both fight (Combatable) and cast spells (Magical).

### 4. Engine Layer (`ex3`)
The "Brain." We used the **Strategy Pattern** for AI behavior and the **Abstract Factory Pattern** to create themed sets of cards (like Fantasy or Sci-Fi) without changing the core code.

### 5. Platform Layer (`ex4`)
The Stadium. A unified `TournamentPlatform` that handles card registration, matches, and a live Leaderboard with an Elo-style rating system.

---

## Engineering Concepts

This project was built using several professional software engineering principles:

* **S.O.L.I.D Principles:** Specifically *Interface Segregation* (keeping combat and magic logic separate) and *Single Responsibility*.
* **Design Patterns:** Utilizing *Factory* and *Strategy* patterns to make the game engine highly flexible.
* **Defensive Programming:** Using Type Hinting and smart attribute lookups (`getattr`) to prevent crashes.
* **Polymorphism:** Allowing the game engine to treat any object (Dragon, Spell, or Ring) as a simple "Card" while executing unique behaviors.

---

## How to Run

To run any part of the project, use the Python module flag from the root directory:

```bash
# Example: Running the Game Engine
python3 -m ex3.main

# Example: Running the Tournament Platform
python3 -m ex4.main