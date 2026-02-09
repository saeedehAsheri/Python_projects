# 🕶️ Project: Matrix Data Engineering

In `ex01`, we move from environment isolation to **Dependency Management**. As Neo needed "Guns, lots of guns," a Data Engineer needs libraries—but they must be loaded with absolute precision.

---

## Core Concepts

### 1. What is Rigor?
In this project, **Rigor** refers to the scientific discipline and strict adherence to standards. It means:
- **Reproducibility:** Ensuring the code works the same way on every machine.
- **Error Handling:** Anticipating that things will go wrong (like missing packages) and handling them gracefully without crashing.
- **Standardization:** Following PEP 8 (Flake8) and using Type Hints to make the code self-documenting and robust.

### 2. Package Management: The Two Paths

#### A. The Classic Way: `requirements.txt`
The `requirements.txt` file is a simple list of the libraries your project needs. 
- **Usage:** You use it with `pip install -r requirements.txt`.
- **Pros:** Universal and simple.
- **Cons:** It doesn't always handle "dependency of a dependency" conflicts well. It’s like a shopping list that doesn't check if the items actually fit together.

#### B. The Modern Way: Poetry
**Poetry** is a sophisticated tool that handles the entire lifecycle of a Python project.
- **Usage:** Defined in `pyproject.toml` and executed via `poetry install`.
- **The `poetry.lock` file:** This is the "Source of Truth." It records the exact hash and version of every single sub-dependency, guaranteeing 100% consistency across all environments.
- **Environment Management:** Poetry automatically creates and manages a virtual environment for you, so you don't have to do it manually.



---

##  Technical Standards

This project adheres to the following strict requirements:
- **Python 3.10+**: Utilizing modern features and performance.
- **Flake8 Compliance**: Zero linting errors.
- **Type Hinting**: All functions include explicit type definitions.
- **Defensive Programming**: Using `importlib.metadata` to check for packages before attempting to use them.

---

##  Mission: Exercise 01

The goal is to build `loading.py`, a tool that analyzes simulated Matrix data and generates a visualization of Sentinel density.
