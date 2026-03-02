# banking-system
A simple banking system designed to practice Object-Oriented Programming (OOP) concepts in Python, including classes, inheritance, encapsulation, and magic methods.

## Features
 - Create accounts
 - Deposit & withdraw
 - Display account info
 - Savings & Checking accounts (Inheritance)
 - Error handling

## Project Structure
'''
banking-system-oop/
│
├─ README.md                   
├─ requirements.txt            
├─ .gitignore                  
│
├─ main.py                     # Entry point (CLI menu)
│                   
├─ account.py         
├─ savings.py      
├─ checking.py     
│
├─ utils/                      
│ 
├─ tests.py/                             
│
└─ data/                       
    └─ accounts.json           
'''

## How to Use
  1. **Clone repository**
    ```bash
    git clone https://github.com/othey47/banking-system.git
    cd banking-system-oop
  2. Run main.py
    python main.py or python3 main.py
  3. Follow menu
    -> Create accounts 
    -> Deposit or withdraw money
    -> Display account info
    -> Apply interest (Savings)
    -> Use overdraft (Checking)
