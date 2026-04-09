class BankAccount:
    def __init__(self, account_owner: str, account_number: str, account_type: str) -> None:
        self.account_owner = account_owner
        self.account_number = account_number
        self.__balance = 0
        self.account_type = account_type
        self.__transaction_count = 0

    def deposit(self, amount: float) -> float:
        if amount < 0:
            print("Enter a valid deposit amount")
            return None
        self.__balance += float(amount)
        self.__transaction_count += 1
        return self.__balance
    
    def withdraw(self, amount):
        if self.__balance > 0:
            self.__balance -= float(amount)
            self.__transaction_count += 1
            return self.__balance
        else:
            print("Balance is too low for this transaction")
            return None
        
    def get_balance(self):
        return f"Your account {self.account_number} is of type : {self.account_type} and present balance is : Rs.{float(self.__balance)}"

    def transfer(self, amount: float, target_account) -> str:
        if self.__balance > 0 and self.__balance > amount:
            self.withdraw(amount)
            target_account.deposit(amount)
            return f"Successfully transfered amount Rs. {amount} from {self.account_number} to {target_account.account_number}!"
        
    @property
    def balance(self):
        return self.__balance

acc_1 = BankAccount("Harvey Specter", "RBI001", "Current")
acc_2 = BankAccount("Jessica Pearson", "RBI002", "Current")


print(acc_1.get_balance())
print(acc_2.get_balance())

acc_2.deposit(1000)
acc_1.deposit(100220)
print(acc_2.get_balance())

print(acc_1.transfer(100, acc_2))

print("=================== [ENCAPSULATION on balance] ====================================")

print(acc_1.balance)
print(acc_1.balance)

# acc_1.balance = 6787        # AttributeError: property 'balance' of 'BankAccount' object has no setter
print(acc_1.balance)
