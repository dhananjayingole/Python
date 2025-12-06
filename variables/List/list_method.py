# append
a = [1,2,3]
a.append(4)  # appending an element to the list
print("List after append:", a)
# extend
b = [5,6]
a.extend(b)  # extending list a by adding elements from list b
print("List after extend:", a)

# insert
a.insert(2, 2.5)  # inserting 2.5 at index 2
print("List after insert:", a)

# remove
a.remove(2.5)  # removing the first occurrence of 2.5       
print("List after remove:", a)

# pop
popped_element = a.pop()  # removing and returning the last element 
print("Popped element:", popped_element)

# you can pop specific index element also.
popped_element = a.pop(0)  # removing and returning element at index 1
print("Popped element at index 1:", popped_element)

# index
index_of_3 = a.index(3)  # getting the index of first occurrence of 3
print("Index of 3:", index_of_3)

# count
count_of_2 = a.count(2)  # counting occurrences of 2    
print("Count of 2:", count_of_2)

# sort
a.sort()  # sorting the list in ascending order 
print("List after sort:", a)

# reverse
a.reverse()  # reversing the list       
print("List after reverse:", a)

# finidng Common Elements between two lists
list1 = [1, 2, 3, 4, 5] 
list2 = [4, 5, 6, 7, 8]

s1 = set(list1)
s2 = set(list2)

s3 = s1.intersection(s2)  # finding common elements
common_elements = list(s3)  # converting set back to list
print("Common elements between list1 and list2:", common_elements)