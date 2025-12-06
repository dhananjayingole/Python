# can store different types of variables in a list
# list is ordered, mutable, and allows duplicate values.
my_list = [10, "Hello", 3.14, True, "World", 10]
print(my_list)
print("Length of the List is:",len(my_list))  # length of the list

# indexing
print("First element:", my_list[0])  # first element
print("Last element:", my_list[-1])   # last element

# iteration through list by for loop
for item in my_list:
    print(item)

# checking membership
word  = str(input('Enter a word: '))
if word in my_list:
    print("{word} is present in the list") 
else:
    print("{word} is not present in the list")

# copy method -> it doesn't share the reference of the original list.
# but instead creates a new list with the same elements then it copies.
# list2 = list1 -> then this will share the reference of list1.

list1 = [1,2,3,4,5]
list2 = list1.copy()
print("Original List:", list1)

list1.append(6)  # modifying the original list
print("Modified Copied List:", list1, list2)