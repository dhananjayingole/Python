import pandas as pd
data = {
    "Name": ["Ram", "Shyam", "Ghanshyam","Lakshman","Hanuman","Ravan","Kumbhkaran","Vibhishan"],
    "Age": [10, 20, 30, 25, 35, 40, 45, 50],
    "City": ["Nagpur", "Mumbai", "Delhi", "Agra", "Mathura", "Pune", "Goa", "Bangalore"],
    "Salary": [1000, 2000, 3000, 2500, 3500, 4000, 4500, 5000],
    "Performance Score": [85, 90, 78, 88, 92, 80, 75, 95]
}

df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)

# Accessing Single Column
print("\nAccessing 'Name' Column:")
print(df['Name'])
# Accessing Multiple Columns
print("\nAccessing 'Name', 'Salary' and 'City' Columns:")
print(df[["Name","Salary","City"]])

# Accessing Single condition rows
high_salary = df[df['Salary'] > 3000]
print("\nEmployees with Salary greater than 3000:")
print(high_salary)

# Accessing Multiple condition rows
high_perf_high_salary = df[(df['Salary'] > 3000) & (df['Performance Score'] > 80)]
print("\nEmployees with Salary greater than 3000 and Performance Score greater than 80:")
print(high_perf_high_salary)

# Accessing Rows by Index Position
second_row = df.iloc[1]
print("\nSecond Row of the DataFrame:")
print(second_row)
