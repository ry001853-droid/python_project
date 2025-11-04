
####################################### 7th practical #########################################################
# a program to create a dictionary and perform various operations like adding, updating, and deleting items

# Creating a dictionary

my_dict = {
"name": "Alice",
"age": 25,
"city": "Mumbai"
}

print("Original dictionary:", my_dict)

# Adding an item
my_dict["email"] = "alice@example.com"
print("After adding email:", my_dict)

# Updating an item
my_dict["age"] = 26
print("After updating age:", my_dict)

# Deleting an item using del
del my_dict["city"]
print("After deleting city:", my_dict)

# Deleting an item using pop (also shows the removed value)
removed_value = my_dict.pop("email")
print("Removed value using pop:", removed_value)
print("Dictionary after pop operation:", my_dict)

# Clearing all items from the dictionary
my_dict.clear()
print("After clearing dictionary:", my_dict)

#########################################################################3

# 2. Implement a program to use dictionary methods such as keys(), values(), items(), and get().

# Sample dictionary

student = {
"name": "Raj",
"age": 21,
"course": "Computer Science",
"university": "Mumbai University"
}

# Using keys() method
print("Keys in the dictionary:")
for key in student.keys():
 print(key)

# Using values() method
print("\nValues in the dictionary:")
for value in student.values():
 print(value)

# Using items() method (returns key-value pairs)
print("\nKey-value pairs in the dictionary:")
for key, value in student.items():
 print(f"{key}: {value}")

# Using get() method to safely access values
print("\nUsing get() method:")
print("Name:", student.get("name"))
print("Grade:", student.get("grade", "N/A"))

###################################################################

# Demonstrate the use of for loop to iterate through dictionary items and perform operations on them.

# Sample dictionary representing items and their prices
products = {
"apple": 50,
"banana": 20,
"cherry": 75,
"dates": 100
}

# Iterate through dictionary items and apply discount
discount_percentage = 10
print("Product prices after applying discount:")

for product, price in products.items():
  discounted_price = price - (price * discount_percentage / 100)
print(f"{product.title()}: Original price = {price}, Discounted price = {discounted_price :. 2f}")




############################################ 8th practical ################################################
# write a program to open,read, write and close text files using both traditional and 'with' statement methods

# Traditional method for file handling

# Writing to a file
file = open("example_traditional.txt", "w")
file.write("Hello, this is the traditional way of handling files. \n")
file.write("We manually open and close the file.")
file.close()

# Reading from a file
file = open("example_traditional.txt", "r")
content = file.read()
print("Content read using traditional method:")
print(content)
file.close()

# Using 'with' statement for file handling
# Writing to a file
with open("example_with.txt", "w") as file:
 file.write("Hello, this is the 'with' statement method. \n")
 file.write("File is automatically closed after this block.")

# Reading from a file
with open("example_with.txt", "r") as file:
 content = file.read()
 print("\nContent read using 'with' statement:")
 print(content)

####################################################################3

# Implement a program to work with binary files, including reading and writing binary data.

# Writing binary data to a file
data = bytearray([10, 20, 30, 40, 50])

with open("binaryfile.bin", "wb") as binary_file:
 binary_file.write(data)
print("Binary data written to file.")

# Reading binary data from the file
with open("binaryfile.bin", "rb") as binary_file:
 content = binary_file.read()
print("Binary data read from file:", list(content))

####################################################################

# Demonstrate the use of Pickle module for serializing and deserializing objects.

import pickle

# Sample data: a dictionary
data = {
 "name": "John",
 "age": 30,
 "courses": ["Math", "Science", "History"]
}

# Serialization: converting the object to a byte stream and saving to a file
with open("data.pkl", "wb") as file:
 pickle.dump(data, file)
 print("Data has been pickled and saved to 'data.pkl'.")

# Deserialization: loading the object back from the file
with open("data.pkl", "rb") as file:
 loaded_data = pickle.load(file)
print("Data has been unpickled from 'data.pkl':")
print(loaded_data)

