import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam"],
    "Age": [10, 20, 30],
    "City": ["Nagpur", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print(df)

# to save DataFrame to an Excel file
# df.to_excel("output.xlsx", index=False)
# to save DataFrame to a JSON file
# df.to_json("output.json", orient='records', lines=True)
# to save DataFrame to a CSV file
df.to_csv("output.csv", index=False)
print(df.describe())