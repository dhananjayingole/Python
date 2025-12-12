import pandas as pd
data = {
    "Name": ["Ram", "Shyam", "Ghanshyam","Lakshman","Hanuman","Ravan","Kumbhkaran","Vibhishan"],
    "Age": [10, 20, 30, 25, 35, 40, 45, 50],
    "City": ["Nagpur", "Mumbai", "Delhi", "Agra", "Mathura", "Pune", "Goa", "Bangalore"],
    "Salary": [1000, 2000, 3000, 2500, 3500, 4000, 4500, 5000],
    "Performance Score": [85, 90, 78, 88, 92, 80, 75, 95]
}

df = pd.DataFrame(data)
print(df)

# Adding A new Col to the DataFrame
df["Bonus"] = df["Salary"] * 0.1 # 10% of Salary as Bonus
print("After Adding Bonus Column:")
print(df)
# using insert method ->df.insert(loc, column_name, some_data)
df.insert(0, "Employee ID", [101, 102, 103, 104, 105, 106, 107, 108])
print("After Inserting Employee ID Column at position 0:")
print(df)

# updating value by .loc[row_index, 'column_name'] = new_value
df.loc[2, "City"] = "Chennai"  # Updating City of Ghanshyam
print("After Updating City of Ghanshyam:")
print(df)

# if wants to update multiple values based on condition
# let increasing salary by 10% for those whose Performance Score > 80
df.loc[df["Performance Score"] > 80, "Salary"] *= 1.1
print("After Increasing Salary by 10% for Performance Score > 80:")
print(df)

# removing columns using drop method -> df.drop(columns=['column_name','column_name2','''''], inplace=True)
df.drop(columns=["Bonus"],inplace = True)
print("After Dropping Bonus Column:")
print(df)