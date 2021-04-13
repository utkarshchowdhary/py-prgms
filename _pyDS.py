# A string is a sequence of characters we prefer to read data in using strings and
# then parse and convert the data as we need

# we can get any single character in a string using an index specified in square brackets
# you will get a python error (IndexError: string index out of range)
# if you attempt to index beyond the end of a string

# The built-in fun len gives us the length of a string
# len('banana)

# Slicing Strings
# we can also get an continuous section of a string using a colon operator.
# s[0:4]
# The second number is up to but not included

# If we leave off the first number or the last number of the slice, it is assumned to be
# beginning or end of the string resp.

# The in keyword can also be used to check to see if one string is in another string it return True or False

# Python has a number of string functions which are in the string library
# These functions are built-in into every string and we invoke them by appending the fun to the string var
# These functions do not modify the original string, instead they return a new string that has been altered
# eg 'HI THERE'.lower(),'HI THERE'.upper()

# dir() returns a list of attributes of the object it is called upon

# We use find() function to search for a substring within another string it returns the first occurence of the substring
# If it is not found it returns -1

# The rfind() method finds the last occurrence of the specified value

# The replace() fun replaces all occurrences of the search string with the replacement string
# .replace('search-string','replacement-string')

# lstrip() and rstrip() removes whitespace at the left or right of the string
# strip removes whitespaces at both begining and ending

# The startswith() method returns True if a string starts with the specified prefix(string).
# If not, it returns False.

# The endswith() method returns True if a string ends with the specified suffix(string).
# If not, it returns False.


### Files
# To read the contents of the file, we must tell python which file we are going to work with
# and what will will be doing with the file.

# This is done with open() function
# open() returns a "file handle"- a variable used to perform operations on the file

# handle = open(filename,mode) mode should be 'r' if we are planning to read the file and
# 'w' if we are going to write to the file

# If file does not exist it shows FileNotFoundError
# we use "newline" (\n) to indicate when a line ends (newline is still one character)

# A file handle open for read can be treated as a sequence of strings where each line in the file is a string
# in the sequence
# We can use the for statement to iterate through a sequence

# We can read the whole file (newlines and all) into a single string
# inp = fhandle.read()
# The newline is considered "white space" can can be stripped using rstrip()

#### Algorithms
# A set of rules or steps used to solve a problem
#### Data Structures
# A particular way of organizing data in a computer

## List
# A collection allows us to put many values in a single "variable"
# List constants are surrounded by square brackets and the elements in the list are seperated by commas
# A List element can be any Python object- even another list
# You do not have to have same kind of data in a list

# Strings are "immutable"- we cannot change the contents of a string - we must make a new string
# to make any changes

# Lists are "mutable"- we can change an element of a list using the indesx operator
# len() fun takes a list as a parameter ans returns the number of elements in the list

# The range() fun returns a list of numbers that range from zero to one less than the parameter

# We can concatenate(+) lists together
# Lists can be sliced just like strings second number is up to but not including

# We can create an empty list and then add elements using the append method
# The list stays in order and new elements are added at the end of the list
# l = list()
# l.append('something')
# in operator allows you to check if the specified value is in the list
# A list can be sorted using sort method
# l.sort()
# couple of built-in functions you can use with lists len(l),max(l),min(l),sum(l)

# Split breaks a string into parts and produces a list of strings. We can think of these as words.
# We can access a particular word or loop through all the words
# .split(delimiter) - You can specify the separator, default separator is any whitespace.

#### Dictionaries
# dictionaries are like lists except that they use keys instead of numbers to look up values
# They are memory based key value stores
# The dictionary contents are mutable
# Order of dictionaries are not predictable
# some = dict()
# some['key'] = value
# It's an error to reference a key which is not in the dictionary
# we can use the in operator to see if a key is in the dictionary

# The get() method returns the value for the given key, if present in the dictionary.
# If not, then it will return None (if get() is used with only one argument).

# .get('key','default val if key is not found')

# Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries
# in a dictionary, it goes through all the keys in the dictionary

# You can get a list of keys, values, or items(both):-A list of tuples from a dictionary
# list(dict), dict.keys(), dict.values(), dict.items()

# We loop through the key-value pairs in a dictionary using *two* iteration variables
# for k,v in dict.items() :

#### Tuples
# A tuple is an immutable sequence of Python objects - similar to a string

# Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient
# in terms of memory use and performance than lists

# Tuples and Assignment
# We can also put a tuple on the lhs of an assignment stm and it expects a tuple on rhs
# we can even omit the parentheses

# Tuples are Comparable
# The comparison operators work with tuples and other sequences
# If the first item is equal, Python goes on to the next element and so on until it finds one that differs

# We can sort the dictionaries by keys using items() method and sorted() fun
# sorted(dict.items())
# for k,v in sorted(dict.items()) :

# The primary difference between the list sort() function and the sorted() function is that the sort() function
# will modify the list it is called on. The sorted() function will create a new list containing a
# sorted version of the list

# We can sort the dictionaries by value by creating a list obj and storing dictionary key, value pairs
# in the form of tuples in it of order val,key and then use sorted() fun on it
# sorted(l,reverse=True)
