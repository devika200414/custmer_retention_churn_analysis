Customer Retention & Churn Analysis

End-to-End Customer Analytics Project using Excel, SQL, Python, Machine Learning, and Power BI

Project Overview

Customer retention is one of the most important factors influencing business growth and profitability. Acquiring new customers is often more expensive than retaining existing ones, making customer behavior analysis a critical business function.
This project demonstrates an end-to-end customer analytics workflow that transforms raw retail transaction data into actionable business insights. Using Excel, SQL, Python, Machine Learning, and Power BI, the project identifies customer segments, analyzes churn behavior, estimates revenue at risk, and predicts customers likely to stop purchasing.

The goal is to help businesses make data-driven decisions that improve retention, reduce customer loss, and maximize revenue.

Business Problem

Retail businesses generate thousands of customer transactions every day, but raw data alone does not explain:

Which customers generate the highest revenue

Which customer groups are most likely to churn

How much revenue is at risk due to customer loss

Which customers should be targeted by retention campaigns

How customer purchasing behavior changes over time

This project addresses these challenges through customer segmentation, churn analysis, and predictive modeling.


Dataset

The project uses a retail transaction dataset containing customer purchases across multiple countries.

Dataset Information

Total Customers Analyzed: 4,338

Total Transactions: 18,532

Total Revenue: 8.89 Million

Multiple Countries Included

Product-Level Transaction Data

Tools & Technologies

Microsoft Excel

Initial data cleaning

Data validation

Duplicate identification

Pivot table analysis

Preliminary business insights

SQL (SQLite)

Data querying

Aggregations

Customer-level analysis

Revenue calculations

Business metric extraction

Python

Libraries Used:

Pandas

NumPy

Matplotlib

Seaborn

Scikit-Learn

Power BI

KPI dashboards

Interactive visualizations

Customer segmentation reports

Churn monitoring dashboards

Machine Learning

Logistic Regression

Data preprocessing

Churn probability prediction

Customer risk classification

Project Workflow

1. Data Cleaning
   
The raw dataset contained duplicates, missing values, and invalid records.

Cleaning activities included:

Removing duplicate transactions

Handling missing values

Removing invalid quantities

Removing invalid unit prices

Creating a Revenue column

Standardizing data types

Exporting a cleaned dataset for analysis

Output

Cleaned Retail Dataset

3. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand customer purchasing behavior and business performance.

Analysis included:

Monthly revenue trends

Country-wise revenue analysis

Product performance analysis

Customer activity patterns

Sales distribution analysis

Key Findings

Revenue was concentrated among a small group of high-performing products.

The United Kingdom generated the highest revenue contribution.

Customer purchasing behavior varied significantly across segments.

4. RFM Customer Segmentation

Customers were segmented using the RFM Framework:

Recency

Frequency

Monetary Value

Each customer received an RFM score and was assigned to a business segment.

Customer Segments

Champion

Recent customers with high purchase frequency and spending.

Loyal Customer

Consistent customers who contribute stable revenue.

Potential Loyalist

Customers showing signs of becoming long-term buyers.

At Risk

Customers who previously purchased but have become inactive.

Lost Customer

Customers with long periods of inactivity and low engagement.

4. Churn Analysis

Customer churn analysis was performed to understand customer loss patterns.

Analysis included:

Overall churn rate

Segment-wise churn rate

Customer distribution by churn status

High-risk customer identification

Results

Retention Rate: 66.60%

Churn Rate: 33.40%

The analysis revealed that churn was concentrated within specific customer segments, creating opportunities for targeted retention campaigns.

5. Machine Learning Churn Prediction

A Logistic Regression model was developed to predict customer churn probability.

Model Features

Recency

Frequency

Monetary Value

Customer Segment

Model Output

The model generated:

Churn Probability Score

Risk Category

High-Risk Customer List

Low-Risk Customer List

Performance

Model Accuracy: 71.31%

The model enables proactive customer retention by identifying customers most likely to churn.

Key Business Insights

Revenue Insights

Total Revenue Generated: 8.89 Million

Revenue At Risk: 53,605.96

Customer Insights

Total Customers: 4,338

Retention Rate: 66.60%

Churn Rate: 33.40%

Segmentation Insights

Champions generated the highest revenue contribution.

Lost Customers represented a significant portion of the customer base.

At Risk customers displayed elevated churn probabilities.

Loyal Customers demonstrated strong retention behavior.

Business Impact

The project helps organizations:

Identify valuable customers

Reduce churn risk

Prioritize retention campaigns

Protect revenue streams

Improve customer lifetime value

Power BI Dashboards

Customer Retention & Revenue Dashboard

Features:

Revenue KPIs

Customer KPIs

Country-wise revenue

Product performance

Monthly revenue trends

Revenue by Segment Dashboard

Features:

Revenue contribution by segment

Customer distribution by segment

Segment comparison

Churn Analysis Dashboard

Features:

Churn distribution

Segment-wise churn analysis

Customer loss monitoring

ML Churn Prediction Dashboard

Features:

Risk category analysis

Churn probability visualization

High-risk customer tracking

Project Structure

customer_retention_churn_analysis

├── python/

│ ├── data_cleaning.py

│ ├── EDA.py

│ ├── RFM_analysis.py

│ ├── churn_analysis.py

│ └── churn_prediction.py

│

├── projectdataset/

│ ├── cleaned_online_retail.csv

│ ├── country_revenue_analysis.csv

│ ├── customer_churn_analysis.csv

│ ├── customer_churn_predictions.csv

│ ├── eda_insights.csv

│ ├── product_revenue_analysis.csv

│ ├── rfm_segmented.csv

│ └── rfm_table.csv

│

├── sql/

├── powerbi/

└── README.md


Skills Demonstrated

Data Analytics

Data Cleaning

Data Wrangling

Exploratory Data Analysis

Business Analytics

SQL

Aggregations

Filtering

Grouping

Business Queries

Python

Data Manipulation

Data Visualization

Statistical Analysis

Machine Learning

Business Intelligence

Dashboard Design

KPI Development

Data Storytelling

Executive Reporting

Customer Analytics

RFM Segmentation

Customer Retention Analysis

Churn Analysis

Revenue Risk Assessment


Conclusion

This project demonstrates a complete data analytics lifecycle, beginning with raw transactional data and ending with predictive customer intelligence. By combining Excel, SQL, Python, Machine Learning, and Power BI, the project provides meaningful insights into customer behavior, retention patterns, and business performance.

The resulting analytics framework can support data-driven decision-making, improve customer retention strategies, and help businesses reduce revenue loss caused by customer churn.
