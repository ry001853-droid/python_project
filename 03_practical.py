# write program using if-else and if-elif-else

# use of if-else
a = 15

if a % 2 == 0:
   print(a, "is an even number.")
else:
   print(a, "is an odd number.")

# use of if-elif-else 
age = 25

if age < 13:
   print("Child")   
elif age < 20:
   print("Teenager")        
elif age < 60:
   print("Adult")
else:
   print("Senior Citizen")

######################################################

# implement a program using while and for loops, including nested

# while loop 
print("while loop: print numbers from 1 to 9")
count = 1
while count <= 9: 
   print(count, end="")
   count += 1
print("\n")     

# # For loop
print ("For loop: print elements in a list")
fruits = ("grapes", "guava", "gooseberry")
for fruit in fruits:
   print(fruit)
print()

# # Nested loop
print("Nested loops: Print a 3x3 multiplication table")
for i in range(1, 4):
    for j in range(1, 4):
       print(i*j, end="\t")
       print()

####################################################

# Creating a program to demonstrate use of break, continue, pass, assrt and return

# Pass statement 
print("using pass:")
for num in range(1, 7):
    if num == 3:
        pass  
    print(num, end=" ")
print("\n")

# Assert statement 
print("Using assert:")
def check_positive(number):
    assert number > 0, "Number must be positive"
    return f"{number} is positive"

print(check_positive(10)) # example 1


print("Using assert:")
def check_negative(number):
    assert number < 0, "Number must be positive"
    return f"{number} is positive"

print(check_negative(-3)) # example 2

# Return statement
print("Using return:")
def square(num):
    return num * num

result = square(3)
print("square of 3 is", result)

   


