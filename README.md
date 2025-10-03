
# 🛍️ Customer Segmentation and Recommendation System

## 📖 Introduction

This project analyzes customer purchasing behavior using transactional data from an online retailer. The goal is to:

* Understand customer value and buying patterns via **RFM analysis**.
* Segment customers using **KMeans clustering**.
* Identify **top products per segment**.
* Generate **personalized product recommendations**.
* Create a **dashboard-ready summary** for business decision-making.

This README provides a **step-by-step explanation** including methodology, outputs, metrics, and visualizations.

---

## 🧮 1. RFM Analysis

We calculated three key metrics for each customer:

| Metric    | Definition                                 |
| --------- | ------------------------------------------ |
| Recency   | Days since last purchase (lower is better) |
| Frequency | Number of unique transactions              |
| Monetary  | Total money spent by the customer          |

**Example RFM snapshot:**

| CustomerID | Recency | Frequency | Monetary |
| ---------- | ------- | --------- | -------- |
| 12346      | 326     | 2         | 0.00     |
| 12347      | 2       | 7         | 4310.00  |
| 12348      | 75      | 4         | 1797.24  |
| 12349      | 19      | 1         | 1757.55  |
| 12350      | 310     | 1         | 334.40   |

---

## 🏷️ 2. Customer Segmentation (KMeans)

**Clusters were generated using scaled RFM metrics.**

**Cluster Summary:**

| Cluster | Recency | Frequency | Monetary  | Num Customers | Segment Name       | Emoji |
| ------- | ------- | --------- | --------- | ------------- | ------------------ | ----- |
| 0       | 10.75   | 28.51     | 12168.26  | 194           | Frequent Buyers    | 🟢    |
| 1       | 248.93  | 1.81      | 455.11    | 1077          | At-risk / Inactive | 🔴    |
| 2       | 5.09    | 109.91    | 124312.31 | 11            | High-value Loyal   | 💎    |
| 3       | 42.78   | 4.37      | 1320.98   | 3090          | Price-sensitive    | 🟡    |

> **Legend:**
> 🟢 – Active/Frequent Buyers
> 🔴 – At-risk / Inactive
> 💎 – High-value Loyal
> 🟡 – Price-sensitive

---

## 📊 3. Top Products per Segment

**Top 5 products purchased by each segment:**

| Segment               | Top Products (Quantity)                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 💎 High-value Loyal   | PACK OF 72 RETROSPOT CAKE CASES (6773), RABBIT NIGHT LIGHT (6532), WHITE HANGING HEART T-LIGHT HOLDER (6471), SPACEBOY LUNCH BOX (6215), HEART OF WICKER SMALL (6200)                                  |
| 🟢 Frequent Buyers    | WORLD WAR 2 GLIDERS ASSTD DESIGNS (22097), JUMBO BAG RED RETROSPOT (18190), ASSORTED COLOUR BIRD ORNAMENT (17286), PACK OF 72 RETROSPOT CAKE CASES (16645), WHITE HANGING HEART T-LIGHT HOLDER (13546) |
| 🟡 Price-sensitive    | WORLD WAR 2 GLIDERS ASSTD DESIGNS (24493), JUMBO BAG RED RETROSPOT (20556), POPCORN HOLDER (19059), PACK OF 12 LONDON TISSUES (15379), ASSORTED COLOUR BIRD ORNAMENT (13732)                           |
| 🔴 At-risk / Inactive | WORLD WAR 2 GLIDERS ASSTD DESIGNS (5377), SMALL POPCORN HOLDER (4963), WHITE HANGING HEART T-LIGHT HOLDER (4127), FAIRY CAKE FLANNEL ASSORTED COLOUR (3320), ASSORTED COLOURS SILK FAN (2624)          |

---

## 📈 4. Recommendation System Metrics

| Metric              | Value  |
| ------------------- | ------ |
| Average Precision@5 | 0.8529 |
| Average Recall@5    | 0.5453 |
| MAP@5               | 0.8865 |

> Recommendations are generated per CustomerID based on purchase history and cluster similarity.

---

## ⚙️ 5. Step-by-Step Workflow

1. **Prepare Data**

   * Compute `TotalPrice = Quantity × UnitPrice`.
   * Remove invalid, missing, or duplicate entries.

2. **Compute RFM**

   * Recency: Days since last purchase.
   * Frequency: Number of transactions.
   * Monetary: Total spend per customer.

3. **Normalize RFM Metrics**

   * Used `StandardScaler` for clustering.

4. **KMeans Clustering**

   * Applied 4-cluster KMeans.
   * Mapped clusters to segment names.

5. **Top Products per Segment**

   * Aggregated quantity of products per cluster.
   * Selected top 5 products.

6. **Generate Recommendations**

   * For each customer, suggest products from their segment and similar customers.

7. **Dashboard Ready Outputs**

   * Segment summary table with emojis
   * Top products per segment
   * Customer-level recommendations

---

## 📊 6. Segment Dashboard Mockup

| Segment               | #Customers | Avg Recency | Avg Frequency | Avg Monetary | Emoji |
| --------------------- | ---------- | ----------- | ------------- | ------------ | ----- |
| High-value Loyal 💎   | 11         | 5.09        | 109.91        | 124312.31    | 💎    |
| Frequent Buyers 🟢    | 194        | 10.75       | 28.51         | 12168.26     | 🟢    |
| Price-sensitive 🟡    | 3090       | 42.78       | 4.37          | 1320.98      | 🟡    |
| At-risk / Inactive 🔴 | 1077       | 248.93      | 1.81          | 455.11       | 🔴    |

---

## 🚀 7. How to Run

```bash
# Clone repo
git clone https://github.com/your-username/customer-segmentation-recommendation.git
cd customer-segmentation-recommendation

# Install dependencies
pip install -r requirements.txt

# Run Streamlit dashboard
streamlit run customer_dashboard.py
```

---

## 🔮 8. Future Enhancements

* Deploy **recommendation API** for real-time use.
* Integrate **deep learning-based recommenders** (neural collaborative filtering, sequence models).
* Add **filters in dashboard**: date range, country, product category.
* Monitor **segment changes over time** for retention strategies.

---

## 🏁 9. Conclusion

This project demonstrates how businesses can leverage **RFM analysis + clustering + recommendation systems** to:

* Identify high-value and at-risk customers
* Discover top-selling products per segment
* Provide personalized product suggestions
* Build actionable dashboards for business strategy

By combining **data-driven insights with interactive dashboards**, this system helps increase customer retention, optimize marketing, and maximize revenue.

