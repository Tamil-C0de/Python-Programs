# Factorial -> 5! => 5 * 4 * 3 * 2 * 1 -> 120
# 0! -> 1  1! -> 1

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# print(factorial(5))

# 0 1 1 2 3 5 8...........
# I: n = 6  O: 8
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))
# 5 -> 5 + 4 + 3 + 2 + 1 => 15
def sum_n_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_n_numbers(n - 1)

# print(sum_n_numbers(5))

# Lambda Functions
# students = [('Ram', 85),('Kumar', 92),('Fayas', 70), ('Raj', 63)]

# def get_score(student):
#     return student[1]

# print(sorted(students, key=get_score))

# def square(n):
#     return n * n
# square = lambda n: n * n
# print(square(5))

list1 = [1, 2, 3, 4, 5]

res = []
for x in list1:
    res.append((lambda x: x * 2)(x))

print(res)