# Loan Eligibility System (Learning Project)

## Overview

This project is part of my **5-month Junior AI Full-Stack Programmer journey**.

The goal is to build strong fundamentals before moving into **AI systems and production applications**.

Each day expands the system while improving architecture, testing, and code quality.

---

# What Was Built

## Day 5 — Modular Python Architecture

The loan eligibility system was refactored into a modular structure:


loan_system/
eligibility.py
validation.py
storage.py


Each module has a clear responsibility.

### eligibility.py

Contains business logic for determining whether a loan applicant qualifies.

Example logic:

- Minimum income requirement
- Credit score requirement
- Employment status validation

---

### validation.py

Handles **safe user input**.

Functions include:

- integer validation
- employment type validation

---

### storage.py

Handles **data persistence**.

Currently saves approved loans to a file.

---

## Day 6 — Validation & Control Flow Improvements

Day 6 focused on improving **input validation, exception handling, and program flow**.

The CLI system now properly validates:

- Age
- Credit score
- Income
- Employment status

Validation errors are handled using **try/except**, allowing the program to continue running without crashing.

Example validation checks:

- Age must be between realistic limits
- Credit score must be between **300–850**
- Income cannot be negative

Example interaction:


Enter age (or type 'exit'): 20
Enter credit score (or type 'exit'): 20
Validation error: Credit score must be between 300 and 850


This helped reinforce how **exception handling interacts with loops and control flow** in Python.

---

# Testing

A testing directory was introduced:


tests/
test_eligibility.py


This validates that eligibility logic works correctly.

Example test case:

- Low credit score → rejected
- High income + good credit → approved

Testing ensures logic does not break when the system evolves.

---

# Project Structure


loan_system/
__init__.py
eligibility.py
validation.py
storage.py

tests/
test_eligibility.py

main.py
README.md


---

# What I Learned

### Day 5

- Python module structure
- Package imports
- Separating business logic from input handling
- Creating reusable functions
- Basic testing strategy
- Debugging Python import paths

### Day 6

- Exception handling with `try/except`
- Input validation strategies
- Loop control and program flow
- Handling user input errors gracefully
- Designing safer CLI programs

---

# Next Steps

Day 7 will introduce:

- **Applicant data modeling**
- **JSON data persistence**
- **Saving loan application history**
- **Improved system architecture**

The goal is to gradually transform this script into a **real backend-style application**.

---

# Long Term Goal

By the end of this phase, the system will evolve into:

- a structured backend
- with data persistence
- tested business logic
- API-ready architecture

This will serve as the **foundation for later AI integrations**.