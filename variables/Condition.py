age = int(input("Enter your age: "))

if age >= 18 and age <= 100:
    print("You are eligible to vote!")

elif age == 17:
    print("You will be eligible to vote next year.")

elif age <= 0:
    print("Invalid Age.")

elif age >= 101:
    print("Please Enter age Less than or equal to 100.")

else:
    print("You are not eligible to vote yet.")