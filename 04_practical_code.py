# Creating and manipulating arrays including indexing and slicing

import array

# # Creating an array of integers
arr = array.array('i', [10, 20, 30, 40, 50])

# Accessing elements using indexing
print("Element at index 2:", arr[2])  # Output: 30
print("Element at index 0:", arr[0])  # Output: 50

# # Modifying an element
# arr[1] = 25
print("Modified array:", arr)  

# Slicing the array
slice_arr = arr[1:3]
print("Sliced array (index 1 to 2):", slice_arr)

# # slicing with step
slice_step = arr[::3]
print("Sliced array with step 3:", slice_step)

# # Lenght of array
print("Length of array:", len(arr))

################################################

# This program demonstrates basic array operations and mathematical operations using Numpy

import numpy as np

# Creating a numpy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([11, 22, 33, 44, 55])

# Basic array operations
print("Array 1:", arr1)
print("Array 2:", arr2)

# Array addition 
arr_sum = arr1 + arr2
print("Array Addition:", arr_sum)

# Array subtraction
arr_sub = arr2 - arr1
print("Array Subtraction:", arr_sub)

# Element-wise multiplication
mul = arr1 * arr2
print("Element-wise Multiplication:", mul)

# Element-wise division
div = arr2 / arr1
print("Element-wise Division:", div)

# Mathematical functions in array
print("Mean of arr1:", np.mean(arr1))
print("Sum of arr2:", np.sum(arr2))
print("Standard Deviation of arr1:", np.std(arr1))

# Array slicing 
slice_arr = arr2[1:4]
print("sliced array (index 1 to 3) from arr1:", slice_arr)

#################################################

# Demonstrating aliasing, basic slicing, advanced indexing and exploring dimensions and attributes of Numpy arrays

import numpy as np

# Creating a numpy array
arr = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# Aliasing - both variables refering to same array object
alias_arr = arr
alias_arr[0, 0] = 888

print ("original array after modifying alias_arr:")
print(arr)

# Basic slicing - selecting a subarray
basic_slice = arr[1:, 1:]
print("\nBasic Slicing (row 1 to end, column 1 to end):")
print(basic_slice)

# Advanced indexing - selecting specific elements
adv_index = arr[[0, 2], [1, 2]]
print("\nAdvanced Indexing (elements at (0,1) and (2,2)):")
print(adv_index)

# Dimensions and Attributes
print("\nArray Dimensions (ndim):", arr.ndim)
print("Array Shape (rows, columns):", arr.shape)
print("Array Size (total elements):", arr.size)
print("Array Data type:", arr.dtype)
