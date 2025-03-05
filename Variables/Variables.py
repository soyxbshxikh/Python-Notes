# What is a variable? : A variable is a container for a storing value, which can be of various types
# such as numbers, strings, lists etc.

# Create a varible
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type 
# It can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Join all output +
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)