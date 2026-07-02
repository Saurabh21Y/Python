# Requirement Specification

## Project

Bank Management System (CLI)

## Purpose

Develop a console application that manages customer bank accounts using
JSON as persistent storage.

## Functional Requirements

### FR-1 Create Account

Input: - Name - Age - Email - PIN

System shall: - Validate age and PIN - Generate unique account number -
Initialize balance to 0 - Save account into JSON

### FR-2 Deposit Money

Input: - Account Number - PIN - Amount

System shall: - Authenticate user - Increase balance - Save updated data

### FR-3 Withdraw Money

Input: - Account Number - PIN - Amount

System shall: - Authenticate - Check sufficient balance - Deduct
amount - Save data

### FR-4 View Details

Display all customer information except sensitive data if desired.

### FR-5 Update Details

Allow updating editable fields and persist changes.

### FR-6 Delete Account

Authenticate user and remove account from storage.

## Internal Design

### Bank Class

Responsible for all banking operations.

### Persistent Storage

`data.json` acts as database.

### Runtime Flow

1.  Load JSON into memory.
2.  Perform operations on in-memory list.
3.  Write entire list back to JSON.

### Helper Methods

-   Load data
-   Save data
-   Generate account number
-   Validate inputs

### Suggested Folder Structure

    BankManagement/
    │── main.py
    │── data.json

## Non-functional Requirements

-   Clean code
-   Modular methods
-   Exception handling
-   Easy maintenance
-   Extendable architecture

## Future Improvements

-   Login system
-   Transaction history
-   Interest calculation
-   Multiple account types
-   Password hashing
-   SQLite/MySQL migration
