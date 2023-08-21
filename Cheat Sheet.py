# Variables and Data Types
name = "Justin"  # String variable
age = 24  # Integer variable
height = 5.11  # Float variable
is_student = False  # Boolean variable

# Arithmetic Operators
result = age + 5  # Addition
result = age - 3  # Subtraction
result = age * 2  # Multiplication
result = age / 3  # Division
result = age % 2  # Modulo

# Conditional Statements
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Lists
my_list = [1, 2, 3, 4, 5]  # Creating a list
list_len = len(my_list)  # Getting the length of the list
list_append = my_list.append(6)  # Adding an element to the end
list_extend = my_list.extend([7, 8])  # Adding multiple elements to the end
list_insert = my_list.insert(2, 10)  # Inserting an element at a specific index
list_pop = my_list.pop()  # Removing and returning the last element
list_remove = my_list.remove(3)  # Removing the first occurrence of an element
list_index = my_list.index(4)  # Finding the index of an element
list_count = my_list.count(5)  # Counting occurrences of an element
list_sort = my_list.sort()  # Sorting the list in-place
list_reverse = my_list.reverse()  # Reversing the list in-place

# Loops
for item in my_list:  # Looping through each item in the list
    print(item)  # Printing the current item

for index, item in enumerate(my_list):  # Looping with index using enumerate
    print(f"Index: {index}, Item: {item}")

while condition:  # Executing a block of code while a condition is true
    # Code block
    condition = False  # Ensure the loop eventually terminates

# Range Loop
for i in range(5):  # Looping through a range of numbers (0 to 4)
    print(i)

for i in range(2, 10, 2):  # Looping through a range with start, end, and step
    print(i)


# Functions
def greet(name):  # Defining a function
    return f"Hello, {name}!"


result = greet("Alice")  # Calling the function with an argument

# Strings
my_string = "Hello, World!"
string_length = len(my_string)  # Getting the length of the string
substring = my_string[7:12]  # Extracting a substring
string_upper = my_string.upper()  # Converting the string to uppercase
string_lower = my_string.lower()  # Converting the string to lowercase
string_replace = my_string.replace("World", "Python")  # Replacing a substring
string_strip = my_string.strip()  # Removing leading and trailing whitespace
string_split = my_string.split(",")  # Splitting the string into a list of substrings
string_join = "-".join(["Hello", "Python"])  # Joining a list of strings into one

# Modules
import math  # Importing a module

math_sqrt = math.sqrt(25)  # Using a function from the module
from random import randint  # Importing a specific function from a module

random_num = randint(1, 10)  # Using the imported function

# Dictionaries
my_dict = {"key1": "value1", "key2": "value2"}  # Creating a dictionary
dict_get = my_dict.get("key1")  # Getting the value for a key
dict_keys = my_dict.keys()  # Getting the keys of the dictionary
dict_values = my_dict.values()  # Getting the values of the dictionary
dict_items = my_dict.items()  # Getting the key-value pairs of the dictionary
dict_pop = my_dict.pop("key2")  # Removing a key-value pair and returning the value
dict_popitem = my_dict.popitem()  # Removing and returning a random key-value pair
dict_update = my_dict.update(
    {"key3": "value3"}
)  # Updating dictionary with new key-value pairs


# Object-Oriented Principles
class Person:  # Defining a class
    def __init__(self, name, age):  # Constructor method
        self.name = name  # Assigning attributes
        self.age = age

    def greet(self):  # Method within the class
        return f"Hello, my name is {self.name}."


person1 = Person("Alice", 25)  # Creating an instance of the class
person_greeting = person1.greet()  # Calling the method on the instance

# File Handling
with open("example.txt", "r") as file:
    content = file.read()  # Reading content from a file
with open("output.txt", "w") as file:
    file.write("Hello, Python!")  # Writing content to a file

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Error: Division by zero"

# List Comprehensions
squared_numbers = [x**2 for x in range(1, 6)]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

# Virtual Environments
# Create a virtual environment: python -m venv myenv
# Activate the virtual environment: source myenv/bin/activate (Unix) or myenv\Scripts\activate (Windows)
# Deactivate the virtual environment: deactivate

# Packages and Dependencies
# Install packages using pip: pip install package-name
# Create requirements.txt: pip freeze > requirements.txt
# Install packages from requirements.txt: pip install -r requirements.txt

############################################################################################################################################################################

# Intermediate Python
# Advanced Data Structures
# Sets
my_set = {1, 2, 3, 4, 5}  # Creating a set
my_set.add(6)  # Adding an element to the set
my_set.remove(3)  # Removing an element from the set

# Tuples
my_tuple = (1, 2, 3)  # Creating a tuple
element = my_tuple[0]  # Accessing elements

# Dictionaries - Advanced
from collections import defaultdict, OrderedDict

default_dict = defaultdict(int)  # Creating a defaultdict with int as default factory
ordered_dict = OrderedDict()  # Creating an ordered dictionary

# List Comprehensions and Generators
squared_numbers = [x**2 for x in range(1, 6)]  # List comprehension
even_numbers = (x for x in range(1, 11) if x % 2 == 0)  # Generator expression

# File Handling - Advanced
with open("binary_file.bin", "wb") as file:
    data = b"Hello, Binary!"  # Writing binary data to a file
    file.write(data)


# Exception Handling - Advanced
class CustomError(Exception):
    pass


try:
    if something_bad:
        raise CustomError("Something bad happened!")
except CustomError as e:
    print(e)


# Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello(name):
    return f"Hello, {name}!"


# Modules and Packages - Advanced
from mypackage import module  # Importing modules from a package
from mypackage.subpackage import submodule


# Object-Oriented Concepts - Advanced
class Parent:
    def show(self):
        print("Parent class")


class Child(Parent):
    def show(self):
        super().show()  # Calling parent's method using super()
        print("Child class")


# Functional Programming
# First-class functions and higher-order functions
def apply_function(func, x):
    return func(x)


def square(x):
    return x**2


result = apply_function(square, 5)  # Passing function as an argument

# map, filter, and reduce functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
even_numbers = filter(lambda x: x % 2 == 0, numbers)
from functools import reduce

sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Lambda functions
double = lambda x: x * 2

# Concurrency and Threading
import threading


def print_numbers():
    for i in range(1, 6):
        print(i)


def print_letters():
    for letter in "abcde":
        print(letter)


t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t1.start()
t2.start()
t1.join()
t2.join()

# Regular Expressions
import re

pattern = r"\d+"  # Matching digits
matches = re.findall(pattern, "There are 123 apples and 456 bananas.")

# Debugging and Profiling
# Using pdb debugger
import pdb


def calculate(x, y):
    result = x + y
    pdb.set_trace()
    result *= 2
    return result


# Profiling with cProfile
import cProfile

cProfile.run("calculate(10, 20)")

# External Libraries and APIs
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com")
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.text

import pandas as pd
import numpy as np

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
mean_age = np.mean(df["Age"])
