# -*- coding: utf-8 -*-
"""
=========================================
  Bank Management System
  CLI | OOP | JSON Storage
=========================================
"""

import sys
import io
import json
import random
import string
from pathlib import Path

# Ensure UTF-8 output on Windows terminals (handles ₹ and box-drawing chars)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


# ─────────────────────────────────────────
#  Constants
# ─────────────────────────────────────────
DATA_FILE = Path(__file__).parent / "data.json"

MENU = """
╔══════════════════════════════════════════╗
║        BANK MANAGEMENT SYSTEM            ║
╠══════════════════════════════════════════╣
║  [1]  Create Account                     ║
║  [2]  Deposit Money                      ║
║  [3]  Withdraw Money                     ║
║  [4]  View Account Details               ║
║  [5]  Update Account Details             ║
║  [6]  Delete Account                     ║
║  [0]  Exit                              ║
╚══════════════════════════════════════════╝
"""


# ─────────────────────────────────────────
#  Bank Class
# ─────────────────────────────────────────
class Bank:
    """
    Core banking class responsible for all operations.

    Storage strategy:
        JSON File ──► Load into memory (list of dicts)
                  ──► Perform CRUD operation
                  ──► Save entire list back to JSON
    """

    # ── Private helpers ──────────────────

    def _load_data(self) -> list:
        """Load accounts from JSON file into memory."""
        if not DATA_FILE.exists():
            return []
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("[!] Warning: Could not read data file. Starting fresh.")
            return []

    def _save_data(self, accounts: list) -> None:
        """Persist the in-memory list back to JSON file."""
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(accounts, f, indent=4)
        except IOError as e:
            print(f"[!] Error saving data: {e}")

    def _generate_account_number(self, accounts: list) -> str:
        """Generate a unique 10-digit account number."""
        existing = {acc["account_number"] for acc in accounts}
        while True:
            acc_num = "".join(random.choices(string.digits, k=10))
            if acc_num not in existing:
                return acc_num

    def _find_account(self, accounts: list, account_number: str) -> dict | None:
        """Return the account dict matching the account number, or None."""
        for acc in accounts:
            if acc["account_number"] == account_number:
                return acc
        return None

    def _authenticate(self, account: dict, pin: str) -> bool:
        """Verify PIN against the stored account PIN."""
        return account["pin"] == pin

    # ── Validation ───────────────────────

    @staticmethod
    def _validate_age(age_str: str) -> int:
        """
        Validate age input.
        Returns age as int if valid, raises ValueError otherwise.
        """
        age = int(age_str)
        if age < 18:
            raise ValueError("Age must be 18 or above.")
        return age

    @staticmethod
    def _validate_pin(pin: str) -> str:
        """
        Validate PIN to be exactly 4 numeric digits.
        Returns PIN if valid, raises ValueError otherwise.
        """
        if not (len(pin) == 4 and pin.isdigit()):
            raise ValueError("PIN must be exactly 4 digits.")
        return pin

    @staticmethod
    def _validate_amount(amount_str: str) -> float:
        """
        Validate that amount is a positive number.
        Returns amount as float if valid, raises ValueError otherwise.
        """
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount

    # ── FR-1: Create Account ─────────────

    def create_account(self) -> None:
        """Collect details, validate, generate account number, and save."""
        print("\n── Create New Account ──")
        try:
            name  = input("  Full Name   : ").strip()
            if not name:
                print("[!] Name cannot be empty.")
                return

            age   = self._validate_age(input("  Age         : ").strip())
            email = input("  Email       : ").strip()
            if "@" not in email:
                print("[!] Invalid email address.")
                return

            pin = self._validate_pin(input("  Set 4-digit PIN : ").strip())

        except ValueError as e:
            print(f"[!] Validation Error: {e}")
            return

        accounts   = self._load_data()
        acc_number = self._generate_account_number(accounts)

        new_account = {
            "account_number": acc_number,
            "name":           name,
            "age":            age,
            "email":          email,
            "pin":            pin,
            "balance":        0.0,
        }

        accounts.append(new_account)
        self._save_data(accounts)

        print(f"\n  ✔ Account created successfully!")
        print(f"  ► Account Number : {acc_number}")
        print(f"  ► Initial Balance: ₹0.00")
        print("  [Save your account number safely!]\n")

    # ── FR-2: Deposit Money ──────────────

    def deposit(self) -> None:
        """Authenticate user and add amount to balance."""
        print("\n── Deposit Money ──")
        acc_num = input("  Account Number : ").strip()
        pin     = input("  PIN            : ").strip()

        accounts = self._load_data()
        account  = self._find_account(accounts, acc_num)

        if not account:
            print("[!] Account not found.")
            return
        if not self._authenticate(account, pin):
            print("[!] Incorrect PIN.")
            return

        try:
            amount = self._validate_amount(input("  Amount to Deposit (₹): ").strip())
        except ValueError as e:
            print(f"[!] {e}")
            return

        account["balance"] += amount
        self._save_data(accounts)
        print(f"\n  ✔ ₹{amount:.2f} deposited successfully.")
        print(f"  ► New Balance: ₹{account['balance']:.2f}\n")

    # ── FR-3: Withdraw Money ─────────────

    def withdraw(self) -> None:
        """Authenticate user, check balance, and deduct amount."""
        print("\n── Withdraw Money ──")
        acc_num = input("  Account Number : ").strip()
        pin     = input("  PIN            : ").strip()

        accounts = self._load_data()
        account  = self._find_account(accounts, acc_num)

        if not account:
            print("[!] Account not found.")
            return
        if not self._authenticate(account, pin):
            print("[!] Incorrect PIN.")
            return

        try:
            amount = self._validate_amount(input("  Amount to Withdraw (₹): ").strip())
        except ValueError as e:
            print(f"[!] {e}")
            return

        if amount > account["balance"]:
            print(f"[!] Insufficient balance. Available: ₹{account['balance']:.2f}")
            return

        account["balance"] -= amount
        self._save_data(accounts)
        print(f"\n  ✔ ₹{amount:.2f} withdrawn successfully.")
        print(f"  ► Remaining Balance: ₹{account['balance']:.2f}\n")

    # ── FR-4: View Account Details ───────

    def view_account(self) -> None:
        """Display account information (PIN is hidden)."""
        print("\n── View Account Details ──")
        acc_num = input("  Account Number : ").strip()
        pin     = input("  PIN            : ").strip()

        accounts = self._load_data()
        account  = self._find_account(accounts, acc_num)

        if not account:
            print("[!] Account not found.")
            return
        if not self._authenticate(account, pin):
            print("[!] Incorrect PIN.")
            return

        print("\n  ┌─────────────────────────────────┐")
        print(f"  │  Account Number : {account['account_number']}")
        print(f"  │  Name           : {account['name']}")
        print(f"  │  Age            : {account['age']}")
        print(f"  │  Email          : {account['email']}")
        print(f"  │  Balance        : ₹{account['balance']:.2f}")
        print(f"  │  PIN            : ****")
        print("  └─────────────────────────────────┘\n")

    # ── FR-5: Update Account Details ─────

    def update_account(self) -> None:
        """Allow updating name, age, and email. PIN update included."""
        print("\n── Update Account Details ──")
        acc_num = input("  Account Number : ").strip()
        pin     = input("  PIN            : ").strip()

        accounts = self._load_data()
        account  = self._find_account(accounts, acc_num)

        if not account:
            print("[!] Account not found.")
            return
        if not self._authenticate(account, pin):
            print("[!] Incorrect PIN.")
            return

        print("\n  Which field to update?")
        print("  [1] Name")
        print("  [2] Age")
        print("  [3] Email")
        print("  [4] PIN")
        print("  [0] Cancel")
        choice = input("  Choice: ").strip()

        try:
            if choice == "1":
                new_val = input("  New Name: ").strip()
                if not new_val:
                    print("[!] Name cannot be empty.")
                    return
                account["name"] = new_val

            elif choice == "2":
                account["age"] = self._validate_age(input("  New Age: ").strip())

            elif choice == "3":
                new_email = input("  New Email: ").strip()
                if "@" not in new_email:
                    print("[!] Invalid email.")
                    return
                account["email"] = new_email

            elif choice == "4":
                new_pin = self._validate_pin(input("  New 4-digit PIN: ").strip())
                account["pin"] = new_pin

            elif choice == "0":
                print("  Update cancelled.")
                return
            else:
                print("[!] Invalid choice.")
                return

        except ValueError as e:
            print(f"[!] Validation Error: {e}")
            return

        self._save_data(accounts)
        print("  ✔ Account updated successfully.\n")

    # ── FR-6: Delete Account ─────────────

    def delete_account(self) -> None:
        """Authenticate user and remove account from storage."""
        print("\n── Delete Account ──")
        acc_num = input("  Account Number : ").strip()
        pin     = input("  PIN            : ").strip()

        accounts = self._load_data()
        account  = self._find_account(accounts, acc_num)

        if not account:
            print("[!] Account not found.")
            return
        if not self._authenticate(account, pin):
            print("[!] Incorrect PIN.")
            return

        confirm = input(f"  ⚠ Are you sure you want to delete account {acc_num}? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("  Deletion cancelled.")
            return

        accounts.remove(account)
        self._save_data(accounts)
        print(f"  ✔ Account {acc_num} deleted successfully.\n")


# ─────────────────────────────────────────
#  Main Entry Point
# ─────────────────────────────────────────
def main() -> None:
    bank = Bank()

    actions = {
        "1": bank.create_account,
        "2": bank.deposit,
        "3": bank.withdraw,
        "4": bank.view_account,
        "5": bank.update_account,
        "6": bank.delete_account,
    }

    while True:
        print(MENU)
        choice = input("  Enter your choice: ").strip()

        if choice == "0":
            print("\n  Thank you for using Bank Management System. Goodbye!\n")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("\n  [!] Invalid option. Please choose from the menu.\n")


if __name__ == "__main__":
    main()
