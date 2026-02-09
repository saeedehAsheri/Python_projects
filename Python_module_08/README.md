# Matrix Data Engineering: The Core Fundamentals

"Welcome to the real world." This repository contains a series of exercises designed to master the infrastructure of professional Data Engineering: Environment Isolation, Dependency Management, and Secure Configuration.

---

## Project Overview

### [Ex00] The Construct: Virtual Environments
**Concept:** Isolation of the development environment.
- **Key Learning:** Using `venv` to create a simulated reality for Python projects.
- **Why?** To prevent "Dependency Hell" and ensure the host system (OS) remains clean.
- **Standard:** Use of `sys.prefix` and `sys.base_prefix` to detect environment status.

### [Ex01] Loading Programs: Package Management
**Concept:** Managing external libraries with Rigor.
- **Key Learning:** Comparing **pip** (`requirements.txt`) and **Poetry** (`pyproject.toml` & `poetry.lock`).
- **Tools:** `pandas`, `numpy`, `matplotlib`.
- **Why?** To ensure that "Loading" a program works consistently for every resistance fighter in Zion, regardless of their machine.

### [Ex02] Accessing the Mainframe: Security & Config
**Concept:** Separation of Code and Secrets.
- **Key Learning:** Using `.env` files and `python-dotenv` to manage sensitive data.
- **Why?** To keep API keys and database credentials secure. 
- **Rigor:** Implementation of `.gitignore` to prevent leaking secrets to the Matrix (GitHub).

---

## Core Engineering Principles (The Code of Zion)

### 1. What is Rigor?
In this project, **Rigor** is the strict adherence to professional standards:
- **Flake8 Compliance:** Zero linting errors for maximum readability.
- **Type Hinting:** Explicitly defining data types to prevent runtime bugs.
- **Backward Compatibility:** Using `typing.Optional` and `typing.Dict` to ensure code runs across Python 3.9 to 3.13.

### 2. Dependency Management: Pip vs. Poetry
- **Pip:** Quick, manual, and simple for small scripts.
- **Poetry:** Robust, deterministic, and professional. It uses "Lock files" to freeze the entire dependency tree.

### 3. Environment Security
We follow the "Twelve-Factor App" methodology by storing configuration in the environment. This makes our data pipelines **Scalable** and **Secure**.

---
