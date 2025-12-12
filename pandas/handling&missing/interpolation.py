# in this we fill up the Estimated value in the Missing values.
# interpolation method only replaces the numeric value with the Estimated Value.

import pandas as pd
 
data = {
    "Name": ["Ram",'Shyam', "Ghanshyam","Lakshman","Hanuman","Ravan","Kumbhkaran","Vibhishan"],
    "Age": [10, None, 30, 25, 35, 40, 45, 50],
    "City": ["Nagpur", None, "Delhi", "Agra", "Mathura", "Pune", "Goa", "Bangalore"],
    "Salary": [1000, None, 3000, 2500, 3500, 4000, 4500, 5000],
    "Performance Score": [85, None, 78, 88, 92, 80, 75, 95]
}

df = pd.DataFrame(data)
print(df)

# linear, polynomial, time, quadratic,cubic, nearest
df.interpolate(method="linear", axis = 0, inplace=True)
print(df)