import joblib
import pandas as pd
from flask import Flask, request, jsonify

superkart_api = Flask("superkart_sales_forecast")
model = joblib.load("superkart_sales_model.joblib")

@superkart_api.get("/")
def home():
    return "SuperKart Sales Forecast API is running."

@superkart_api.get("/health")
def health():
    return jsonify({"status": "ok"})

@superkart_api.post("/v1/predict")
def predict_sales():
    data = request.get_json(force=True)

    required = [
        "Product_Weight",
        "Product_Sugar_Content",
        "Product_Allocated_Area",
        "Product_MRP",
        "Store_Size",
        "Store_Location_City_Type",
        "Store_Type",
        "Product_Id_char",
        "Store_Age_Years",
        "Product_Type_Category",
    ]
    missing = [x for x in required if x not in data]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    sample = {field: data[field] for field in required}
    prediction = float(model.predict(pd.DataFrame([sample]))[0])
    return jsonify({"Sales": prediction})

if __name__ == "__main__":
    superkart_api.run(host="0.0.0.0", port=7860)
