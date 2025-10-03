# 🛍️ Customer Segmentation and Recommendation System

📌 Project Overview

This project analyzes customer purchasing behavior using online retail transaction data and builds a recommendation system to provide personalized product suggestions. It combines customer segmentation (RFM + clustering) with recommendation models to help businesses improve retention, marketing, and revenue.

🎯 Objectives

Segment customers based on Recency, Frequency, and Monetary (RFM) values.

Apply clustering techniques (KMeans, Agglomerative) to group similar customers.

Perform exploratory data analysis (EDA) to uncover sales trends, top products, and customer patterns.

Build recommendation systems (collaborative & content-based filtering).

Create an interactive dashboard with Streamlit for visualization and recommendations.

📦 Dataset

Source: Online Retail dataset (transactions from a UK-based retailer).

Size: ~500K rows

Key Columns:

InvoiceNo, StockCode, Description

Quantity, InvoiceDate, UnitPrice

CustomerID, Country

🛠️ Methodology

Data Preprocessing

Removed missing values, duplicates, and invalid entries.

Created new features such as TotalPrice (Quantity × UnitPrice).

Exploratory Data Analysis (EDA)

Sales trend over time.

Top-selling products.

Customer purchase behavior distribution.

Customer Segmentation (RFM + Clustering)

Calculated Recency, Frequency, Monetary values for each customer.

Applied KMeans (k=4) and Agglomerative clustering.

Segmented customers into 4 key groups (loyal, high spenders, at-risk, and inactive).

Recommendation System

Collaborative Filtering: Product recommendations based on similar customers.

Content-Based Filtering: Recommendations using product features and purchase history.

Dashboard (Streamlit)

Sales trends visualization.

Top 10 products chart.

Customer segmentation overview.

Interactive customer-specific recommendations.

⚙️ Prerequisites

Make sure you have installed:

python >= 3.9
pip >= 21.0


Libraries needed (already in requirements.txt):

pandas

numpy

scikit-learn

matplotlib

seaborn

plotly

streamlit

openpyxl

Install all at once:

pip install -r requirements.txt

📊 Dashboard Features

Sales Trend Over Time: Identify seasonal trends and peaks.

Top Products: Best-selling products.

Customer Segments: Distribution of customer clusters.

Personalized Recommendations: Enter/select a CustomerID to view tailored product suggestions.

📈 Results

From the analysis and modeling:

Customer Segmentation:

Optimal 4 clusters (KMeans) found.

Segments included high-value loyal customers, frequent buyers, price-sensitive, and at-risk groups.

Recommendation System Evaluation (Top-5):

Average Precision@5: 0.8529

Average Recall@5: 0.5453

MAP@5 (Mean Average Precision): 0.8865

Insights:

A small % of customers contribute to ~80% of revenue (Pareto principle).

Top products are decor, gifts, and seasonal items.

Recommendations generated personalized product suggestions per customer ID.

🚀 How to Run

Clone this repo:

git clone https://github.com/your-username/customer-segmentation-recommendation.git
cd customer-segmentation-recommendation


Install dependencies:

pip install -r requirements.txt


Run Streamlit Dashboard:

streamlit run customer_dashboard.py

🔮 Future Enhancements

Deploy recommendation API for real-time use.

Add deep learning-based recommender systems (e.g., neural collaborative filtering).

Enhance dashboard with advanced filters (date range, region, product categories).

📚 Tech Stack

Python, Pandas, NumPy, Scikit-learn – Data processing & modeling

Matplotlib, Seaborn, Plotly – Visualization

Streamlit – Interactive dashboard

Excel/CSV Dataset – Data source

✨ This project demonstrates how businesses can leverage data science to better understand customers and provide personalized shopping experiences
