# Function definition
'''
def add():
    a = 10
    b = 20
    print(a + b)

add() # function calling
'''
'''
name = input("Enter your name: ")
age = int(input("Enter your age: "))

def display_user(name, age): # arguments
    print(name, age)

display_user(name, age) # parameters
# print(n, a)
'''

# return keyword
def add(a, b): # a = 10, b = 20
    res = a + b
    return res
    # print('End')

ans = add(10, 20) # ans = 30
print(ans + 5)