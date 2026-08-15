import os
import streamlit as st
import requests

st.set_page_config(page_title="SuperKart Sales Forecast", page_icon="📈")
st.title("SuperKart Sales Forecast")
st.caption("Predict product-store sales using the tuned Random Forest model.")

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://YOUR-HF-USERNAME-superkart-sales-forecast-backend.hf.space"
).rstrip("/")

Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66, step=0.1)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ['Low Sugar', 'No Sugar', 'Regular'])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.0, value=0.06, step=0.01, format="%.3f")
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=146.74, step=1.0)
Store_Size = st.selectbox("Store Size", ['High', 'Medium', 'Small'])
Store_Location_City_Type = st.selectbox("Store Location City Type", ['Tier 1', 'Tier 2', 'Tier 3'])
Store_Type = st.selectbox("Store Type", ['Departmental Store', 'Food Mart', 'Supermarket Type1', 'Supermarket Type2'])
Product_Id_char = st.selectbox("Product ID Prefix", ['DR', 'FD', 'NC'])
Store_Age_Years = st.number_input("Store Age (Years)", min_value=0, value=16, step=1)
Product_Type_Category = st.selectbox("Product Type Category", ['Non Perishables', 'Perishables'])

payload = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

if st.button("Predict Sales", type="primary"):
    try:
        response = requests.post(f"{BACKEND_URL}/v1/predict", json=payload, timeout=30)
        response.raise_for_status()
        predicted_sales = response.json()["Sales"]
        st.success(f"Predicted Product Store Sales Total: {predicted_sales:,.2f}")
    except Exception as exc:
        st.error(f"Prediction request failed: {exc}")
