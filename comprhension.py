# list comprehension
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = [num for num in nums if num % 2 == 0]

# for num in nums:
#     if num % 2 == 0:
#         even_nums.append(num)

print(even_nums)

# (value * 9/5) + 32
celsius_values = [0, 10, 20, 30, 40]
fahrenheit_values = [(value * 9/5) + 32 for value in celsius_values]
print(fahrenheit_values)
'''

# Dictionary Comprehension
# {1: 1, 2: 4, 3: 9}
squares = {number:number*number for number in range(1, 6)}

# for number in range(1, 6):
#     squares[number] = number * number

print(squares)