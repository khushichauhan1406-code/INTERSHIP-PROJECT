import streamlit as st
import pandas as pd
import pickle

# =====================================
# LOAD DATA
# =====================================

data = pd.read_csv(
    r"data\RetailPulse.csv")

# =====================================
# LOAD MODELS
# =====================================

sales_model = pickle.load(
    open(
        r"C:\Users\LENOVO\OneDrive\Desktop\INTERSHIP PROJECT\models\sales_model.pkl",
        "rb"
    )
)

customer_model = pickle.load(
    open(
        r"C:\Users\LENOVO\OneDrive\Desktop\INTERSHIP PROJECT\models\customer_model.pkl",
        "rb"
    )
)

# =====================================
# TITLE
# =====================================

st.title("RetailPulse Dashboard")

st.subheader(
    "Smart Retail Analytics System"
)

# =====================================
# DATASET
# =====================================

if st.checkbox("Show Dataset"):
    st.write(data)

# =====================================
# KPI SECTION
# =====================================

st.header("Business Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sales",
        f"₹ {data['Total Amount'].sum()}"
    )

with col2:
    st.metric(
        "Total Customers",
        data['Customer ID'].nunique()
    )

with col3:
    st.metric(
        "Average Sales",
        round(data['Total Amount'].mean(), 2)
    )

# =====================================
# CATEGORY SALES GRAPH
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

age_graph = data.groupby(
    "Age"
)["Customer ID"].count()

st.line_chart(age_graph)

# =====================================
# MONTHLY SALES TREND
# =====================================

st.header("Sales Trend")

sales_trend = data.groupby(
    "Quantity"
)["Total Amount"].mean()

st.area_chart(sales_trend)

# =====================================
# SALES PREDICTION
# =====================================

st.header("Predict Sales")

quantity = st.number_input(
    "Enter Quantity",
    min_value=1
)

price = st.number_input(
    "Enter Price Per Unit",
    min_value=1
)

age = st.number_input(
    "Enter Customer Age",
    min_value=10
)

if st.button("Predict Future Sales"):

    prediction = sales_model.predict(
        [[quantity, price, age]]
    )

    st.success(
        f"Predicted Sales = ₹ {prediction[0]}"
    )

# =====================================
# PREMIUM CUSTOMER PREDICTION
# =====================================

st.header("Premium Customer Prediction")

if st.button("Check Customer Type"):

    result = customer_model.predict(
        [[quantity, price, age]]
    )

    if result[0] == 1:
        st.success("Premium Customer")
    else:
        st.warning("Regular Customer")

# =====================================
# TOP 10 CUSTOMERS
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