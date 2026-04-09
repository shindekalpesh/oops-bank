class BankAccount:
    def __init__(self, account_owner: str, account_number: str, account_type: str) -> None:
        self.account_owner = account_owner
        self.account_number = account_number
        self.balance = 0
        self.account_type = account_type
        self.__transaction_count = 0

    def deposit(self, amount: float) -> float:
        self.balance += float(amount)
        self.__transaction_count += 1
        return self.balance
    
    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= float(amount)
            self.__transaction_count += 1
            return self.balance
        else:
            return "Balance is too low for this transaction"
        
    def get_balance(self):
        return f"Your account {self.account_number} is of type : {self.account_type} and present balance is : Rs.{float(self.balance)}"

    def transfer(self, amount: float, target_account) -> str:
        if self.balance > 0 and self.balance > amount:
            self.withdraw(amount)
            target_account.deposit(amount)
            return f"Successfully transfered amount Rs. {amount} from {self.account_number} to {target_account.account_number}!"
        
    # @property
    # def balance(self):
    #     return self.balance

acc_1 = BankAccount("Harvey Specter", "RBI001", "Current")
acc_2 = BankAccount("Jessica Pearson", "RBI002", "Current")


print(acc_1.get_balance())
print(acc_2.get_balance())

acc_2.deposit(1000)
acc_1.deposit(100220)
print(acc_2.get_balance())

print(acc_1.transfer(100, acc_2))

print("=================== [ENCAPSULATION] ====================================")

print(acc_1.balance)

acc_1.balance = 6787
print(acc_1.balance)
