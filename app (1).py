import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# --- Title ---
st.title("💼 Business Profit Prediction App")

st.write("""
This simple app predicts business profits based on spending on R&D, Administration, and Marketing.
""")

# --- Sample data upload or use built-in data ---
st.sidebar.header("Upload Your Data (optional)")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file with R&D Spend, Administration, Marketing Spend, Profit", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
else:
    # Example data
    data = pd.DataFrame({
        "R&D Spend": [165349.20, 162597.70, 153441.51, 144372.41, 142107.34],
        "Administration": [136897.80, 151377.59, 101145.55, 118671.85, 91391.77],
        "Marketing Spend": [471784.10, 443898.53, 407934.54, 383199.62, 366168.42],
        "Profit": [192261.83, 191792.06, 191050.39, 182901.99, 166187.94]
    })

st.subheader("📊 Data Preview")
st.write(data.head())

# --- ML model ---
X = data[["R&D Spend", "Administration", "Marketing Spend"]]
y = data["Profit"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# --- User Input ---
st.sidebar.header("Input New Business Data")
rd = st.sidebar.number_input("R&D Spend", 0.0, 1000000.0, 100000.0)
admin = st.sidebar.number_input("Administration", 0.0, 1000000.0, 50000.0)
market = st.sidebar.number_input("Marketing Spend", 0.0, 1000000.0, 200000.0)

# --- Prediction ---
input_data = pd.DataFrame({"R&D Spend": [rd], "Administration": [admin], "Marketing Spend": [market]})
prediction = model.predict(input_data)[0]

st.subheader("💰 Predicted Profit:")
st.write(f"${prediction:,.2f}")

# --- Model performance ---
y_pred = model.predict(X_test)
st.sidebar.write(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
st.sidebar.write(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
