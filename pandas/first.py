import pandas as pd
# read of excel file
# df = pd.read_excel("D:\Python\pandas\SampleSuperstore.xlsx", sheet_name='Sample Superstore')
# read of json file
df = pd.read_json("D:\Python\pandas\sample_Data.json")
# read data from CSV file
# df = pd.read_csv("D:\Python\pandas\sales_data_sample.csv", encoding='latin1')
print(df.head(3)) #-> it return first 5 rows by default, otherwise you can pass number as argument
print(df.tail(3)) #-> it return last 5 rows by default, otherwise you can pass number as argument

print(df.info()) #it Display the Info of datasets.

print("Statistical DataSet:",df.describe()) #it Display the statistical summary of datasets.
print("Columns in DataSet:",df.columns) #it Display the columns of datasets.
print("Shape of DataSet:",df.shape) #it Display the shape of datasets.
print("DataSet Index:",df.index) #it Display the index of datasets.
