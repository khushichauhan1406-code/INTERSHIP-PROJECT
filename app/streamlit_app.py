import streamlit as st
import pandas as pd

# =====================================
# PAGE SETTINGS
# =====================================

st.set_page_config(
    page_title="RetailPulse Dashboard",
    layout="centered"
)

# =====================================
# LOAD DATA
# =====================================

data = pd.read_csv("data/RetailPulse.csv")

# =====================================
# TITLE
# =====================================

st.title(" RetailPulse Dashboard")

st.subheader(
    "AI-Powered Customer Analytics & Demand Forecasting Platform"
)

# =====================================
# SHOW DATASET
# =====================================

st.header("Retail Dataset")

if st.checkbox("Show Dataset"):
    st.write(data)

# =====================================
# BUSINESS OVERVIEW
# =====================================

st.header("Business Overview")

col1, col2, col3 = st.columns(3)

with col1:
    total_sales = data["Total Amount"].sum()

    st.metric(
        "Total Sales",
        f"₹ {total_sales}"
    )

with col2:
    total_customers = data["Customer ID"].nunique()

    st.metric(
        "Total Customers",
        total_customers
    )

with col3:
    avg_sales = round(
        data["Total Amount"].mean(),
        2
    )

    st.metric(
        "Average Sales",
        f"₹ {avg_sales}"
    )

# =====================================
# CATEGORY SALES
# =====================================

st.header("Category Wise Revenue")

category_sales = data.groupby(
    "Product Category"
)["Total Amount"].sum()

st.bar_chart(category_sales)

# =====================================
# AGE DISTRIBUTION
# =====================================

st.header("Customer Age Distribution")

age_data = data.groupby(
    "Age"
)["Customer ID"].count()

st.line_chart(age_data)

# =====================================
# SALES TREND
# =====================================

st.header("Sales Trend")

sales_trend = data.groupby(
    "Quantity"
)["Total Amount"].mean()

st.area_chart(sales_trend)

# =====================================
# TOP CUSTOMERS
# =====================================

st.header("Top 10 Customers")

top_customers = data.groupby(
    "Customer ID"
)["Total Amount"].sum()

top_customers = top_customers.sort_values(
    ascending=False
).head(10)

st.bar_chart(top_customers)

st.write(top_customers)

# =====================================
# SALES PREDICTION
# =====================================

st.header("Predict Future Sales")

quantity = st.number_input(
    "Enter Quantity",
    min_value=1,
    value=1
)

price = st.number_input(
    "Enter Price Per Unit",
    min_value=1,
    value=100
)

age = st.number_input(
    "Enter Customer Age",
    min_value=10,
    value=25
)

if st.button("Predict Sales"):

    predicted_sales = quantity * price

    st.success(
        f"Predicted Sales = ₹ {predicted_sales}"
    )

# =====================================
# CUSTOMER TYPE PREDICTION
# =====================================

st.header("Customer Type Prediction")

if st.button("Check Customer Type"):

    total_purchase = quantity * price

    if total_purchase >= 1000:
        st.success("Premium Customer")
    else:
        st.warning("Regular Customer")
