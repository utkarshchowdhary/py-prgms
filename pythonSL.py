import math
import random
import datetime
import os
from time import time, sleep

print(math.factorial(4))  # Return x factorial as an integer
print(math.ceil(10.4))  # Return the smallest integer greater than or equal to x
print(math.floor(10.4))  # Return the largest integer less than or equal to x
print(math.gcd(4, 6))  # Return the greatest common divisor of the integers a and b
print(math.isqrt(36))  # Return the integer square root of the nonnegative integer
print(math.pow(2, 3))  # Return x raised to the power y
print(math.exp(3))  # Return e raised power x
print(math.pi)  # π

print(
    random.random()
)  # Return the next random floating point number in the range 0.0 <= x < 1.0
print(random.randint(2, 10))  # Returns an integer number from the specified range
print(random.uniform(2.5, 10))  # Random float between two intervals:  2.5 <= x < 10.0
print(
    random.choice([1, 2, 3, 4, 5])
)  # Return a random element from the non-empty sequence
print(
    random.sample([1, 2, 3, 4, 5], 3)
)  # Return a k length list of unique elements chosen from the population sequence or set

print(datetime.datetime.now())  # Get Current Date and Time
print(datetime.date.today())  # Get Current Date

print(
    os.name
)  # This function gives the name of the operating system dependent module imported
print(os.getcwd())  # Returns the Current Working Directory(CWD)

print(time())  # The time() function returns the number of seconds passed since epoch

# The sleep() function suspends (delays) execution of the current thread for the given number of seconds
sleep(2)
