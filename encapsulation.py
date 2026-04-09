# "__" + @property = Encapsulation Enforcement

class BankAccount:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.__balance = 0            
        self.transaction_count = 0 


    @property
    def balance(self):
        return self.__balance        # Getter — controls reading

    @balance.setter
    def balance(self, value):        # Setter — controls writing
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    
account_1 = BankAccount("PewPew", "ABC123")
print(account_1.balance)
account_1.balance = 1111        # Works since non-negative
print(account_1.balance)
account_1.balance = -9999       # ValueError: Balance cannot be negative
print(account_1.balance)



