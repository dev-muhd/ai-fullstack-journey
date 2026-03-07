# Day 3 & Day 4 — Student Loan Eligibility System

---

## Overview

This project implements a modular **Student Loan Eligibility System** using core Python fundamentals.

The system evolved across **Day 3 and Day 4** from a single script into a more structured mini-application with:

* Separated business logic
* Reusable validation utilities
* Structured unit testing
* Cleaner control flow design

The focus is **correctness, modular structure, and testability**.

---

## Objective

Determine whether a student qualifies for a loan based on:

* Age
* Academic grade
* Employment status

---

## Eligibility Rule

A student is eligible if:

age >= 18 AND (grade >= 70 OR employed == True)

This rule is implemented as a **pure boolean expression inside a dedicated module**.

---

# Project Structure

student-loan-eligibility/

│
├── main.py
├── utils.py
├── eligibility.py
├── test_eligibility.py
└── README.md

---

# Architecture Breakdown

## 1. Business Logic Layer

**eligibility.py**

Contains the function:

check_eligibility(age, grade, employed)

Characteristics:

* Pure function
* No input/output logic
* Returns only True or False
* Easily testable

This isolates the **core decision rule** from user interaction.

---

## 2. Validation Layer

**utils.py**

Contains reusable validation utilities.

Example function:

get_int_input(prompt, min_value=None, max_value=None)

Features:

* Generic integer validation
* Optional minimum and maximum boundaries
* Retry enforcement using `while True`
* Exit handling via `"exit"`
* Prevents invalid values from entering the system

This removes **duplicate validation logic** across the program.

---

## 3. Control Layer

**main.py**

Responsible for:

* Coordinating validation functions
* Handling early exits
* Managing employment input
* Calling the eligibility logic
* Displaying results

`main()` acts as the **program orchestrator**.

---

## 4. Testing Layer

**test_eligibility.py**

Implements unit tests for the eligibility logic.

The tests use **tuple-driven test cases**.

Example structure:

(age, grade, employed, expected_result)

Each case is validated using assertions.

---

# How to Run

Run the program:

python main.py

Run the tests:

python test_eligibility.py

Execute commands from the **project root directory**.

---

# Concepts Strengthened

* Boolean logic design
* Control flow discipline
* Input validation systems
* Separation of concerns
* Modular programming
* Assertion testing
* Tuple unpacking
* Fail-fast program design

---

# Key Design Decisions

* Eligibility logic is **pure and isolated**
* Validation logic is **reusable**
* Control flow is centralized in `main()`
* Tests validate logic **independent of CLI interaction**

---

# Future Improvements

* Introduce `pytest`
* Add automated test coverage
* Convert CLI system into an API
* Replace prints with structured logging
* Package the project as a Python module
