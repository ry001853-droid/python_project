############################################# 1st practical @#################################################
a <- 12
b <- 28

sum <- a + b
difference <- a - b
product <- a * b
quotient <- a / b
powerab <- a ^ b

is_greater <- a > b
is_equal <- a == b

cat("The sum of a and b is: ", sum, "\n")
cat("The difference of a and b is: ", difference, "\n")
cat("The product of a and b is: ", product, "\n")
cat("The division of a and b is ", quotient, "\n")
cat("The power of a and b is: ", powerab, "\n")
cat("a > b ?: ", is_greater, "\n")
cat("a = b ?: ", is_equal, "\n")

################################################ 2nd practical ################################################
############################################## 2nd practical ################################################
############################################## 2nd practical ################################################
# 1. VECTORS
# Creating Vectors
vector_a <- c(1, 2, 3, 4, 5) # Numeric Vector
vector_b <- c("Apple", "Banana", "Mango") # Character Vector
vector_c <- c(TRUE, FALSE, TRUE, FALSE) #Logical Vector

# Printing Vectors Using Cat
cat("Numeric Vector:\n", vector_a, "\n")
cat("Character Vector:\n", vector_b, "\n")
cat("Logical Vector:\n", vector_c, "\n\n")


# 2. MATRIX
# Creating A Matrix
matrix_1 <- matrix(c(1,3,6,4), nrow = 2, ncol = 2, byrow = TRUE) #Filling rows first
cat("Matrix: \n")
print(matrix_1) # Using Print Here Because 'cat' Cannot Display A Matrix Directly

# Accessing Elements In A Matrix
element <- matrix_1[1,2] # Element In 1st Row And 2nd Column
cat("Element at row 1, column 2: ", element, "\n\n")

# 3. ARRAYS
# Creating A 3D Array
array_1 <- array(1:24, dim = c(3, 4, 2)) # 3 Rows, 4 Column, 2 Layers
cat("3D Array:\n")
print(array_1) # Using Print For Array Visualization

# Accessing An Element In The Array
array_element <- array_1[2,3,1] # Element At 2nd Row, 3rd Column, 1st Layer
cat("Element at row 2, column 3, layer 1:", array_element, "\n\n")

# 4. LISTS
# Creating A List
my_list <- list(Name = 'Harsh', Age = 18, Scores = c(90, 88, 85))
cat("List:\n")
print(my_list) # Using Print For Better List Visualization

cat("Name from the list:", my_list$Name, "\n")
cat("Scores from the list: \n", my_list$Scores, "\n\n")
cat("Age from the list: \n", my_list$Age, "\n\n")
    
# 5. DATA FRAMES
# Creating A Data Frame
students <- data.frame(
  Name = c("Krish", "Riddhi", "Rishi"),
  Age =c(18, 17, 17),
  Marks = c(85, 90, 88)
)
      
cat("Data Frame:\n")
print(students) #Using Print For Better Data Frame Visualization
      
# Accessing Elements In A Data Frame
cat("Names of students:\n", students$Name, "\n")
cat("First row of the data frame: \n")
print(students[1, ]) # Printing the first row
cat("Marks of Riddhi:", students [students$Name == "Riddhi", "Marks"], "\n")

