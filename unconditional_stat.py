# break 
'''
for i in range(1, 11):
    if i == 5:
        print("Got 5. Exiting the loop!")
        break
    print(i)
'''
'''
i = 0
while True:
    i += 1
    print(i)
    if i == 3:
        print('i is 3.')
        break
'''

# continue
'''
for i in range(1, 6):
    if i == 3:
        print("Skipping 3")
        continue
    print(i)
'''

'''
shopping_list = ['butter', 'eggs', 'cookies', 'milk', 'bread']

for item in shopping_list:
    if item == 'milk':
        print("Milk is present in the list")
        break
    print("Checking items: " + item)
'''

nums = [10, -5, -3, 12, 3]
total = 0

for num in nums:
    if num < 0:
        print(f"Skipping Negative number: {num}")
        continue
    total += num # total = total + num   total = 25
print("Total: " , total)