import pandas as pd

df_Region1 = pd.DataFrame({
    'CustomerID': [1,2],
    'Name': ["gopal","Raju"]
})

# order dataframe
df_Region2 = pd.DataFrame({
    'CustomerID': [3,4],
    'Name': ["shyam","baburao"]
})

# concating vertically
df_concat= pd.concat([df_Region1, df_Region2], axis=0, ignore_index=True)
print("Concatinate ColumnWise:")
print(df_concat)

# horizontally
df_concat= pd.concat([df_Region1, df_Region2], axis=1, ignore_index=True)
print("Concatinate Row Wise:")
print(df_concat)