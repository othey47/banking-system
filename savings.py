
from account import Account


class SavingsAccount(Account):
    """
    SavingsAccount class inherits from Account.
    Adds an interest rate feature and allows internet application.
    """
    def __init__(self, name, balance, interest_rate):
        """
        Initialize a new SavingsAccount object.
        Parameters:
         - name (str): Customer name.
         - balance (int or float): Initial balance.
         - interest_rate (int or float): Interest rate (as decimal, e.g., 0.05 for 5%).
        Raises:
         - ValueError: If interest_rate is not a number or <= 0
        """
        super().__init__(name, balance)
        
        # Validate interest rate: must be int or float.
        if not isinstance(interest_rate,(int, float)):
            raise ValueError("Invalid input: interest rate must be a number (int or float).")
        if interest_rate <= 0:
            raise ValueError("Invalid input: interest rate must be positive.")
        
        # Private attribute for interset rate. 
        self.__interest_rate = interest_rate

    # Getter for interset rate
    def get_interest_rate(self):
        """Return the current interset rate of the account"""
        return self.__interest_rate
    # Apply interset to balance
    def apply_interest(self):
        """
        Apply interset to the current balance.
        Uses the formula: balance += balance * interset_rate
        """
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
    # Override __str__ for detailed account info
    def __str__(self):
        """Return formatted account info including interest rate"""
        return super().__str__() + f", Interest Rate: {self.__interest_rate * 100:.2f}%"    

