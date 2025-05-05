<h1 align="center">Python Notes </h1>

### 1. What is Python?

- Python is a high-level, interpreted programming language.
- Python was created by Guido van Rossum (in 1991).
- Python files have a .py extension.
- Python emphasizes code readability with its notable use of significant whitespace.

---

### 2. Which software is used for Python?

- IDLE (Python's built-in IDE)
- Visual Studio Code
- PyCharm
- Jupyter Notebook
- Spyder

---

### 3. How to run Python code?

- Open terminal/command prompt and type `python filename.py`
- Use an IDE with a run button
- For interactive mode, type `python` in terminal

---

### 4. Basic structure of Python code

```python
# This is a comment
print("Hello, World!")

# Variables
name = "Python"
age = 32

# Basic function
def greet(name):
    return f"Hello, {name}!"

# Calling a function
message = greet(name)
print(message)
```

---
## 5. Variables and Data Types

```python
# Integer
x = 5

# Float
y = 3.14

# String
name = "Python"

# Boolean
is_true = True
is_false = False

# List: Ordered | Mutable | Allows duplicates
my_list = [1, 2, 3, 4, 5]

# Tuple: Ordered | Immutable | Allows duplicates
my_tuple = (1, 2, 3, 4, 5)

# Dict : Changable | Ordered | no duplicate | {key : value} pair 
my_dict = {"name": "Python", "age": 32}

# Set: Unordered | Mutable | No duplicates
my_set = {1, 2, 3, 4, 5}
```

---
## 6. Operators

```python
# Arithmetic Operators
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a % b)  # Modulus: 1
print(a ** b)  # Exponentiation: 1000
print(a // b)  # Floor division: 3

# Comparison Operators
print(a == b)  # Equal: False
print(a != b)  # Not equal: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal: True
print(a <= b)  # Less than or equal: False

# Logical Operators
x = True
y = False
print(x and y)  # Logical AND: False
print(x or y)   # Logical OR: True
print(not x)    # Logical NOT: False

# Assignment Operators
c = 5
c += 3  # c = c + 3
print(c)  # 8
c -= 2  # c = c - 2
print(c)  # 6
```

---
## 7. Control Flow

### 1) If-Else Statement
```python
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are an adult.")
```

### 2) For Loop
```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop using range
for i in range(5):  # 0 to 4
    print(i)

# Loop with range start and end
for i in range(2, 5):  # 2 to 4
    print(i)
    
# Loop with step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### 3) While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1

# Break statement
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break

# Continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Prints odd numbers
```

---
## 8. Functions

```python
# Basic function
def greet():
    print("Hello, World!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Function with default parameter
def greet_with_time(name, time="morning"):
    print(f"Good {time}, {name}!")

# Function with return value
def add(a, b):
    return a + b

# Calling functions
greet()
greet_person("Alice")
greet_with_time("Bob")
greet_with_time("Carol", "evening")
result = add(5, 3)
print(result)  # 8

# Lambda function (anonymous function)
square = lambda x: x ** 2
print(square(4))  # 16
```

---
## 9. Lists

```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # apple
print(fruits[-1])  # cherry

# Changing elements
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append("orange")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'orange']

fruits.insert(2, "grape")
print(fruits)  # ['apple', 'blueberry', 'grape', 'cherry', 'orange']

# Removing elements
fruits.remove("blueberry")
print(fruits)  # ['apple', 'grape', 'cherry', 'orange']

popped_fruit = fruits.pop()
print(popped_fruit)  # orange
print(fruits)  # ['apple', 'grape', 'cherry']

# List operations
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
combined = nums1 + nums2
print(combined)  # [1, 2, 3, 4, 5, 6]

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

numbers.reverse()
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

print(len(numbers))  # 7
print(numbers.count(1))  # 2
```

---
## 10. Tuples

```python
# Creating a tuple
coordinates = (10, 20)

# Accessing elements
print(coordinates[0])  # 10
print(coordinates[1])  # 20

# Tuples are immutable
# This will cause an error:
# coordinates[0] = 15

# Unpacking a tuple
x, y = coordinates
print(x)  # 10
print(y)  # 20

# Tuple methods
numbers = (3, 1, 4, 1, 5, 9, 2)
print(numbers.count(1))  # 2
print(numbers.index(5))  # 4

# Converting list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3)
```

---
## 11. Dictionaries

```python
# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing elements
print(person["name"])  # John

# Alternative access method (safer)
print(person.get("age"))  # 30
print(person.get("country", "Unknown"))  # Unknown (default value)

# Changing values
person["age"] = 31
print(person)  # {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding new key-value pairs
person["job"] = "Developer"
print(person)  # {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Developer'}

# Removing key-value pairs
removed_value = person.pop("city")
print(removed_value)  # New York
print(person)  # {'name': 'John', 'age': 31, 'job': 'Developer'}

# Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

print(list(keys))  # ['name', 'age', 'job']
print(list(values))  # ['John', 31, 'Developer']
print(list(items))  # [('name', 'John'), ('age', 31), ('job', 'Developer')]
```

---
## 12. Sets

```python
# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding elements
fruits.add("orange")
print(fruits)  # {'cherry', 'apple', 'orange', 'banana'} (order may vary)

# Removing elements
fruits.remove("banana")
print(fruits)  # {'cherry', 'apple', 'orange'}

# Safe removal
fruits.discard("kiwi")  # No error if element doesn't exist

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.union(set2))  # Same as above

# Intersection
print(set1 & set2)  # {4, 5}
print(set1.intersection(set2))  # Same as above

# Difference
print(set1 - set2)  # {1, 2, 3}
print(set1.difference(set2))  # Same as above

# Symmetric difference
print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))  # Same as above
```

---
## 13. String Operations

```python
# String creation
single_quoted = 'Hello'
double_quoted = "World"
triple_quoted = '''This is a
multi-line string'''

# String concatenation
greeting = single_quoted + " " + double_quoted
print(greeting)  # Hello World

# String repetition
repeated = "Ha" * 3
print(repeated)  # HaHaHa

# String methods
text = "   Python Programming   "
print(text.strip())  # "Python Programming"
print(text.lower())  # "   python programming   "
print(text.upper())  # "   PYTHON PROGRAMMING   "
print(text.replace("P", "J"))  # "   Jython Jrogramming   "

# String splitting
sentence = "Python is awesome"
words = sentence.split()
print(words)  # ['Python', 'is', 'awesome']

csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

# String joining
joined = ", ".join(fruits)
print(joined)  # "apple, banana, cherry"

# String formatting
name = "Alice"
age = 25
# Old style
old_format = "My name is %s and I am %d years old" % (name, age)
# Format method
new_format = "My name is {} and I am {} years old".format(name, age)
# F-strings (Python 3.6+)
f_string = f"My name is {name} and I am {age} years old"

print(f_string)  # My name is Alice and I am 25 years old
```

---
## 14. File Handling

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nThis line is appended.")

# Reading and writing binary files
with open("binary_file.bin", "wb") as file:
    file.write(b"\x48\x65\x6C\x6C\x6F")  # "Hello" in hex

with open("binary_file.bin", "rb") as file:
    binary_data = file.read()
    print(binary_data)  # b'Hello'
```

---
## 15. Exception Handling

```python
# Basic try-except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple except blocks
try:
    number = int("abc")
except ValueError:
    print("Invalid conversion!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Generic exception catch
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except Exception as e:
    print(f"An error occurred: {e}")

# try-except-else-finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")  # Executes if no exception
finally:
    print("This always executes!")  # Always executes

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is too high")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(e)  # Age cannot be negative
```

---
## 16. Object-Oriented Programming

```python
# Creating a class
class Person:
    # Class attribute
    species = "Homo sapiens"
    
    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def greet(self):
        return f"Hello, my name is {self.name}"
    
    # Instance method with parameters
    def celebrate_birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old"

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing attributes
print(person1.name)  # Alice
print(person1.species)  # Homo sapiens

# Calling methods
print(person1.greet())  # Hello, my name is Alice
print(person1.celebrate_birthday())  # Alice is now 26 years old

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call parent constructor
        super().__init__(name, age)
        self.student_id = student_id
    
    # Override method
    def greet(self):
        return f"Hi, I'm {self.name}, a student"
    
    # New method
    def study(self, subject):
        return f"{self.name} is studying {subject}"

# Creating student object
student1 = Student("Eve", 20, "S12345")
print(student1.greet())  # Hi, I'm Eve, a student
print(student1.study("Python"))  # Eve is studying Python
print(student1.celebrate_birthday())  # Eve is now 21 years old
```

---