import pandas as pd

df = pd.read_csv("Nike_Sales_Uncleaned.csv")
#print(df.shape)
#print("Null\n",df.isnull().sum())
#print(df.head())
#print(df.dtypes)

#Dropping Duplicates
df = df.drop_duplicates(subset='Order_ID', keep='first')

#Fixing the logic
df['Discount_Applied'] = df["Discount_Applied"].fillna(0.0)

#Imputing Math
df["Units_Sold"] = df['Units_Sold'].fillna(df['Units_Sold'].median())

#Imputing the Text
df["Size"] = df['Size'].fillna("UNKNOWN")

#Normalizing the Cities
df['Region'] = df['Region'].str.upper()
df["Region"] = df['Region'].replace('HYD', 'HYDERABAD', regex=False)

df.to_csv("Nike_sales_audit.csv", index=False)

print(df.head())
print(df['Region'].unique())
print("Null Count: ",df['Units_Sold'].isnull().sum())