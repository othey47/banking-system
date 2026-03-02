from account import Account
class CheckingAccount(Account):
    """
    => CheckingAccount class inherits from Account.
    => Adds an overdraft feature allowing withdrawals beyond the balance up to a limit. 
    """
    def __init__(self, name, balance, overdraft_limit):
        """
        => Initialize a new CheckingAccount object.
        => Parameters:
         - name (str): Customer name
         - balance (int or float): Initial balance
         - overdraft_limit (int or float): Maximum allowed overdraft
        => Raises:
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

    # Getter for remaining overdraft
    def get_overdraft_remaining(self):
        """Return the remaining overdraft amount available"""
        return self.__overdraft_limit - self.__overdraft_used

    # Withdraw method handling overdraft
    def withdraw(self, amount):
        """
        => Withdraw money from the account, using balance first, then overdraft if needed.
        => Parameters:
         - amount (int or float): Amount to withdraw
        => Raises:
         - ValueError: If amount is invalid or execeeds available funds
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        available_funds = self.get_balance() + self.get_overdraft_remaining()
        if amount > available_funds:
            raise ValueError("Exceeds available funds: {available_funds:.2f}")
        
        # Wuthdraw from balance first:
        if amount <= self.get_balance():
            super().withdraw(amount)
        else:
            # Use entire balance and remaining from overdraft
            remaining = amount - self.get_balance()
            super().withdraw(self.get_balance())
            self.__overdraft_used += remaining
    # Override __str__ for detailed account info
    def __str__(self):
        """
        Return formatted account info including overdraft limit and remaining overdraft
        """
        return (
            super().__str__() +
            f", Overdraft Limit: {self.__overdraft_limit:.2f}, "
            f"Overdraft Remaining: {self.get_overdraft_remaining():.2f}"
        )