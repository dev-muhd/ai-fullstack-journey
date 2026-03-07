# Loan Eligibility System (Learning Project)

## Overview

This project is part of my **5-month Junior AI Full-Stack Programmer journey**.

Day 5 focused on transforming a simple Python script into a **modular backend-style system** with proper architecture and testing.

The goal is to build strong fundamentals before moving into **AI systems and production applications**.

---

# What Was Built Today (Day 5)

## Modular Python Architecture

The loan eligibility system was refactored into a modular structure:

```
loan_system/
    eligibility.py
    validation.py
    storage.py
```

Each module has a clear responsibility.

### eligibility.py

Contains business logic for determining whether a loan applicant qualifies.

Example logic:

* Minimum income requirement
* Credit score requirement
* Employment status validation

---

### validation.py

Handles **safe user input**.

Functions include:

* integer validation
* employment type validation

---

### storage.py

Handles **data persistence**.

Currently saves approved loans to a file.

---

## Testing

A testing directory was introduced:

```
tests/
    test_eligibility.py
```

This validates that eligibility logic works correctly.

Example test case:

* Low credit score → rejected
* High income + good credit → approved

Testing ensures logic does not break when the system evolves.

---

# Project Structure

```
loan_system/
    __init__.py
    eligibility.py
    validation.py
    storage.py

tests/
    test_eligibility.py

main.py
README.md
```

---

# What I Learned Today

* Python module structure
* Package imports
* Separating business logic from input handling
* Creating reusable functions
* Basic testing strategy
* Debugging Python import paths

---

# Next Steps

Day 6 will introduce:

* **Data persistence with JSON**
* **Loan application history**
* **Improved system architecture**
* **More robust validation**

The goal is to gradually transform this script into a **real backend-style application**.

---

# Long Term Goal

By the end of this phase, the system will evolve into:

* a structured backend
* with data persistence
* tested business logic
* API-ready architecture

This will serve as the **foundation for later AI integrations**.
