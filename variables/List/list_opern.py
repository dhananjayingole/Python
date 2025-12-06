list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print("Original List:", list1)
list1[0] = 100  # modifying the first element
print("Modified List:", list1)

# to modify multiple elements
list1[1:4] = [200, 300, 400]  # modifying elements from index 1 to 3
print("List after modifying multiple elements:", list1)

# concatenation of two lists
combined_list = list1 + list2   
print("Concatenated List:", combined_list)