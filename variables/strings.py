name = "Dhananjay"
name_2 = "Ingole"

name_3 = '''he 
is a Multitalented person'''

name_4 = """he
is a Handsome Boy""" 

print(name, name_2, name_3, name_4)

# 3 characters of string
# -> strings are immutable
# -> indexing and slicing
# -> Iterable

first_name = "Dhananjay"
last_name = "Ingole"
print(first_name + last_name) # concatenation of strings

print(len(first_name)) # length of string

print(first_name[0]) # indexing

# in slicing it includes [start:stop:step]
print(first_name[0:4:1]) # slicing

for char in first_name:
    print(char) # iterating through string

# string methods
number = '10'
print(number * 5) # prints 1010101010
# print(number ** 5) # error bcz str does not support exponentiation

print(number.isdigit()) # checks if all characters are digits
print(first_name.isalpha()) # checks if all characters are alphabets