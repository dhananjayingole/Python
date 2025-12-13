# using .mean(), .sum(), .min(), .max() of particular column.

import pandas as pd

data = {
    "Name":['Arun','Varun','Karun','Narun','Marun'],
    "Age":[28,34,22,34,28], 
    "Salary":[50000, 60000, 45000, 52000, 48000]
}

df = pd.DataFrame(data)

avg_salary = df["Salary"].mean()
print(avg_salary)

# Grouping of Data -> 
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

# grouping mutliple col
multi_grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(multi_grouped)