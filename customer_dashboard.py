# customer_dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Dashboard", layout="wide")

st.title("🛍️ Customer Segmentation & Recommendation Dashboard")

st.markdown("""
This dashboard helps you **analyze customer behavior and sales**:
- **Summary Stats:** Quick overview of total sales, customers, and products.
- **Sales Trend:** Total sales over time.
- **Top Products:** Best-selling products.
- **Customer Segments:** Groups of customers based on RFM clustering.
- **Personalized Recommendations:** Get product suggestions for each customer.
""")

# --- 1. Load Data with Caching ---
@st.cache_data
def load_transaction_data():
    cols = ['InvoiceDate', 'CustomerID', 'Description', 'Quantity', 'UnitPrice']
    df = pd.read_excel("OnlineRetail.xlsx", usecols=cols)
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df

@st.cache_data
def load_rfm_data():
    rfm = pd.read_csv("rfm_clusters.csv")
    rfm.columns = rfm.columns.str.strip().str.lower().str.replace('\u200b','')
    return rfm

df = load_transaction_data()
rfm = load_rfm_data()

# --- 2. Summary Stats ---
total_customers = df['CustomerID'].nunique()
total_sales = df['TotalPrice'].sum()
total_products = df['Description'].nunique()

st.subheader("📝 Summary Stats")
st.markdown(f"""
- **Total Customers:** {total_customers}
- **Total Sales:** ${total_sales:,.2f}
- **Total Products:** {total_products}
""")

# --- 3. Precompute Aggregates ---
@st.cache_data
def precompute_sales_trend(df):
    df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M').dt.to_timestamp()
    return df.groupby('InvoiceMonth')['TotalPrice'].sum().reset_index()

@st.cache_data
def precompute_top_products(df, n=10):
    return df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(n).reset_index()

@st.cache_data
def precompute_customer_segments(rfm):
    cluster_col = 'kmeans_cluster'  # use your RFM column
    cluster_counts = rfm[cluster_col].value_counts().reset_index()
    cluster_counts.columns = ['Cluster', 'Count']
    return cluster_counts

@st.cache_data
def get_user_products(df):
    return {uid: group['Description'].value_counts().index.tolist()
            for uid, group in df.groupby('CustomerID')}

sales_trend = precompute_sales_trend(df)
top_products = precompute_top_products(df)
customer_segments = precompute_customer_segments(rfm)
user_products = get_user_products(df)

# --- 4. Sales Trend ---
st.subheader("1️⃣ Sales Trend Over Time")
st.markdown("Total sales aggregated by month to show high/low sales periods.")
fig1 = px.line(sales_trend, x='InvoiceMonth', y='TotalPrice', title="Monthly Sales Trend")
st.plotly_chart(fig1, use_container_width=True)

# --- 5. Top Products ---
st.subheader("2️⃣ Top 10 Products by Sales")
st.markdown("Top-selling products help understand customer preferences.")
fig2 = px.bar(top_products, x='Description', y='TotalPrice', title="Top 10 Products")
st.plotly_chart(fig2, use_container_width=True)

# --- 6. Customer Segments ---
st.subheader("3️⃣ Customer Segments")
st.markdown("Shows number of customers in each KMeans cluster based on RFM analysis.")
fig3 = px.bar(customer_segments, x='Cluster', y='Count', title="Customer Segments (KMeans)")
st.plotly_chart(fig3, use_container_width=True)

# --- 7. Personalized Recommendations ---
st.subheader("4️⃣ Personalized Recommendations")
st.markdown("Select a customer ID to get top 5 product recommendations based on purchase history.")

available_ids = sorted(df['CustomerID'].unique())
user_id = st.selectbox("Select Customer ID", available_ids)

def recommend_collaborative(user_id, n=5):
    return user_products.get(user_id, df['Description'].value_counts().index[:n].tolist())

if st.button("Get Recommendations"):
    recs = recommend_collaborative(user_id, n=50)  # show up to 50 in scrollable way
    st.write("Recommended Products:")
    st.dataframe(pd.DataFrame(recs, columns=["Product Name"]), height=400)