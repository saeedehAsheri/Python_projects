#  Space Station Data

## Overview
This exercise focuses on mastering the fundamentals of **Pydantic v2** for data validation. As a junior Data Engineer, you are responsible for ensuring that all data received from interstellar space stations is accurate, consistent, and strictly typed.

##  Technical Requirements
To maintain high-quality software standards, the following constraints are applied:
* **Python 3.10+**: Leveraging modern type hinting features.
* **Pydantic 2.x**: Utilizing the latest validation engine (Rust-powered).
* **Flake8 Standards**: All code must adhere to PEP 8 styling guidelines.
* **Type Safety**: Mandatory type hints for all functions and methods.

---

##  Key Concepts

### 1. Pydantic BaseModel
The `BaseModel` is the core building block. It allows you to define the "schema" of your data using Python classes. Unlike standard classes, `BaseModel` automatically parses and validates incoming data during instantiation.

### 2. Field Constraints
Using `pydantic.Field`, we move beyond simple type checking to functional validation:
* **Numerical Constraints**: `ge` (greater than or equal), `le` (less than or equal).
* **String Constraints**: `min_length`, `max_length`.
* **Metadata**: Adding descriptions and default values to fields.

### 3. Data Coercion (Automatic Conversion)
One of Pydantic's most powerful features is **Coercion**. It attempts to convert input data to the required type if safe.
- **Example**: Passing `"2026-02-10"` to a `datetime` field or `"15.5"` to a `float` field will succeed as Pydantic handles the parsing internally.

### 4. Exception Handling
When data violates the defined rules, Pydantic raises a `ValidationError`. This object contains detailed information about:
- Which field failed (`loc`).
- Why it failed (`msg`).
- The type of error (`type`).

---

##  SpaceStation Model Specification

The model validates the following interstellar telemetry:

| Field | Type | Validation Rules |
| :--- | :--- | :--- |
| `station_id` | `str` | 3 to 10 characters |
| `name` | `str` | 1 to 50 characters |
| `crew_size` | `int` | Range: 1 - 20 |
| `power_level` | `float` | 0.0% - 100.0% |
| `oxygen_level` | `float` | 0.0% - 100.0% |
| `last_maintenance`| `datetime`| Must be a valid ISO format string or object |
| `is_operational` | `bool` | Default: `True` |
| `notes` | `Optional[str]`| Max 200 characters |

---
