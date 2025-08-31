# dashboard/streamlit_app.py
import streamlit as st
import requests

st.title("Livelihood Risk Predictor")

income = st.number_input("Income")
shocks = st.slider("Shocks", 0, 5)
health = st.slider("Health Access", 0.0, 1.0)
asset = st.slider("Asset Index", 0.0, 1.0)
edu = st.selectbox("Education Level", [0, 1, 2, 3, 4])

res = requests.post("https://livelihood-risk.onrender.com/predict", json={
    "income": income,
    "shocks": shocks,
    "health_access": health,
    "asset_index": asset,
    "education_level": edu
})

    if res.status_code == 200:
        response = res.json()
        st.write("Predicted Score:", response["vulnerability_score"])
    else:
        st.error("Failed to get prediction. Check API.")
