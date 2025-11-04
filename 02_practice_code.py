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


######################################################## 10th practical ######################################
######################################################## 10th practical ######################################
######################################################## 10th practical ######################################

# Write a program to display the current date and time, and format them in different ways.

from datetime import datetime

# Get current date and time
now = datetime.now()

# Default string representation
print("Current date and time:", now)

# Custom formats
print("Formatted date (DD-MM-YYYY):", now.strftime("%d-%m-%Y"))
print("Formatted date (Month day, Year):", now.strftime("%B %d, %Y"))
print("Formatted time (24-hour):", now.strftime("%H:%M:%S"))
print("Formatted time (12-hour with AM/PM):", now.strftime("%I:%M:%S %p"))
print("ISO 8601 format:", now.isoformat())

##################################################################################################

# 2. Implement a program to find and compare dates, and sort a list of dates.

from datetime import datetime

# Sample dates as strings
date_strings = [
"2025-12-25",
"2024-01-01",
"2025-06-15",
"2023-09-27",
"2025-01-01"
]

# Convert strings to datetime objects
dates = [datetime. strptime(date_str, "%Y-%m-%d") for date_str in date_strings]

# Comparing two dates
date1 = dates[0]
date2 = dates[1]

if date1 > date2:
 print(f"{date1.date()} is after {date2.date()}")
elif date1 < date2:
 print(f"{date1.date()} is before {date2.date()}")
else:
 print(f"{date1.date()} is the same as {date2.date()}")

# Sorting the list of dates
sorted_dates = sorted(dates)
print("\nDates sorted in ascending order:")
for date in sorted_dates:
 print(date.strftime("%Y-%m-%d"))


####################################################################################

# 3. Demonstrate the use of calendar module to perform operations such as printing calendars and finding specific dates.

import calendar

# Print the calendar for a specific month and year
year = 2025
month = 9
print(f"Calendar for {calendar.month_name[month]} {year}:")
print(calendar.month(year, month))

# Print the calendar for the whole year
print(f"Calendar for the year {year}:")
print(calendar.calendar(year))

# Find the weekday of a specific date
day = 26
weekday = calendar.weekday(year, month, day)
print(f"Weekday for {year}-{month}-{day} is:", calendar.day_name[weekday])

# Check if a year is a leap year
is_leap = calendar.isleap(year)
print(f"Is {year} a leap year? {is_leap}")

# Get the number of leap years in a range
start_year = 2000
end_year = 2025
leap_years_count = calendar. leapdays(start_year, end_year)
print(f"Number of leap years between {start_year} and {end_year}: {leap_years_count}")



