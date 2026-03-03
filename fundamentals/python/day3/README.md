# Day 3 — Student Loan Eligibility System

---

## Overview

This project implements a Student Loan Eligibility System using core Python fundamentals.

It focuses on disciplined control flow and strict input validation.

Concepts applied:

- Comparison operators
- Logical operators (`and`, `or`)
- Boolean expressions
- Conditional statements (`if`, `elif`, `else`)
- Nested decision structures
- `while True` validation loops
- `continue` control flow behavior

The goal is to strengthen logical thinking and structured program design.

---

## Objective

Determine whether a student qualifies for a loan based on:

- Age
- Academic grade
- Employment status

---

## Eligibility Rule

A student is eligible if:

```
age >= 18 AND (grade >= 70 OR employed == True)
```

This condition is implemented as a pure boolean expression inside a dedicated function.

---

## Program Structure

### Business Logic Layer

`check_eligibility(age, grade, employed)`

- Pure function
- Returns `True` or `False`
- Contains no input/output logic

---

### Input Validation Layer

Functions:

- `get_valid_age()`
- `get_valid_grade()`
- `get_valid_employment()`

Each function:

- Uses `while True` to enforce retries
- Prevents invalid data from passing forward
- Allows user to type `"exit"` to terminate early
- Returns `None` when exiting

---

### Control Layer

`main()`

Responsible for:

- Coordinating validation functions
- Handling early exits
- Managing retry prompts
- Maintaining clean control flow

---

## How to Run

```bash
python main.py
```

---

## What This Project Strengthened

- Logical grouping of conditions
- Avoiding messy nested conditionals
- Understanding operator precedence
- Clear separation of concerns
- Designing retry systems using loops
- Preventing fallthrough errors

---

## Future Improvements

- Add unit tests for eligibility logic
- Refactor validation into reusable utilities
- Add input sanitization edge-case handling
- Convert CLI system into API endpoint