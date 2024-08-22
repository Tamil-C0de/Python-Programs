'''
name = "John"
age = 25
# My name is John and my age is 25
print("My name is " + name + " and my age is " + str(age)) # Concatenation
print("My name is {1} and my age is {0}".format(age, name))
# f-string |   String Interpolation
print(f"My name is {name} and my age is {age}")
'''
'''
name = input("Enter a name: ")
age = int(input('Enter your age: '))
# age = int(age)
print(type(name), type(age))
'''

# Indentation
# Branching Statements -> Boolean values
'''
x = int(input("Enter a num: "))
if x > 0: # True -> Execute
    print(f'{x} is a Positive Number')
elif x == 0:
    print("It is Zero.")
else:
    print(f'{x} is a Negative Number')
'''
# Nested if
x = int(input("Enter a three digit number: ")) # 3-digit and even number

if x >= 100 and x <= 999:
    if x % 2 == 0 and x % 4 == 0:
        print(f"{x} is a 3-digit even number")
        # if x % 4 == 0:
        #     print(f"{x} is divisible by 4")
    else:
        print(f"{x} is a 3-digit but not an even number")
else:
        print(f"{x} is not a 3-digit even number")