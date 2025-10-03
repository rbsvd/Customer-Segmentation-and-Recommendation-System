# 🛍️ Customer Segmentation & Recommendation System

## 📖 Introduction

This project explores **customer behavior in online retail** using **data science and machine learning**.

By analyzing transaction data, we can segment customers, identify top products, and provide **personalized recommendations**. The project combines **data preprocessing, exploratory data analysis, clustering, and recommendation modeling** into a complete workflow.

**Why this project matters:**

* Businesses can focus on **loyal or high-value customers**.
* Personalized recommendations improve **sales and retention**.
* Insights from RFM and clustering uncover hidden **customer patterns**.

---

## 🧮 1. Customer Segmentation

**Recency, Frequency, Monetary (RFM) Analysis:**

* **Recency:** How recently a customer made a purchase.
* **Frequency:** How often a customer purchases.
* **Monetary:** How much a customer spends.

We calculate RFM scores for all customers and then apply **clustering algorithms**:

* **KMeans (k=4)** → Groups customers into 4 key segments.
* **Agglomerative Clustering** → Confirms hierarchical relationships between segments.

**Example segments identified:**

1. High-value loyal customers
2. Frequent buyers
3. Price-sensitive customers
4. At-risk / inactive customers

---

## 🔢 2. Recommendation Systems

Two approaches were applied:

1. **Collaborative Filtering:**

   * Suggests products by identifying customers with similar purchase behavior.

2. **Content-Based Filtering:**

   * Suggests products similar to what a customer already bought.

These models allow us to generate **personalized recommendations per customer**.

---

## 📊 3. Project Workflow

**Step 1: Data Preprocessing**

* Remove missing values and duplicates.
* Compute `TotalPrice = Quantity × UnitPrice`.
* Filter out canceled or invalid transactions.

**Step 2: Exploratory Data Analysis (EDA)**

* Identify **top-selling products**.
* Explore **sales trends over time**.
* Analyze **customer purchase distributions**.

**Step 3: Customer Segmentation**

* Compute RFM scores.
* Apply KMeans and Agglomerative clustering.
* Label segments and visualize clusters.

**Step 4: Recommendation Modeling**

* Train collaborative and content-based models.
* Evaluate top-5 product recommendations using **Precision@5, Recall@5, MAP@5**.

**Step 5: Dashboard Deployment (Streamlit)**

* Visualize **sales trends, top products, and customer clusters**.
* Enter a `CustomerID` to get **real-time personalized recommendations**.

---

## ⚙️ 4. Prerequisites

**Python >= 3.9**
**pip >= 21.0**

Install libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn plotly streamlit openpyxl
```

---

## 📈 5. Sample Dataset

* **Rows:** ~500,000 transactions
* **Columns:**
  `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`

**Derived Features:**

* `TotalPrice` per transaction
* RFM scores per customer

---

## 📊 6. Model Evaluation & Results

**Customer Segmentation (KMeans, k=4):**

* Identified four distinct segments with **business-relevant insights**.

**Recommendation System (Top-5 products):**

| Metric              | Value  |
| ------------------- | ------ |
| Average Precision@5 | 0.8529 |
| Average Recall@5    | 0.5453 |
| MAP@5               | 0.8865 |

**Key Insights:**

* ~20% of customers generate ~80% of revenue (Pareto principle).
* Top-selling products: **decor, gifts, and seasonal items**.
* Personalized recommendations deliver **high relevance per customer**.

---

## 🚀 7. How to Run

1. Clone repository:

```bash
git clone https://github.com/your-username/customer-segmentation-recommendation.git
cd customer-segmentation-recommendation
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit dashboard:

```bash
streamlit run customer_dashboard.py
```

---

## 🔮 8. Future Enhancements

* Deploy **real-time recommendation API**.
* Use **deep learning** (neural collaborative filtering) for improved recommendations.
* Add **advanced dashboard filters** (date range, region, product categories).
* Integrate **customer feedback** to continuously improve recommendations.

---

## 📚 9. Tech Stack

* **Python, Pandas, NumPy, Scikit-learn** → Data processing & ML
* **Matplotlib, Seaborn, Plotly** → Visualization
* **Streamlit** → Interactive dashboard
* **Excel/CSV Dataset** → Source data

---

## 🏁 10. Conclusion

This project demonstrates how **data science can transform raw retail transaction data into actionable business insights**.

Through **RFM-based customer segmentation** and **personalized recommendations**, businesses can:

* Understand **customer value** and **purchase behavior**.
* Target marketing strategies to **loyal and high-value segments**.
* Improve **sales and customer retention** through data-driven suggestions.

The combination of **data preprocessing, EDA, clustering, recommendation modeling, and interactive visualization** provides a **complete, end-to-end solution** that can be extended to real-time deployment or deep learning enhancements.

