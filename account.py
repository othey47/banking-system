


class Account:
    # class variable: id counter
    _id_counter = 1

    def __init__(self, name, balance):
        # 1 validate name
        #   - must be string
        if not isinstance(name, str):
            raise ValueError("Invalid name")
        #   - must not be empty
        if not name:
            raise ValueError("Empty name")
        
        # 2 validate balance
        #   - must not be negative
        if balance < 1:
            raise ValueError("Invalid balance, blance must be positive")
        
        # 4 assign private attributes:
        #   __name
        self.__name = name
        #   __balance
        self.__balance = balance
        #   __id
        self.__id = Account._id_counter
        
        # 5 increment class counter
        Account._id_counter += 1


    # getter for id
    def get_id(self):
        return self.__id
    # getter for name
    def get_name(self):
        return self.__name
    # getter for balance
    def get_balance(self):
        return self.__balance


    def deposit(self, amount):
        # 1 validate amount
        #  - must be intger or float
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid amount")
       
        # 2 validate amount
        #   - must be positive
        if amount < 1:
            raise ValueError("Invalid amount, amount must be positive.")
        # 3 add amount to balance
        self.__balance += amount


    def withdraw(self, amount):
        # 1 validate amount
        #  - must be intger or float
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid amount")

        # 2 validate amount
        #   - must be positive
        if amount < 1:
            raise ValueError("Invalid amount, amount must be positive.")
        
        # 3 check if amount > balance
        #   - raise error if not enough
        if amount > self.__balance:
            raise ValueError()
        
        # 4 subtract amount from balance
        self.__balance -= amount

    def __str__(self):
         return f"Account ID: {self.__id}, Name: {self.__name}, Balance: {self.__balance}"


acc = Account("Ali", 100.50)
acc.deposit(50.25)
acc.withdraw(20.10)
print(acc.get_balance())
print(acc)