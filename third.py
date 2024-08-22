# list inbuilt functions
list1 = [2, 4 ,6, 8, 10]
#print(len(list1))

# Mutable
#list1[2] = 21
#list1[1:4] = [1, 5, 7]
#print(list1)

# append() -> add a single element
list1.append(12)
list1.append(24)
#print(list1)

# extend() -> add a list of elements
#list1.extend([1, 5, 7])
#print(list1)

# insert()
list1.insert(0, 'A')
#print(list1)

# remove()
list1.remove(10)
#print(list1)

# Tuple () -> Immutable
tuple1 = (10, 20, 30, 40)
print(tuple1[2])

#tuple1[2] = 50
list2 = list(tuple1)
print(list2, type(list2))
list2[2] = 50
tuple1 = tuple(list2)
print(tuple1, type(tuple1))

num1 = (1, 2, 3)
num2 = (4, 5, 6)
res = num1 + num2
print(num1, num2, res)

# list -> mutable and ordered, tuple -> immutable and ordered





















