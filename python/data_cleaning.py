import pandas as pd

df = pd.read_csv("projectdataset/online_retail.csv")

print("Duplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("Shape after removing duplicates:")
print(df.shape)
print(df.isnull().sum())
# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nData Types:")
print(df.dtypes)
# Remove rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove rows with missing Description
df = df.dropna(subset=["Description"])

print("\nShape after removing missing values:")
print(df.shape)
# Remove invalid Quantity
df = df[df["Quantity"] > 0]

# Remove invalid UnitPrice
df = df[df["UnitPrice"] > 0]

print("\nShape after removing invalid records:")
print(df.shape)
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print(df[["Quantity", "UnitPrice", "Revenue"]].head())
df.to_csv("projectdataset/cleaned_online_retail.csv", index=False)

print("Cleaned dataset saved successfully!")