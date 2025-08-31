import streamlit as st
import requests

# Title
st.title("Livelihood Risk Predictor")

# Input fields
income = st.number_input("Income", min_value=0.0, step=100.0, format="%.2f")
shocks = st.slider("Shocks", 0, 5)
health = st.slider("Health Access", 0.0, 1.0)
asset = st.slider("Asset Index", 0.0, 1.0)
edu = st.selectbox("Education Level", [0, 1, 2, 3, 4])

# API endpoint
API_URL = "https://livelihood-risk.onrender.com"

# Predict button
if st.button("Predict"):
    payload = {
        "income": income,
        "shocks": shocks,
        "health_access": health,
        "asset_index": asset,
        "education_level": edu
    }

    try:
        res = requests.post(API_URL, json=payload, timeout=20)

        if res.status_code == 200:
            response = res.json()
            score = response.get("vulnerability_score")
            st.success(f"Predicted Vulnerability Score: {score}")
        elif res.status_code == 404:
            st.error("API endpoint not found. Check your FastAPI deployment URL.")
        else:
            st.error(f"Failed with status code: {res.status_code}\nResponse: {res.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {e}")
