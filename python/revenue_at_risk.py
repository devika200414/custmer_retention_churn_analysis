import pandas as pd

rfm = pd.read_csv(
    r"C:\Users\user\Desktop\Customer Retention Project\projectdataset\customer_churn_predictions.csv"
)

high_risk = rfm[
    rfm["Churn_Probability"] >= 0.5
]

print("High Risk Customers:", len(high_risk))

print(
    "Revenue At Risk:",
    round(high_risk["Monetary"].sum(), 2)
)