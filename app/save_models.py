import pandas as pd
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

# =====================================
# LOAD DATASET
# =====================================

data = pd.read_csv(
    r"C:\Users\LENOVO\OneDrive\Desktop\INTERSHIP PROJECT\data\RetailPulse.csv"
)

# =====================================
# SALES PREDICTION MODEL
# =====================================

X = data[["Quantity", "Price per Unit", "Age"]]

y = data["Total Amount"]

sales_model = LinearRegression()

sales_model.fit(X, y)

pickle.dump(
    sales_model,
    open(
        r"C:\Users\LENOVO\OneDrive\Desktop\INTERSHIP PROJECT\models\sales_model.pkl",
        "wb"
    )
)

print("Sales Model Saved")

# =====================================
# CUSTOMER TYPE MODEL
# =====================================

# Premium customer condition

data["Premium Customer"] = data[
    "Total Amount"
].apply(
    lambda x: 1 if x > 1000 else 0
)

X_customer = data[[
    "Quantity",
    "Price per Unit",
    "Age"
]]

y_customer = data["Premium Customer"]

customer_model = DecisionTreeClassifier()

customer_model.fit(X_customer, y_customer)

pickle.dump(
    customer_model,
    open(
        r"C:\Users\LENOVO\OneDrive\Desktop\INTERSHIP PROJECT\models\customer_model.pkl",
        "wb"
    )
)

print("Customer Model Saved")