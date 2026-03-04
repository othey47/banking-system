# banking-system
A simple banking system designed to practice Object-Oriented Programming (OOP) concepts in Python, including classes, inheritance, encapsulation, and magic methods.

## Features
 - Create accounts (Savings or Checking)
 - Deposit & withdraw
 - Display account info
 - Apply interest for SavingsAccount
 - Handle overdraft for CheckingAccount
 - Data persistence to JSON file
 - Input validation and error handling
 - CLI menu interface

## Project Structure
```
 banking-system-oop/
 │
 ├─ README.md                   
 ├─ requirements.txt            
 ├─ .gitignore                  
 │
 ├─ main.py                     # Entry point (CLI menu + persistence)
 │                   
 ├─ account.py                  # Base Account class
 ├─ savings.py                  # SavingsAccount subclass
 ├─ checking.py                 # CheckingAccount subclass
 │
 ├─ utils/                      # Optional helpers(validators, etc.)
 │ 
 ├─ tests.py/                   # Test cases for accounts and CLI
 │                             
 ├─ storage.py                  # JSON storage for accounts & transactions
 │
 └─ accounts.json  
           
```

## How to Use
  1. **Clone repository**
    ```bash
    git clone https://github.com/othey47/banking-system.git
    cd banking-system-oop
  2. Run main.py
    python main.py or python3 main.py
  3. Follow menu
    -> Create accounts (Savings or Checking)
    -> Deposit or withdraw money
    -> Display account information
    -> Apply interest (SavingsAccount only)
    -> Use overdraft (CheckingAccount)

## Notes
 - All accounts are automatically saved to 'data/accounts.json' after each operation.
 - Savings accounts have an interest rate applied using 'apply_interest()'.
 - Checking accounts support overdraft, tracked and validated automatically.
 - Input validation prevents invalid names, balances, deposits, withdrawals, interest rates, or overdraft limits.
