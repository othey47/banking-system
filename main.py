"""
Entry point for the Banking System CLI application.

This module provides a simple command-line interface (CLI) to manage different types of bank accounts:
 - Create accounts
 - Deposit money
 - Withdraw money
 - Display accounts
 - Apply interest (SavingsAccount only)

This file acts as the controller layer between the user and the account models.
"""
from account import Account
from savings import SavingsAccount
from checking import CheckingAccount


class Display:
    """
    Handles user interaction and controls application flow.
    This class:
     - Stores all created accounts in memory
     - Displays the main menu
     - Handles user input
     - Calls appropriate account operations
    """
    def __init__(self):
        # Dictionary to store accounts
        # Key   -> account ID
        # Value -> Account object
        self.accounts = {}
    
    def menu(self):
        """Display the main menu options."""
        print(f"{'=' * 20} Menu {'=' * 20}")
        print("  1. Create account.")
        print("  2. Deposit.")
        print("  3. Withdraw.")
        print("  4. Show account.")
        print("  5. Apply interest (savings only).")
        print("  0. Exit.")
        print(f"{'=' * 46} ")
    
    def create_account(self):
        """
        Create a new account based on user input.

        Supports:
         - SavingsAccount
         - CheckingAccount
        """

        acc_type = input("Enter account type (svaings/checking): ").lower()
        name = input("Enter name: ")
        balance = float(input("Enter balance:"))

        if acc_type == "savings":
            rate = float(input("Enter interest rate: "))
            account = SavingsAccount(name, balance, rate)
        elif acc_type == "checking":
            overdraft = float(input("Enter overdraft limit: "))
            account = CheckingAccount(name, balance, overdraft)
        
        # Store account using it's unique ID
        self.accounts[account.get_id()] = account
        print("Account created successfully.")
    
    def deposit_info(self):
        """Handle deposit operation for a specific account."""
        acc_id = int(input("Enter account ID: "))

        if acc_id in self.accounts:
            amount = float(input("Enter deposit amount: "))
            self.accounts[acc_id].deposit(amount)
        else:
            print("Account not found.")

    def withdraw_info(self):
        """Handle withdrawal operation for a specific account."""
        acc_id = int(input("Enter account ID: "))

        if acc_id in self.accounts:
            amount = float(input("Enter withdraw amount: "))
            self.accounts[acc_id].withdraw(amount)
    
    def show_account(self):
        """Display all stored accounts."""
        for acc in self.accounts.values():
            print(acc)

    def apply_interest(self):
        """
        Apply interest to a SavingsAccount only.
        Uses isinstance() to ensure the account type supports interest application.
        """
        acc_id = int(input("Enter account ID: "))
        account = self.accounts.get(acc_id)

        if isinstance(account, SavingsAccount):
            account.apply_interest()
        else:
            print("Interset only available for SavingsAccount.")

    def control(self):
        """
        Main application loop.

        Continuously displays the menu and executes user-selected operations until exit.
        """
        while True:
            self.menu()
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.create_account()
            elif choice == '2': 
                self.deposit_info()
            elif choice == '3':
                self.withdraw_info()
            elif choice == '4':
                self.show_account()
            elif choice == '5':
                self.apply_interest()
            elif choice == '0':
                print("Exiting application...")
                break
            else:
                print("Invalid choice: Please try again.") 
