# program to define call function including returning multiple values

# Function to greet a user
def greet(name):
    return f"Hello, {name}!"

# Function to sum and multiply two numbers and return both result
def add_and_multiply(x, y):
    sum_result = x + y
    product_result = x * y
    return sum_result, product_result 

# Calling the greet function 
message = greet ("Zoro")
print(message)

# Calling add_and_multiply function 
sum_val, product_val = add_and_multiply(11, 3)
print("sum:", sum_val)
print("Product:", product_val)

###################################################################################

# Recursive and Anonymous (lambda) functions

# Recursive function to calculate factorial of a number
def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n - 1)
    
print("Factorial of 5:", factorial(5))

# Anonymous lambda function to calculate square of a number
square = lambda x: x * x

print("Square of 6:", square(6))

# Recursive use of lambda to calculate fibonacci number 
fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)

print("Fibonacci number at position 7:", fib(7))

######################################################################

# Program demonstrating various string operations, including formatting, finding characters, and inserting substrings

# Original string
text = "hello, zoro!"

# string formatting using f-string
name = "sanji"
age = 21
formatted_str = f"My name is {name} and I am {age} years old"
print("Formatted String:", formatted_str)

# Finding charaters 
index = text.find("r")
print("Index of 'r' in text:", index)

# Finding substring ocurrence count 
count_o = text.count("o")
print("count of 'o' intext:", count_o)

# Inserting a substring - by slicing and concatenation
insert_pos = 7
substring = "King of hell "
new_text = text[:insert_pos] + substring + text[insert_pos:]
print("After inserting substring:", new_text)

#################################################################################

# Modules of python in program

# Importing the math module for mathematical functions
import math

# Importing specfic function from random module
from random import randint, choice

# Using math module functions
print("Square root of 13:", math.sqrt(13))
print("Value of pi:", math.pi)
print("Cosine of 90 radians:", math.cos(90))

# Using random module function
random_num = randint(1, 100)
print("Random integer:", random_num)

choices = ['Grapes', 'coconut', 'Apple', 'orange']
random_choice = choice(choices)
print("Random choice from list:", random_choice)
