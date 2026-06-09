import pandas as pd
import numpy as np

print("")

#Reading the CSV file and turning it into a Pandas DataFrame
df = pd.read_csv("Nike_sales_audit.csv")

#Imputing Values
df['MRP'] = df['MRP'].fillna(df.groupby('Product_Name')['MRP'].transform('median'))

#Vectorized Financial Engineering
df['Revenue'] = df['Units_Sold'] * df['MRP'] * (1 - df['Discount_Applied'])

#Date Unification
df['Order_Date'] = pd.to_datetime(df["Order_Date"], format='mixed', errors='coerce')

nulls = df['Order_Date'].isnull().sum() #Finding total number of NULL value rows
df = df.dropna(subset=['Order_Date'])   #Dropping the null value rows

df['Order_Month'] = df['Order_Date'].dt.month_name() #Creating a new column for extracting month names

df['Region'] = df['Region'].replace('BENGALURU', 'BANGALORE', regex=False) #Standardizing the region errors

#The Executive Matrix
Executive_pivot = pd.pivot_table(
    data=df,
    index='Region',
    columns='Product_Line',
    values='Profit',
    aggfunc='sum',
    fill_value=0
)

#Printing the Executive Pivot Table
print("The Executive Summary Pivot Table:\n",Executive_pivot,"\n")