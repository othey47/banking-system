"""
Entry point for the Banking System CLI application.

This module provides a command-line interface (CLI) to manage different types of bank accounts:
 - Create accounts
 - Deposit money
 - Withdraw money
 - Display accounts
 - Apply interest (SavingsAccount only)
 - Persist data to a JSON file

This file acts as the controller layer between the user and the account models.
"""
from account import Account
from savings import SavingsAccount
from checking import CheckingAccount
from storage import Storage

class Display:
    """
    Handles user interaction and controls application flow.
    Responsibilities:
     - Stores all created accounts in memory
     - Displays the main menu
     - Handles user input
     - Calls appropriate account operations
     - Persists data to JSON file via Storage
    """
    def __init__(self):
        '''
        Initialize Display instance.
         - Creates an empty accounts dictionary.
         - Initializes the storage object.
         - Loads previously saved accounts from JSON.
        '''
        # Key: account ID, Value: Account object
        self.accounts = {}
        # Storage object for JSON persistence
        self.storage = Storage()
        # Load saved account at startup
        self.load_accounts()
    
    def load_accounts(self):
        """
        Load accounts from storage (JSON file) into memory.
        Restores account objects with their type, balance, and ID. 
        """
        data = self.storage.load()

        for acc in data.get("accounts", []):

            if acc['type'] == "savings":
                account = SavingsAccount(
                    acc['name'],
                    acc['balance'],
                    acc['interest_rate']
                )
            elif acc['type'] == "checking":
                account = CheckingAccount(
                    acc['name'],
                    acc['balance'],
                    acc['overdraft_limit']
                )
            
            # Restore original ID to maintain consistency 
            account.set_id(acc['id']) 
            self.accounts[account.get_id()] = account 


    def menu(self):
        """Display the main menu options to the user."""
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
        Returns:
            bool: True if account created successfully, False otherwise.
        """

        acc_type = input("Enter account type (savings/checking): ").lower()
        name = input("Enter name: ")
        balance = float(input("Enter balance: "))

        if acc_type == "savings":
            rate = float(input("Enter interest rate: "))
            account = SavingsAccount(name, balance, rate)
        elif acc_type == "checking":
            overdraft = float(input("Enter overdraft limit: "))
            account = CheckingAccount(name, balance, overdraft)
        else:
            print("Invalid account type.")
            return False
        
        # Store account in memory
        self.accounts[account.get_id()] = account
        print("Account created successfully.")
        return True
    
    def deposit_info(self):
        """
        Handle deposit operation for a specific account.
        Returns:
            bool: True if deposit was successful, False if account not found.
        """
        acc_id = int(input("Enter account ID: "))

        if acc_id in self.accounts:
            amount = float(input("Enter deposit amount: "))
            return self.accounts[acc_id].deposit(amount)
        else:
            print("Account not found.")
            return False
        
    def withdraw_info(self):
        """
        Handle withdrawal operation for a specific account.

        Returns:
            bool: True if withdraw was successful, False if account not found.
        """
        acc_id = int(input("Enter account ID: "))

        if acc_id in self.accounts:
            amount = float(input("Enter withdraw amount: "))
            return self.accounts[acc_id].withdraw(amount)
        else:
            print("Account not found.")
            return False
    
    def show_account(self):
        """Display all stored accounts. if no accounts exist, print a message."""
        if not self.accounts:
            print("accounts not found.")
        else:
            for acc in self.accounts.values():
                print(acc)

    def save_all_accounts(self):
        """
        Persist all account data to a JSON file.
        Converts account objects to dictionaries for storage.
        """
        data = {
            "accounts": [acc.to_dict() for acc in self.accounts.values()]
        }
        self.storage.save(data)

    def apply_interest(self):
        """
        Apply interest to a SavingsAccount only.
        Uses isinstance() to ensure the account type supports interest application.

        Returns:
            bool: True if interest applied, False if account not found or invalid type.
        """
        acc_id = int(input("Enter account ID: "))
        account = self.accounts.get(acc_id)
        
        if account is None:
            print("Account not found.")
            return False
        elif isinstance(account, SavingsAccount):
            account.apply_interest()
            return True
        else:
            print("Interest only available for SavingsAccount.")
            return False

    def control(self):
        """
        Main application loop.

        Continuously displays the menu and executes user-selected operations until exit.
        Automatically saves data after every successful operation.
        """
        while True:
            self.menu()
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                if self.create_account():
                    self.save_all_accounts()
            elif choice == '2': 
                if self.deposit_info():
                    self.save_all_accounts()
            elif choice == '3':
                if self.withdraw_info():
                    self.save_all_accounts()
            elif choice == '4':
                self.show_account()
            elif choice == '5':
                if self.apply_interest():
                    self.save_all_accounts()
            elif choice == '0':
                print("Exiting application...")
                break
            else:
                print("Invalid choice: Please try again.") 

