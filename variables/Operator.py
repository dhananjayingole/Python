# arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division - gives float value
print("Floor Division:", a // b)   # Floor Division - gives integer value
print("Exponentiation:", a ** b)   # Exponentiation- gives Power
print("Modulus:", a % b)           # Modulus - gives reminder

# comparison Operators
print("Equal to:", a == b)         # Equal to
print("Not equal to:", a != b)     # Not equal to  
print("Greater than:", a > b)      # Greater than
print("Less than:", a < b)         # Less than          
print("Greater than or equal to:", a >= b)  # Greater than or equal to
print("Less than or equal to:", a <= b)     # Less than or equal to    


# logical Operators
age = 22
is_student = True  

print("Logical AND:", age > 18 and is_student)        # Logical AND -  shows true if both conditions are true
print("Logical OR:", age > 25 or is_student)          # Logical OR - shows true if at least one condition is true
print("Logical NOT:", not is_student)          # Logical NOT
print("Logical NOT:", not age > 18)          # Logical NOT- gives opposite value

# Assignment Operators
x = 5
print("Initial value of x:", x)
x += 3
print("After x += 3:", x)
x -= 2
print("After x -= 2:", x)
x *= 4
print("After x *= 4:", x)
x /= 3

print("After x /= 3:", x)
x //= 2
print("After x //= 2:", x)
x **= 2
print("After x **= 2:", x)

# Identity Operators
y = x
print("x is y:", x is y)           # Identity Operator - is
print("x is not y:", x is not y)   # Identity Operator - is not

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)         # Membership Operator - in
print("6 not in my_list:", 6 not in my_list) # Membership Operator - not in

# Bitwise Operators
p = 10  # In binary: 1010   
q = 4   # In binary: 0100
print("Bitwise AND:", p & q)        # Bitwise AND - gives 0 if both bits are 0 else gives 1
print("Bitwise OR:", p | q)         # Bitwise OR - gives 1 if at least one bit is 1 else gives 0
print("Bitwise XOR:", p ^ q)        # Bitwise XOR - gives 1 if both bits are different else gives 0
print("Bitwise NOT:", ~p)            # Bitwise NOT - inverts all bits
print("Left Shift p by 2:", p << 2)  # Left Shift- shifts bits to the left, adding zeros on the right
print("Right Shift p by 2:", p >> 2) # Right Shift - shifts bits to the right, removing bits on the right
