# Exception Handling
'''
try:
    res = 10 / 2
    print(res)
except ZeroDivisionError as e:
    print("Error: Cannot Divide by Zero")
print("End")
'''

try:
    num = int(input("Enter a number: "))
    print(num)
except Exception as e:
    print("Error: Please enter a valid number")
    print(e)
finally:
    print("Program End")