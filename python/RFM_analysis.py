import pandas as pd
df = pd.read_csv("C:\\Users\\user\\Desktop\\Customer Retention Project\\projectdataset\\cleaned_online_retail.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

print(reference_date)
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (reference_date - x.max()).days,
    "InvoiceNo": "nunique",
    "Revenue": "sum"
}).reset_index()
rfm.columns = [
    "CustomerID",
    "Recency",
    "Frequency",
    "Monetary"
]
print(rfm.head())
rfm.to_csv(
    "C:\\Users\\user\\Desktop\\Customer Retention Project\\projectdataset\\rfm_table.csv",
    index=False
)

print("RFM table saved successfully!")
# Recency Score
rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5,4,3,2,1]
)

# Frequency Score
rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1,2,3,4,5]
)

# Monetary Score
rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    5,
    labels=[1,2,3,4,5]
)

print(rfm.head())
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

print(rfm.head())

def segment_customer(row):

    if row["R_Score"] >= 4 and row["F_Score"] >= 4 and row["M_Score"] >= 4:
        return "Champion"

    elif row["R_Score"] >= 3 and row["F_Score"] >= 4:
        return "Loyal Customer"

    elif row["R_Score"] >= 4 and row["F_Score"] >= 2:
        return "Potential Loyalist"

    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk"

    else:
        return "Lost Customer"
rfm["Segment"] = rfm.apply(segment_customer, axis=1)

print(
    rfm[["CustomerID","RFM_Score","Segment"]].head(10)
)
rfm.to_csv(
    r"C:\Users\user\Desktop\Customer Retention Project\projectdataset\rfm_segmented.csv",
    index=False
)

print("RFM Segmentation saved successfully!")