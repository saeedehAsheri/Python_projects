# Alien Contact Logs

## Overview
As the data stream from deep space intensifies, we encounter sensitive reports of extraterrestrial contact. This exercise focuses on **Advanced Data Validation** using Pydantic v2. You will move beyond simple field-level constraints to implement complex **Business Logic** that governs the relationships between different data points.

## Technical Specifications
* **Python 3.10+**: Utilizing modern type annotations.
* **Pydantic 2.x**: Using Rust-powered validation for high performance.
* **Enums**: Implementing restricted choice sets for categorical data.
* **Flake8 (PEP 8)**: Strict adherence to clean code standards (79-character line limit).

---

##  Core Concepts

### 1. Enumerations (Enum)
We use `str, Enum` to define `ContactType`. This ensures that the `contact_type` field only accepts a specific set of values (`radio`, `visual`, `physical`, `telepathic`). 
- **Benefit**: Prevents typos and ensures data consistency across the observatory's database.

### 2. Model-Level Validation (`@model_validator`)
While `Field()` constraints check individual attributes, `@model_validator(mode='after')` allows for **Inter-field Validation**. This is used to verify that specific combinations of data are logical and valid.



### 3. The `mode='after'` Lifecycle
In Pydantic v2, the `after` mode ensures that:
1. All basic types are already validated (e.g., `witness_count` is confirmed to be an integer).
2. Data coercion is complete (e.g., ISO strings are converted to `datetime` objects).
3. The validator receives a fully formed `self` instance to perform final logic checks.

---

## Interstellar Business Rules
The following complex rules are enforced in this module:

| Rule Target | Logic Requirement |
| :--- | :--- |
| **ID Format** | `contact_id` must start with the prefix **"AC"**. |
| **Physical Contact** | If type is `physical`, `is_verified` must be `True`. |
| **Telepathic Contact**| Requires at least **3 witnesses** to be considered valid. |
| **Signal Integrity** | If `signal_strength > 7.0`, a `message_received` is mandatory. |

---

##  Getting Started

### 1. Setup Environment
Ensure your virtual environment is active and dependencies are installed:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install pydantic flake8