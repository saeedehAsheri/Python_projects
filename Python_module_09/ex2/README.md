# Space Crew Management

## Overview
As we scale our operations, data structures become increasingly complex. Exercise 2 focuses on **Nested Pydantic Models**, where one model contains a collection of other models. This module simulates a real-world Mission Control system where we must validate not just a single entity, but an entire ecosystem of related data (Missions and their Crews).

## Technical Specifications
* **Python 3.10+**: Utilizing `List` and `Optional` type hints.
* **Nested Models**: Implementing `CrewMember` as a sub-type within `SpaceMission`.
* **Recursive Validation**: Pydantic automatically validates every object in a list against the child model.
* **Flake8 Compliance**: Code is optimized for the 79-character line limit.

---

##  Core Concepts

### 1. Nested Data Structures
In Pydantic, a field can be a list of other Pydantic models:
`crew: List[CrewMember]`
When a `SpaceMission` is initialized, Pydantic performs a "Recursive Check." If any single `CrewMember` in the list fails its own validation (e.g., age is 15), the parent `SpaceMission` will fail to initialize.



### 2. Advanced Inter-model Validation
Using `@model_validator(mode='after')`, we can verify rules that depend on the relationship between the Mission and its Crew. This allows us to calculate percentages, check for specific roles, and verify status across a collection of objects.

### 3. Efficiency with `any()` and `all()`
We utilize Python’s built-in logic functions to keep the validation code clean and performant:
- **`any()`**: Returns `True` if at least one element meets the criteria (e.g., checking for at least one Captain).
- **`all()`**: Returns `True` only if every element meets the criteria (e.g., ensuring all crew members are active).

---

##  Mission Safety Protocols
The `SpaceMission` model enforces the following critical safety checks:

| Protocol | Requirement |
| :--- | :--- |
| **Command Structure** | Every mission must include at least one **Captain** or **Commander**. |
| **Experience Ratio** | Missions > 365 days require **50% of the crew** to have 5+ years of experience. |
| **Duty Status** | Every member in the crew list must have `is_active=True`. |
| **ID Identification** | Mission IDs must be prefixed with the letter **'M'**. |



---

## 87 Execution Guide

### 1. Environment Setup
```bash
# Activate your environment
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install requirements
pip install pydantic flake8