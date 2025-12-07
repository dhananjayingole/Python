# tuples are immutable, heterogenous collections of items
# they are defined using parentheses ()
my_tuple = (1, "hello", 3.14, True)
print("Original tuple:", my_tuple) 
print(my_tuple[1])
print(my_tuple[0:3])

# in tuples, we cannot add, remove or modify elements
# the following operations will raise errors if uncommented 
# my_tuple[1] = "world"  # TypeError: 'tuple' object does not support item assignment
# my_tuple.append(5)     # AttributeError: 'tuple' object has no attribute
# my_tuple.remove(3.14) # AttributeError: 'tuple' object has no attribute
# however, we can concatenate tuples to create a new tuple
new_tuple = my_tuple + (5, 6, 7)    
print("New tuple after concatenation:", new_tuple)

# we can use functions like len(), min(), max(), sort(), count(), and sum() on tuples.
