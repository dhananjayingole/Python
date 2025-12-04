# while loop
i = 1
while i <= 5:
    print("Iteration:", i)
    i = i + 1

#  for loop
# here range -> it shows as (start, stop, step)
for i in range(1, 8, 2):
    print("Iterations: ", i) 
    # 1, 3, 5, 7

# nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print("i =", i, ", j =", j)

# iteration through a list
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print("Fruit:", i)
