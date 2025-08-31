import streamlit as st
import requests

st.title("Livelihood Risk Predictor")

income = st.number_input("Income")
shocks = st.slider("Shocks", 0, 5)
health = st.slider("Health Access", 0.0, 1.0)
asset = st.slider("Asset Index", 0.0, 1.0)
edu = st.selectbox("Education Level", [0, 1, 2, 3, 4])

# Run prediction only on button click
if st.button("Predict"):
    try:
        res = requests.post(
            "https://livelihood-risk.onrender.com/predict",
            json={
                "income": income,
                "shocks": shocks,
                "health_access": health,
                "asset_index": asset,
                "education_level": edu
            },
            timeout=20  # add timeout in case API is slow
        )

        if res.status_code == 200:
            response = res.json()
            st.success(f"Predicted Vulnerability Score: {response['vulnerability_score']}")
        else:
            st.error(f"Failed with status code: {res.status_code}")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")
