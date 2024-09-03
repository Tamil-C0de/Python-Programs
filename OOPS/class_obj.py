'''
class Car:
    brand = "Toyota"
    color = "Red"

    def start_engine(self):
        print("Engine Started.", self.brand)

# Object creation
car1 = Car() # constructor
print(car1.brand)
car1.start_engine()

car2 = Car()
car2.brand = "Honda"
car2.color = "White"
print(f"Brand: {car2.brand}  Color: {car2.color}")
'''
# Constructor
'''
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print("Engine Started.")

    def display_info(self):
        print(f"Brand: {self.brand}  Color: {self.color}")

car1 = Car("Toyota", "Red")
car1.display_info()
car2 = Car("Honda", "White")
car2.display_info()
'''

# Python Scope
'''
Local       Global       Enclosing         Built-in
'''
x = 10 # Global

def outer_function():
    y = 20 # Enclosing

    def inner_function():
        z = 30 # local
        print("Inner Function")
        print("X is: ", x)
        print("Y is: ", y)
        print("Z is: ", z)
    
    print("Local z: ", z)
    inner_function()

outer_function()
print("Global x: ", x)
# print("Enclosing y: ", y)