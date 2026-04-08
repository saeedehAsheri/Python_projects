# 🌌 Cosmic Data Observatory: Pydantic Mastery Course

##  Overview
This repository contains a series of exercises designed to master **Pydantic v2**, Python's most powerful data validation library. Through a space-themed curriculum, we transition from basic data models to complex, nested interstellar mission architectures.

---

##  Core Module Summary

###  Exercise 0: Basic Data Modeling
**Focus:** Foundations of `BaseModel` and `Field`.
- **Key Concepts:** Type hinting, required vs. optional fields, and basic constraints.
- **Data Coercion:** Automatic conversion of strings to `datetime` objects and integers.
- **Validation:** Using `Field(ge=..., le=...)` for numerical boundaries and `min_length/max_length` for strings.

###  Exercise 1: Advanced Logic Validation
**Focus:** Business rules and `model_validator`.
- **Enums:** Restricting inputs to specific categories (e.g., `ContactType`).
- **Inter-field Logic:** Using `@model_validator(mode='after')` to check relationships between fields.
- **Logic Rules:** Implementing conditional requirements (e.g., "Physical contact must be verified").

###  Exercise 2: Nested Systems & Collections
**Focus:** Hierarchical data and list processing.
- **Nested Models:** Embedding models within models (`List[CrewMember]`).
- **Recursive Validation:** Automatic validation of child objects by the parent model.
- **Complex Aggregation:** Using `any()` and `all()` to enforce safety protocols across entire mission crews (e.g., "50% experience rule").

---

## Global Standards
All modules in this project adhere to strict engineering standards:
1. **Python 3.10+**: Utilizing modern typing features.
2. **Flake8 (PEP 8)**: Clean code with a 79-character line limit.
3. **Robust Error Handling:** Capturing `ValidationError` to provide human-readable feedback.
4. **Self-Documenting Code**: Comprehensive docstrings and explicit type hints.

---

## Installation & Usage

```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install pydantic flake8

# Linting check
flake8 .

# Run Exercises
python ex0/space_station.py
python ex1/alien_contact.py
python ex2/space_crew.py