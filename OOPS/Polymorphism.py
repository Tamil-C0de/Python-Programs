# Polymorphism -> Multiple Forms

'''
    Method Overloading
    Method Overriding
'''
'''
class Calculator:
    # def add(self, a, b):
    #     return a + b

    def add(self, a, b, c = 0): # Default Argument
        return a + b + c

calc = Calculator()
print(calc.add(2, 5))
print(calc.add(1, 2, 3))
'''

class CreditCardPayment:
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class DebitCardPayment:
    def process_payment(self, amount):
        return f"Processing debit card payment of ${amount}"

class GooglePay:
    def process_payment(self, amount):
        return f"Processing google pay payment of ${amount}"

def process_payment(payment_method, amount):
    print(payment_method.process_payment(amount))

credit = CreditCardPayment()
debit = DebitCardPayment()
gpay = GooglePay()

process_payment(credit, 2000)