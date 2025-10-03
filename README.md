# 🛍️ Customer Segmentation and Recommendation System

This project implements a data-driven customer segmentation and recommendation engine using the Online Retail dataset. The system leverages RFM (Recency, Frequency, Monetary) analysis, clustering techniques, and a lightweight recommendation algorithm to provide personalized product suggestions.

To make insights accessible, the system is deployed as a Streamlit dashboard that allows business teams to explore customer behavior, analyze product trends, and get real-time recommendations without writing code.

🎯 Objective

Segment customers based on purchasing patterns

Identify high-value customers for targeted campaigns

Build a simple recommendation engine for product suggestions

Provide an interactive dashboard for visualization & exploration

💼 Business Use Case

Retail businesses face challenges like:

Identifying loyal vs. one-time buyers

Targeting the right customers with promotions

Recommending products to increase cross-sell & up-sell opportunities

This project provides:
✔️ Customer insights (segmentation, behavior patterns)
✔️ Top product analysis (popular items, sales drivers)
✔️ Personalized recommendations (per customer ID)
✔️ Visual analytics dashboard for business users

⚙️ Prerequisites

Python ≥ 3.8

Installed packages:

pip install streamlit pandas plotly scikit-learn openpyxl


Dataset files:

OnlineRetail.xlsx (raw data)

rfm_clusters.csv (pre-computed RFM + clustering results)

📂 Project Structure
📦 customer-segmentation-recommendation-system
 ┣ 📜 customer_dashboard.py     # Streamlit dashboard
 ┣ 📜 OnlineRetail.xlsx         # Input dataset
 ┣ 📜 rfm_clusters.csv          # Pre-computed RFM segments
 ┣ 📜 README.md                 # Documentation
 ┗ 📜 reports                   # Detailed project report

🧠 Technical Workflow
1️⃣ Data Preprocessing

Removed null values and duplicates

Generated TotalPrice = Quantity × UnitPrice

Extracted transactional features

2️⃣ Feature Engineering (RFM Analysis)

Recency: Days since last purchase

Frequency: Number of transactions

Monetary: Total spend

3️⃣ Customer Segmentation (Clustering)

Normalized RFM features

Applied KMeans clustering (Elbow method for K)

Segmented customers into groups like:

Champions (high RFM)

Loyal Customers

At Risk

Lost Customers

4️⃣ Recommendation Engine

Based on customer purchase history

Fallback: Popular products if customer has limited history

Future scope: Collaborative filtering & embeddings

5️⃣ Dashboard (Streamlit)

Sections included:

📈 Sales Trend Over Time

🏆 Top Products by Sales

👥 Customer Segments Overview

🎯 Personalized Recommendations

📊 Sample Dashboard Preview

Sales Trend → visualize growth over time

Top Products → highlight best-sellers

Customer Segments → cluster distribution (pie chart)

Recommendations → instantly view products per customer

📈 Results & Insights

Segmented customers into 4 clusters

Identified top revenue-generating products

Delivered personalized recommendations with fallback logic

Business teams can now use the dashboard for decision-making

🔮 Future Scope

Integrate Collaborative Filtering (CF) and Content-based Filtering

Real-time API deployment (Flask/FastAPI + Streamlit)

Automated marketing strategies per segment

Deploy on cloud (Heroku/Streamlit Cloud/AWS)
