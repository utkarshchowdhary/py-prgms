"""
// (Integer DIVISION) Divides and rounds down to the nearest integer
"""
# An operation involving an int and a float always produces a float
# when we convert a float to an int the part of the number after the decimal point is cut off

# print(5/0) ZeroDivisionError: division by zero

# String is a data type for immutable ordered sequences of characters
# You can define a string with either double quotes " or single quotes '

# You can also include a \ in your string to be able to include quotes in your string
# You can use multiplication operator to repeat the string as many times you multiply it

# There are different methods depending upon the type of data you are working with.
# methods are functions that belong to an object
## String methods
# .title() method on string capitalized first letter of each word
# .islower() checks if all the characters in a string are lowercase
# .isupper() checks if all the characters in a string are uppercase
# .isalpha() returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.

# count() function in an inbuilt function in python programming language that returns the number of occurrences
# of a substring in the given string.
# string.count(substring, start=…, end=…)

# string.replace(old, new, count)

# The startswith() method returns True if a string starts with the specified prefix(string).
# If not, it returns False.
# The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.

# str.format() is one of the string formatting methods which allows multiple substitutions and value formatting.
# Formatters work by putting in one or more replacement fields and placeholders defined by a pair of curly
# braces {} into a string and calling the str.format(). The value we wish to put into the placeholders and
# concatenate with the string passed as parameters into the format function.
"""
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))
output:- Maria loves math and statistics
"""
# split() method returns a list of strings after breaking the given string by the specified separator
""" str.split(separator, maxsplit) """
# maxsplit: It is a number, which tells us to split the string into maximum of provided number of times

# in evaluates if object on left side is included in object on right side
# not in evaluates if object on left side is not included in object on right side
"""
mutability : wheather an object can change its values after it has been created
"""
## List functions
# len() returns how many elements are in a list
# max() returns the greatest element of the list
# min() returns the smallest element in a list
# sorted() returns a copy of a list in order from smallest to largest
# sum() returns the sum of the elements in a list, and
# pop() is a list method that removes the last element from a list and returns it
## join method
# Join is a string method that takes a list of
# strings as an argument, and returns a string consisting of the list elements joined by a separator string.
# name = "-".join(["García", "O'Kelly"])
# output: García-O'Kelly

## append method
# adds an element to the end of a list
# .append()

## Tuples
# A tuple is another useful container. It's a data type for immutable ordered sequences of elements.
# The parentheses are optional when making tuples

# You can use tuple unpacking to assign information from a tuple into multiple variables
# without having to access them one by one

## SET
# A set is a data type for mutable unordered collections of unique elements.
# One application of a set is to quickly remove duplicates from a list.
# Sets unlike lists are unordered so it can't be indexed and sliced like list
"""
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)
output: {1, 2, 3, 6}
"""
# pop() method removes elements from set.Although, when you pop an element from a set,
# a random element is removed
"""
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
"""

## DICTIONARY
# A data type for mutable objects that store mappings of unique keys to values
# A string or tuple can be used as the key of a dictionary
"""
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary

print("carbon" in elements) #True
print(elements.get("dilithium")) #None
"""

## Identity Operators
# is evaluates if both sides have the same identity
# is not evaluates if both sides have different identities

## Compound Data Structures
# We can include containers in other containers to create compound data structures.
# For example, this dictionary maps keys to values that are also dictionaries!
"""
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}


"""
# We can access elements in this nested dictionary like this.
"""
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]
"""
# You can also add a new key to the element dictionary.
"""
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)
"""

# range() is a built-in function used to create an iterable sequence of numbers.
# range(start=0, stop, step=1)
# The 'start' argument is the first number of the sequence. If unspecified, 'start' defaults to 0
# The 'stop' argument is 1 more than the last number of the sequence.
# The 'step' argument is the difference between each number in the sequence.
# If unspecified, 'step' defaults to 1.
# Modifying a list is a bit more involved, and requires the use of the range() function.

"""
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()
"""
# break terminates a loop
# continue skips one iteration of a loop

# zip returns an iterator that combines multiple iterables into one sequence of tuples.
# Each tuple contains the elements in that position from all the iterables.
"""
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

list(zip(letters, nums))
output: [('a', 1), ('b', 2), ('c', 3)]

using For:
for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
"""
"""
unzip a list into tuples using an asterisk.:
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
:-('a','b','c'),(1,2,3)
"""
"""
enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
"""
# Zip Lists to a Dictionary
"""
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)
"""

## List Comprehensions
# In Python, you can create lists really quickly and concisely with list comprehensions.
"""
eg:
capitalized_cities = [city.title() for city in cities]
squares = [x**2 for x in range(9) if x % 2 == 0]
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
"""

# Defining Functions
"""
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
"""
# The function header always starts with the def keyword, which indicates that this is a function definition
# Default Arguments
"""
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name

"""
# Python doesn't allow functions to modify variables that are outside the function's scope

## Lambda Expressions
# You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name.
# The lambda keyword is used to indicate that this is a lambda expression.
"""
multiply = lambda x, y: x * y
"""
# map() is a higher-order built-in function that takes a function and iterable as inputs,
# and returns an iterator that applies the function to each element of the iterable.
"""
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)
output: [57.0, 58.2, 50.6, 27.2]
"""

# filter() is a higher-order built-in function that takes a function and iterable as inputs and
# returns an iterator with the elements from the iterable for which the function returns True
"""
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

is_short=lambda name: len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)
"""
## Iterators And Generators
# Iterables are objects that can return one of their elements at a time, such as a list
# An iterator is an object that represents a stream of data.
# Generators are a simple way to create iterators using functions
"""
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
# It will produces an iterator that is a stream of numbers from 0 to (x - 1)
"""
# yield allows the function to return values one at a time, and start where it left off each time it’s called.

# Generator Expressions
"""
sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
"""

# eval() function evaluates a string as a line of Python.
"""
result = eval(input("Enter an expression: ")) ## 2 * 3
print(result) ## 6
"""
## Try Statement
# try: This is the only mandatory clause in a try statement.
# except: If Python runs into an exception while running the try block,
# it will jump to the except block that handles that exception

# finally: Before Python leaves this try statement, it will run the code in this
#         finally block under any conditions, even if it's ending the program

# Specifying Exceptions
# Exception is just the base class for all built-in exceptions
# We can actually specify which error we want to handle in an except block
"""
try:
    # some code
except ValueError:
    # some code
"""
# If we want this handler to address more than one type of exception, we can include a parenthesized tuple
"""
try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code
"""
# if we want to execute different blocks of code depending on the exception, you can have multiple except blocks
"""
try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code
"""
# Accessing Error Messages
"""
try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
"""
# Reading and Writing Files
"""
# Reading a File

f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()
"""
# The open function returns a file object, which is a Python object through which Python
# interacts with the file itself
# read method takes the text contained in a file and puts it into a string
"""
# Writing to a File

f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()
"""
# If the file does not exist, Python will create it for you. If you open an existing file in writing mode,
# any content that it had contained previously will be deleted

# With
# Python provides a special syntax that auto-closes a file for you once you're finished using it.
"""
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.readlines()

# Reading Line by Line    
for line in filedata:
"""

# Importing Local Scripts
# We can actually import Python code from other scripts
# This import statement creates a module object
# Modules are just Python files that contain definitions and statements.
# To access objects from an imported module, you need to use dot notation
# We can add an alias to an imported module
"""
import useful_functions as uf
uf.add([1, 2, 3, 4])
"""
# To import an individual function or class from a module
"""
from module_name import object_name
"""
# To import multiple individual objects from a module:
"""
from module_name import first_object, second_object
"""
# To rename a module:
"""
import module_name as new_name
"""
# To import an object from a module and rename it:
"""
from module_name import object_name as new_name
"""

# Using a main block
# To avoid running executable statements in a script when it's imported as a module in another script,
# include these lines in an if __name__ == "__main__" block

# The assert keyword is used when debugging code.

# The assert keyword lets you test if a condition
# in your code returns True, if not, the program will raise an AssertionError

#### Mutable & Immutable Data Types in Python ####
# Mutable data types can be changed after they are created
# Immutable data types can't be changed after they are created

# Immutable data types are passed into functions as a copy of the original object
# Changes that happen to this copy within the function don't affect the original object

# Mutable data types are passed into functions as a pointer to the original object
# Changes that happen to this pointer within the function change the original object

# Immutable Data types :-    # Mutable Data Types :-
# boolean value              # list
# integer                    # dictionary
# float                      # set
# tuple
# string

##### Jupyter Notebook #####

# Jupyter Notebook is a web application which facilitates creating and sharing documents containing live code

## Installing jupyter notebook
# update pip:
"""
 python -m pip install --upgrade pip
 python -m pip install jupyter
 jupyter notebook
"""
# Code cells can be executed with the shift enter keystroke

# Markdown cells
"""
# Header 1
## Header 2
### Header 3
"""
# Links
"""
[Udacity's home page](https://www.udacity.com)
"""
# Emphasis
"""
Bold text uses two symbols, **aardvark** or __aardvark__
italics text uses two symbols, _gelato_ or *gelato*
"""
# Magic keywords
# Timing code
# You can use the timeit magic command to time how long it takes for a function to run
"""
%timeit fibol(20)
"""
# If you want to time how long it takes for a whole cell to run, you’d use %%timeit

# With the Python kernel, you can turn on the interactive debugger using the magic command %pdb

# Converting notebooks
# Notebooks are just big JSON files with the extension .ipynb
# To convert a notebook to an HTML file, in your terminal use
"""
jupyter nbconvert --to html notebook.ipynb
"""
# Running the slideshow
# To create the slideshow from the notebook file, you'll need to use nbconvert
"""
jupyter nbconvert notebook.ipynb --to slides
"""
# To convert it and immediately see it, use
"""
jupyter nbconvert notebook.ipynb --to slides --post serve
"""

