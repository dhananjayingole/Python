# in dictionary, create a new key-value pair if the key does not already exist.
# key must be Always unique.
# dict are unordered, changeable/mutable, and indexed collections.

my_dict = {
    "Name":"dhananjay", "age":22, "city":"Nanded","marks":[90,85,88]
}      
print("Original Dict:",my_dict)

# Adding a new key-value pair
my_dict["country"] = "India"
print("Dict after adding new key-value pair:",my_dict)

# Updating an existing key-value pair
my_dict["age"] = 30 
print("Dict after updating age:",my_dict)

# deleting a key-value pair
del my_dict["city"]
print("Dict after deleting city:",my_dict)

# using pop() method to remove a key-value pair
removed_value = my_dict.pop("marks")
print("Removed marks value:", removed_value)

# using get() method to access value of a key
age = my_dict.get("age")
print("Age using get():", age)

# using keys() method to get all keys
keys = my_dict.keys()
print("Keys in the dict:", keys)

# using values() method to get all values
values = my_dict.values()
print("Values in the dict:", values)

# using items() method to get all key-value pairs
items = my_dict.items()
print("Items in the dict:", items)

# difference between del and pop() method is that del removes the key-value pair without returning the value,
# whereas pop() removes the key-value pair and returns the value associated with the key.