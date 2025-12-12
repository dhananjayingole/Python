# dropna()
# df.dropna(axis = 0, inplace = True)  # Drops rows with any missing values
# if axis 1 -> Drops columns with any missing values
# inplace True -> modifies the original DataFrame

import pandas as pd

data = {
    "Name": ["Ram",None, "Ghanshyam","Lakshman","Hanuman","Ravan","Kumbhkaran","Vibhishan"],
    "Age": [10, None, 30, 25, 35, 40, 45, 50],
    "City": ["Nagpur", None, "Delhi", "Agra", "Mathura", "Pune", "Goa", "Bangalore"],
    "Salary": [1000, None, 3000, 2500, 3500, 4000, 4500, 5000],
    "Performance Score": [85, None, 78, 88, 92, 80, 75, 95]
}

df = pd.DataFrame(data)
print(df)

# to drop missing elements.
# df.dropna(inplace=True)
# print("\nDataFrame after dropping rows with missing values:")
# print(df)

# Replacing missing value with other/defualt value.
df.fillna(0,inplace=True)
print("Replacing default Value:")
print(df)

# let we have to Replace Age with mean value
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)
