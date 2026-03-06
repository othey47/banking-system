from account import Account
class CheckingAccount(Account):
    """
    CheckingAccount class inherits from Account.
    Adds an overdraft feature allowing withdrawals beyond the balance up to a limit. 
    Tracks how much overdraft has been used and ensures withdrawals respect the limit.
    """
    def __init__(self, name, balance, overdraft_limit):
        """
        Initialize a new CheckingAccount object.
        Parameters:
         - name (str): Customer name.
         - balance (int or float): Initial balance
         - overdraft_limit (int or float): Maximum allowed overdraft
        Raises:
         - ValueError: If overdraft_limit is not a number or <= 0 
        """
        super().__init__(name, balance)
        
        # Validate overdraft limit
        if not isinstance(overdraft_limit, (int, float)):
            raise ValueError("Overdraft limit must be a number")
        if overdraft_limit <= 0:
            raise ValueError("Overdraft limit must be positive")
        
        # Private attributes
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_used = 0 # Tracks how much of the overdraft has been used

    # Getter for overdraft limit:
    def get_overdraft_limit(self):
        """Return the maximum overdraft limit for this account."""
        return self.__overdraft_limit

    # Getter for remaining overdraft
    def get_overdraft_remaining(self):
        """Return the remaining overdraft amount available for use."""
        return self.__overdraft_limit - self.__overdraft_used

    # Withdraw method handling overdraft
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Withdraws from the balance first, then uses overdraft if necessary. 
        Parameters:
         - amount (int or float): Amount to withdraw
        Raises:
         - ValueError: If amount is invalid or execeeds available funds (balance + remaining overdraft).
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Total available funds = balance + remaining overdraft 
        available_funds = self.get_balance() + self.get_overdraft_remaining()
        if amount > available_funds:
            raise ValueError(f"Exceeds available funds: {available_funds:.2f}")
        
        # Wuthdraw from balance first:
        if amount <= self.get_balance():
            super().withdraw(amount)
        else:
            # Use entire balance and remaining from overdraft
            remaining = amount - self.get_balance()
            super().withdraw(self.get_balance())
            self.__overdraft_used += remaining

    def to_dict(self):
        """
        Convert the CheckingAccount object into a dictionary.

        This method is mainly used for:
         - Serializing account data.
         - Saving account information to JSON files.
         - Preparing structured data output
        
        Returns:
            dict: A dictionary representation of the checking account including id, type, name, balance, and overdraft limit.
        """
        return {
            "id" : self.get_id(),                                # Unique account identifier
            "type": "checking",                                  # Account type (used for reconstruction)
            "name": self.get_name(),                             # Account holder name
            "balance": self.get_balance(),                       # Current account balance
            "overdraft_limit": self.get_overdraft_limit()        # checking overdraft limit
    }
    # Override __str__ for detailed account info
    def __str__(self):
        """
        Return formatted string representation of the account.

        Includes:
         - Base account info (ID, name, balance)
         - Overdraft limit
         - Remaining overdraft available
        """
        return (
            super().__str__() +
            f", Overdraft Limit: {self.__overdraft_limit:.2f}, "
            f"Overdraft Remaining: {self.get_overdraft_remaining():.2f}"
        )