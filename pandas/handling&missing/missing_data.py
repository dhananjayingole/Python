# representation of missing data in pandas includes
# NaN (Not a Number) 
# None (for object data types)

# isNull() method is used to detect missing values in a DataFrame.
# if true -> Nan is missing
# if false -> value is present
import pandas as pd

data = {
    "Name": ["Ram",None, "Ghanshyam","Lakshman","Hanuman","Ravan","Kumbhkaran","Vibhishan"],
    "Age": [10, None, 30, 25, 35, 40, 45, 50],
    "City": ["Nagpur", None, "Delhi", "Agra", "Mathura", "Pune", "Goa", "Bangalore"],
    "Salary": [1000, None, 3000, 2500, 3500, 4000, 4500, 5000],
    "Performance Score": [85, None, 78, 88, 92, 80, 75, 95]
}

df = pd.DataFrame(data)

print(df.isnull())  # Detecting missing values
print(df.isnull().sum())  # Counting missing values in each column
