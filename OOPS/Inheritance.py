# Inheritance
'''
    Single -> 1 Parent / Base / Super, 1 Child / subclass
    Multiple
    Multilevel
    Hierarchical 

    1.Single
    BankAccount  -> SavingsAccount
'''
class BankAccount:
    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 <= amount <= self.balance: # 0 < amount and amount <= self.balance
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_num, balance, interest_rate):
        super().__init__(account_num, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)

savings = SavingsAccount("123456789", 1000, 2.0)
savings.deposit(500)
print("Balance after deposit: ", savings.get_balance())

savings.apply_interest()
print("Balance after Interest Rate: ", savings.get_balance())