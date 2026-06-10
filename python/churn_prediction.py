import pandas as pd

rfm = pd.read_csv(
    r"C:\\Users\\user\\Desktop\\Customer Retention Project\\projectdataset\\customer_churn_analysis.csv"
)

print(rfm.head())
print(rfm.shape)
import pandas as pd

rfm = pd.read_csv(
    r"C:\\Users\\user\\Desktop\\Customer Retention Project\\projectdataset\\customer_churn_analysis.csv"
)

print(rfm.shape)
print(rfm.columns)
print(rfm.head())
rfm["Churn_Flag"] = rfm["Churn"].map({
    "No": 0,
    "Yes": 1
})
print(rfm["Churn"].value_counts())
print(rfm["Churn_Flag"].value_counts())
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = rfm[["Frequency", "Monetary"]]

y = rfm["Churn_Flag"]

X_train, X_test, y_train, y_test = train_test_split( X, y,test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

rfm["Churn_Probability"] = model.predict_proba(X)[:,1]

print("\nProbability Summary")
print(rfm["Churn_Probability"].describe())

print("\nTop 10 Highest Risk Customers")
print(
    rfm[
        ["CustomerID","Churn_Probability"]
    ]
    .sort_values(
        "Churn_Probability",
        ascending=False
    )
    .head(10)
)

print("\nBottom 10 Lowest Risk Customers")
print(
    rfm[
        ["CustomerID","Churn_Probability"]
    ]
    .sort_values(
        "Churn_Probability",
        ascending=True
    )
    .head(10)
)
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

from sklearn.metrics import accuracy_score

rf_accuracy = accuracy_score(
    y_test,
    rf_predictions
)

print("Random Forest Accuracy:", rf_accuracy)
rfm[
    [
        "CustomerID",
        "Segment",
        "Churn",
        "Churn_Probability"
    ]
]
rfm.to_csv(
    r"C:\Users\user\Desktop\Customer Retention Project\projectdataset\customer_churn_predictions.csv",
    index=False
)

print("Customer churn predictions saved successfully!")