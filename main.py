class BankAccount:
    def __init__(self, account_owner: str, account_number: str, account_type: str) -> None:
        self.account_owner = account_owner
        self.account_number = account_number
        self.account_balance = 0
        self.account_type = account_type
        self.transaction_count = 0

    def deposit(self, amount: float) -> float:
        self.account_balance += float(amount)
        self.transaction_count += 1
        return self.account_balance
    
    def withdraw(self, amount):
        if self.account_balance > 0:
            self.account_balance -= float(amount)
            self.transaction_count += 1
            return self.account_balance
        else:
            return "Balance is too low for this transaction"
        
    def get_balance(self):
        return f"Your account {self.account_number} is of type : {self.account_type} and present balance is : Rs.{float(self.account_balance)}"

    def transfer(self, amount: float, target_account) -> str:
        if self.account_balance > 0 and self.account_balance > amount:
            self.withdraw(amount)
            target_account.deposit(amount)
            return f"Successfully transfered amount Rs. {amount} from {self.account_number} to {target_account.account_number}!"

acc_1 = BankAccount("Harvey Specter", "RBI001", "Current")
acc_2 = BankAccount("Jessica Pearson", "RBI002", "Current")

# print(acc_1.transaction_count)
# print(acc_2.transaction_count)
# acc_2.deposit(1000)
# acc_1.deposit(10)
# acc_2.withdraw(10)
# print(acc_1.transaction_count)
# print(acc_2.transaction_count)


print(acc_1.get_balance())
print(acc_2.get_balance())

acc_2.deposit(1000)
print(acc_2.get_balance())

print(acc_1.transfer(100, acc_2))

# acc_2.transfer(250, acc_1)
# print(acc_1.get_balance())
# print(acc_2.get_balance())
# print(acc_1.transfer(50, acc_2))
# print(acc_1.get_balance())
# print(acc_2.get_balance())
# print(acc_1.transfer())

print("===============================================================")

acc_1._deposit(5555555)
print(acc_1._get_balance())