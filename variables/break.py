# Break Statement -> used for terminating the loop entirely when a certain condition is met.
for num in range(1, 10, 1):
    if num == 5:
        break
    print("Number:", num)

# Continue Statement ->used for skipping the current iteration and moving to the next iteration of the loop.
for num in range(1, 10, 1):
    if num == 5:
        continue
    print("Number:", num)

# Pass Statement -> used as a placeholder when a statement is syntactically required but no action is needed.
for num in range(1, 6): 
    if num == 3:
        pass  # Placeholder for future code
    print("Number:", num)