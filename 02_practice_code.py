# 1st practical

"""This program demonstrates comments and docstrings in python"""

def add(a, b):
    """ this adds two numbers"""
    # result
    result = a + b
    return result # This returns the result 

# Main program
x = 60
y = 7
print("sum =", add(x, y))


print("Hello world")

# 2nd practical

# Demonstrating the different types of data types in python

# Integer
Age = 19
print("Integer :", Age)

# Float 
Height = 5.7
print("Float :", Height)

# String
Name = "zoro"
print("String :", Name)

# List
Marks = [99, 99 , 99]
print("List :", Marks)

# Tuple 
Radii = (6.6, 6.7, 6.8)
print("Tuple :", Radii)

# Dictionaries 
Profile_info = { "Name ": "zoro", "Age ": 19, "Height ": 5.7, "Marks": Marks}
print("Dictionaries :", Profile_info)

# Set
Swords = {"Wado ichimonji", "Sandai Kitetsu", "Yubashiri"}
print("Set :", Swords)

# This program takes input from user and displays the output
Name = input("Enter your name :")
Age = int(input("Enter your age :"))

# Displys the output
print("Hello", Name)
print("You are", Age ,"years old")



