# LEVEL 1
# python --version
# Python 3.13.0 was Installed On My System

#Arithmatic Operations

from math import sqrt


print(3 + 4)   # For addition of two integers

print(3 - 4)   # For subtraction of two integers

print(3 * 4)   # For multiple of the numbers

print(3 / 4)   # For division of the numbers

print(3 **4)  # For to the power of the numbers

print(3 % 4)   # For remandar or modulus of the intergers 

print(3 //4) # For floor division operator

print("\n") # To give space 

# The strings
print("Umar") # My First Name in Python String

print("Haruna Abdurrahman") # My Family Name/Surname and Middle Name in Python String

print("Nigeria") # My Country in Python Strings

print("I'm Really Enjoying 30 Days of Python in ArewaDs Acadamy")

print("\n") # To give space 

# Checking data types

print(type(10))    # It will Return It will Return Integer Number

print(type(9.8))   # It will Return Floating Point Number

print(type(3.14))     # It will Return Floating Point Number

print(type(['Asabeneh', 'Python', 'Finland']))   # It will Return Python List

print(type('Umar'))          # It will Return Python String

print(type("Haruna Abdurrahman"))          # It will Return Python String

print(type('Nigeria'))          # It will Return Python String

print("\n") # To give space 

# LEVEL 3

# Numbers
int_number = 50
float_number = 3.142
complex_number = 2 + 3j  

# String
string_example = "Hello, Amigos!"

# Boolean
boolean_exp = True

# List
sn = [1, 2, 3, 4, 5]

# Tuple
percent = (10, 20, 30)

# Set
number_set = {1, 2, 3, 4, 5}

# Dictionary
bio_data = {
    "name": "Umar",
    "year": 2024,
    "city": "Kano"
}

print("Integer:", int_number)
print("Float:", float_number)
print("Complex:", complex_number)
print("String:", string_example)
print("Boolean:", boolean_exp)
print("List:", sn)
print("Tuple:", percent)
print("Set:", number_set)
print("Dictionary:", bio_data)

print("\n") # To give space 

# The formula for Euclidean distance between two points (2, 3) and (10, 8)
# Distance = sqrt((x2 - x1)^2 + (y2 - y1)^)
# In Our Case we need math library and define our data
# x1 = 2 , x2 = 10 , and y1 = 3 , y2 = 8

x1 ,x2, y1 ,y2 = 2 , 10 ,3 ,8

distance = sqrt( ( (x2 - x1)**2) + ((y2 - y1)**2) )

print("The Euclidean Distance between Point(2, 3) and Point(10, 8) is : ", distance)

print("\n") # To give space 
