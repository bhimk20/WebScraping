# Task 1 downloading a file
import pandas as pd

df = pd.read_csv("https://archives.nseindia.com/content/equities/EQUITY_L.csv")

print(df.head(5))

df.to_csv('file1.csv')


# Task 2 downloading a file
df = pd.read_csv("https://archives.nseindia.com/content/historical/EQUITIES/2022/OCT/cm04OCT2022bhav.csv.zip")

#cleaning the data
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df["SERIES"].fillna("Null", inplace=True)

df.to_csv('file2.csv')
