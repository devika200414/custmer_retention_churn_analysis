import pandas as pd

rfm = pd.read_csv(
    r"C:\Users\user\Desktop\Customer Retention Project\projectdataset\customer_churn_analysis.csv"
)

rfm["CLV"] = rfm["Monetary"]

print("Average CLV:")
print(rfm["CLV"].mean())

print("\nTop 10 Customers by CLV:")
print(
    rfm[
        ["CustomerID", "CLV"]
    ]
    .sort_values("CLV", ascending=False)
    .head(10)
)
clv_by_segment = (
    rfm.groupby("Segment")["CLV"]
    .mean()
    .sort_values(ascending=False)
)

print(clv_by_segment)
clv_by_churn = (
    rfm.groupby("Churn")["CLV"]
    .mean()
)

print(clv_by_churn)