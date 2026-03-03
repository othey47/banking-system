
class Account:
    # # Class variable to auto-increment account IDs for each new account
    _id_counter = 1

    def __init__(self, name, balance):
        """
        Initialize a new account object.
        Parameters:
         - name (str): Customer name, must be non-empty string.
         - balance (int or float): Initial balance, must be positive.
        Raises:
         - ValueError: If name or balance is invalid.
        """
        # Validate name: must be string and not empty.
        if not isinstance(name, str):
            raise ValueError("Invalid name: must be string")
        if not name.strip(): # strip() to avoid whitespace-only names.
            raise ValueError("Invalid name: cannot be empty")
        
        # Validate balance: must be positive.
        if balance <= 0:
            raise ValueError("Invalid balance: must non-negative")
        
        # Assign private attributes.
        self.__name = name
        self.__balance = balance
        self.__id = Account._id_counter
        
        # Increment class-level ID counter.
        Account._id_counter += 1


    # Getter for account ID.
    def get_id(self):
        """Return the unique account ID"""
        return self.__id
    
    # Getter for account name.
    def get_name(self):
        """Return the account holder's name"""
        return self.__name
    
    # Getter for account balance.
    def get_balance(self):
        """Return the current account balance"""
        return self.__balance


    def deposit(self, amount):
        """
        Deposit money into the account.
        Parameters:
         - amount (int or float): Amount to deposit.
        Raises:
         - ValueError: If amount is not a number or is non-negative
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid amount: must be a number")
        if amount <= 0:
            raise ValueError("Invalid amount: must be positive.")
        
        # Add amount to balance. 
        self.__balance += amount


    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Parameters:
         - amount (int or float): Amount to withdraw.
        Raises:
         - ValueError: If amount is invalid or exceeds balance
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid amount: must be a number")
        if amount <= 0:
            raise ValueError("Invalid amount: must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        
        # Subtract amount from balance
        self.__balance -= amount

    def __str__(self):
        """Return a formatted string with account info""" 
        return f"Account ID: {self.__id}, Name: {self.__name}, Balance: {self.__balance:.2f}"