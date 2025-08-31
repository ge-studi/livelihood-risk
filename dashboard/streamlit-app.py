import streamlit as st
import requests

st.title("Livelihood Risk Predictor")

st.markdown(
    "This tool predicts the **vulnerability of a household** based on simple inputs. "
    "Just enter the information below and click Predict."
)

# User Inputs
income = st.number_input("Monthly Household Income (in Rupees)", min_value=0.0, step=100.0, format="%.2f")
shocks = st.slider("Number of Recent Economic/Health Shocks (0 = none, 5 = many)", 0, 5)
health = st.slider("Access to Healthcare (0 = poor, 1 = excellent)", 0.0, 1.0)
asset = st.slider("Household Asset Index (0 = low, 1 = high)", 0.0, 1.0)
edu = st.selectbox("Education Level of Household Head (0 = None, 4 = College+)", [0, 1, 2, 3, 4])

API_URL = "https://livelihood-risk.onrender.com/predict"

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
            score = res.json().get("vulnerability_score")
            
            # Plain language explanation
            if score >= 3:
                risk_level = "High"
            elif score == 2:
                risk_level = "Medium"
            else:
                risk_level = "Low"
            
            st.success(f"Predicted Vulnerability: **{risk_level}** (Score: {score})")
            
            # Optional: Simple guidance
            if risk_level == "High":
                st.info("This household may need immediate support or intervention.")
            elif risk_level == "Medium":
                st.info("This household may require monitoring or targeted support.")
            else:
                st.info("This household is relatively secure at the moment.")

        elif res.status_code == 404:
            st.error("API endpoint not found. Check the URL.")
        else:
            st.error(f"Error {res.status_code}: {res.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to API: {e}")
