"""This program demonstrates comments and docstrings in Python."""

def add(a, b):
    """Return the sum of two numbers."""
    # Add the numbers and store the result
    result = a + b
    return result  # Return the result

# Main program
x = 5  # First number
y = 3  # Second number
print("Sum =", add(x, y))  # Display the sum

print("Hello world")

########################################################## 9th practical ################################################
########################################################## 9th practical ################################################
########################################################## 9th practical ################################################

# Write a program to demonstrate sequence and special characters in regular expressions.

import re

# Sample text
text = "My phone number is 123-456-7890 and my email is test.user@example.com."

# Sequence: \d matches any digit, \w matches any word character (letter, digit, or underscore)
# Special characters: \s matches whitespace, . matches any character except newline

# Find all sequences of digits
digits = re.findall(r"\d+", text)
print("Digits found:", digits)

# Find email pattern using special characters
email_pattern = r"\w+[\.\w]*@\w+\.\w+"
emails = re.findall(email_pattern, text)
print("Emails found:", emails)

# Find phone number pattern (sequence of digits with dashes)
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)

# Use special characters: ^ matches start of string, $ matches end of string
start_check = re.match(r"^My", text)
end_check = re.search(r"com\.$", text)

print("Starts with 'My':", bool(start_check))
print("Ends with 'com.':", bool(end_check))

########################################################################################

# Implement a program to use regular expressions for searching and extracting data from text files.

import re

# Create a sample text file for demonstration
sample_text = """John's email is john. doe@example.com and his phone number is 123-456-7890.
Contact Jane at jane_smith123@mail.net or call 987-654-3210."""

with open("sample_data.txt", "w") as file:
 file.write(sample_text)

# Define regex patterns for email and phone number
email_pattern = r"\b[\w.-]+@[\w .-]+\.\w+\b"
phone_pattern = r"\b\d{3}-\d{3}-\d{4}\b"

# Open and read the file, then search for patterns
with open("sample_data.txt", "r") as file:
 content = file.read()

emails = re.findall(email_pattern, content)
phones = re.findall(phone_pattern, content)

print("Emails found in file:")
for email in emails:
 print(email)

print("\nPhone numbers found in file:")
for phone in phones:
 print(phone)

#############################################################################

#   

import re

# Sample HTML content for demonstration
html_content = """
<html>
<head><title>Sample Page</title></head>
<body>
<h1>Welcome to My Website</h1>
<p class="intro">This is a sample HTML file .< /p>
<a href="https://example.com/page1">Page 1</a>
<a href="https://example.com/page2">Page 2</a>
<p>Contact us at contact@example.com</p>
</body>
</html>
"""

# Extract the title of the page
title_match = re.search(r"<title>(.*?)</title>", html_content, re.IGNORECASE)
title = title_match.group(1) if title_match else "No title found"

# Extract all links (href attribute values)
links = re.findall(r'href="(.*?)"', html_content)

# Extract all paragraph texts
paragraphs = re.findall(r"<p.*?>(.*?)</p>", html_content, re.DOTALL)

# Extract email addresses
emails = re.findall(r"[a-zA-Z0-9._ %+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html_content)

print("Page Title:", title)
print("\nLinks found:")
for link in links:
 print(link)

print("\nParagraphs found:")
for para in paragraphs:
 print(para.strip())

print("\nEmails found:")
for email in emails:
 print(email)
