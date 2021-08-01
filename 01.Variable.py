# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry

# To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)  # Python is awesome

# You can also use the + character to add a variable to another variable:
x = "Python is "
y = "awesome"
z = x + y
print(z)  # Python is awesome

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)  # 15

# ariables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# you can create a variable name same as global variable & if you want to use global variable
# global x