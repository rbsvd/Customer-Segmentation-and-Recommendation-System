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


🔮 Future Scope

Integrate Collaborative Filtering (CF) and Content-based Filtering

Real-time API deployment (Flask/FastAPI + Streamlit)

Automated marketing strategies per segment

Deploy on cloud (Heroku/Streamlit Cloud/AWS)
