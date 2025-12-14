# pd.merge(dataframe1, dataframe2, on="Column_Name",how = "type of Join")

import pandas as pd

df_Customer = pd.DataFrame({
    'CustomerID': [1,2,3],
    'Name': ["Ramesh","Suresh","Kalpesh"]
})

# order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1,2,4],
    'OrderAmount': [250, 450, 350]
})

# merge
df_merged =  pd.merge(df_Customer, df_orders, on="CustomerID", how="inner")
print("Inner Join:") # it gives only Consider those which have Common CutomerId
print(df_merged)

df_merged =  pd.merge(df_Customer, df_orders, on="CustomerID", how="outer")
print("Outer Join:") # it consider all and prit Nan for those whose value we Don't know.
print(df_merged)

df_merged =  pd.merge(df_Customer, df_orders, on="CustomerID", how="left")
print("left Join:") # it gives left one completely and put Nan if not available in right col.
print(df_merged)

df_merged =  pd.merge(df_Customer, df_orders, on="CustomerID", how="right")
print("Right Join:") # it gives right one completely and put Nan if not available in left col.
print(df_merged)

df_merged =  pd.merge(df_Customer, df_orders, on="CustomerID", how="outer")
print("Cross Join:") # it consider all df.
print(df_merged)