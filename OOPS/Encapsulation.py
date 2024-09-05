# Encapsulation -> attributes and methods in a single unit => class

class Account:
    def __init__(self, account_num, balance):
        self.__account_num = account_num # public variable
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance: # 0 < amount and amount <= self.balance
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
    
acc = Account("123456789", 1500)
acc.deposit(500)
# print("Account Num: ", acc.__account_num)
# print("Balance: ", acc.__balance)
# acc.balance = -1000
print("Balance: ", acc.get_balance())