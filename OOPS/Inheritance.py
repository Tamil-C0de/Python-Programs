# Inheritance
'''
    Single -> 1 Parent / Base / Super, 1 Child / subclass
    Multiple -> one or more parent classes, 1 Child 
    Multilevel
    Hierarchical 

    1.Single
    BankAccount  -> SavingsAccount
'''
# class BankAccount:
#     def __init__(self, account_num, balance):
#         self.account_num = account_num
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Deposit amount must be positive.")
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance: # 0 < amount and amount <= self.balance
#             self.balance -= amount
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.balance

# class SavingsAccount(BankAccount):
#     def __init__(self, account_num, balance, interest_rate):
#         super().__init__(account_num, balance)
#         self.interest_rate = interest_rate

#     def apply_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         self.deposit(interest)

# savings = SavingsAccount("123456789", 1000, 2.0)
# savings.deposit(500)
# print("Balance after deposit: ", savings.get_balance())

# savings.apply_interest()
# print("Balance after Interest Rate: ", savings.get_balance())

'''
    Multiple Inheritance
'''
# class BankAccount:
#     def __init__(self, account_num, balance):
#         self.account_num = account_num
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Deposit amount must be positive.")
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance: # 0 < amount and amount <= self.balance
#             self.balance -= amount
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.balance

# class Customer:
#     def __init__(self, name):
#         self.name = name
    
#     def get_name(self):
#         return self.name

# class PremiumAccount(BankAccount, Customer):
#     def __init__(self, account_num, balance, name, benefits):
#         BankAccount.__init__(self, account_num, balance)
#         Customer.__init__(self, name)
#         self.benefits = benefits

#     def show_benefits(self):
#         print(f"Benefits for {self.get_name()}: {self.benefits}")

# premium = PremiumAccount("123456789", 1000, "Kumar", "Credit Card Free")
# premium.deposit(500)
# print("Balance after deposit: ", premium.get_balance())

# premium.show_benefits()


'''
    Multilevel 
    Parent Class
    Child class (parent)
    Child class
'''
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
        if 0 < amount <= self.balance: # 0 < amount and amount <= self.balance
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

class StudentSavingsAccount(SavingsAccount):
    def __init__(self, account_num, balance, interest_rate, student_id):
        super().__init__(account_num, balance, interest_rate)
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

student_account = StudentSavingsAccount("123456789", 1000, 2.0, "S123")
student_account.deposit(500)
print("Balance after deposit: ", student_account.get_balance())

student_account.apply_interest()
print("Balance after Interest Rate: ", student_account.get_balance())

print("Student ID:", student_account.get_student_id())
'''

'''
    Hierarchical -> 1 Parent, one or more child
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
        if 0 < amount <= self.balance: # 0 < amount and amount <= self.balance
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

class CheckingAccount(BankAccount):
    def __init__(self, account_num, balance, overdraft_limit):
        super().__init__(account_num, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit: # 5200 > 5500
            print("Exceeded Limit.")
        else:
            self.balance -= amount # balance = 5000 - 5200

savings = SavingsAccount("123456789", 2500, 3.5)
checking = CheckingAccount("987654321", 5000, 500)

savings.deposit(500)
print("Balance after deposit: ", savings.get_balance())

savings.apply_interest()
print("Balance after Interest Rate: ", savings.get_balance())

checking.withdraw(5200)
print("Checking Balance after withdraw:", checking.get_balance())