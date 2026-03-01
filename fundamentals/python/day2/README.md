 # Day 2 – Student Loan Eligibility System

## Overview

This project implements a **Student Loan Eligibility System** using core Python fundamentals:

- Comparison operators
- Logical operators (`and`, `or`)
- Boolean expressions
- Conditional statements (`if`, `elif`, `else`)
- Nested decision structures

The goal is to strengthen logical thinking and structured control flow.

---

## Objective

Determine whether a student qualifies for a loan based on:

- Age
- Academic grade
- Employment status

The program evaluates these inputs and returns an eligibility decision.

---

## Concepts Practiced

### 1. Comparison Operators
- `>`, `<`, `>=`, `<=`, `==`, `!=`

Used to evaluate age and grade requirements.

### 2. Logical Operators
- `and`
- `or`

Used to combine multiple eligibility conditions.

### 3. Boolean Logic
Understanding how conditions resolve to `True` or `False`.

### 4. Conditional Flow
- `if`
- `elif`
- `else`

Structured into a clear decision tree.

---

## Example Logic Structure

Eligibility may depend on rules such as:

- Age must be 18 or above
- Grade must meet a minimum threshold
- Either employed OR have strong academic performance

Example structure:

```python
if age >= 18 and (grade >= 70 or employed):
    print("Eligible")
else:
    print("Not eligible")