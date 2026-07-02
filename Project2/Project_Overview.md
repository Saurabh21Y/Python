# Bank Management System Project Overview

## Objective

Build a CLI based Bank Management System using Object-Oriented
Programming (OOP) and JSON file storage.

## Main Features

1.  Create Bank Account
2.  Deposit Money
3.  Withdraw Money
4.  View Account Details
5.  Update Account Details
6.  Delete Account

## OOP Concepts Used

-   Class (`Bank`)
-   Object creation
-   Instance methods
-   Class methods
-   Static methods
-   Encapsulation using private helper methods
-   Method decomposition

## Python Concepts Used

-   Functions
-   Dictionaries
-   Lists
-   Loops
-   Conditional statements
-   Exception handling
-   File handling
-   JSON module
-   pathlib
-   random
-   string
-   Input validation

## Data Model

Each account stores: - Name - Age - Email - PIN - Account Number -
Balance

## Storage Strategy

Instead of SQL, data is stored inside `data.json`.

Flow: JSON File → Dummy Data (memory) → CRUD Operation → Save back to
JSON

## Validation

-   Age \>= 18
-   PIN must be 4 digits
-   Account number generated automatically
-   Initial balance = 0

## Expected Modules

-   main.py
-   data.json

## Learning Outcome

This project combines OOP, file handling, JSON persistence, validation,
CRUD operations and modular design into one practical application.
