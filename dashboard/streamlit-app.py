import streamlit as st

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

def simple_risk_predict(income, shocks, health, asset, edu):
    score = 0
    if income < 2000: score += 1
    if shocks > 2: score += 1
    if health < 0.5: score += 1
    if asset < 0.5: score += 1
    if edu < 2: score += 1

    if score >= 4:
        return "High", score
    elif score >= 2:
        return "Medium", score
    else:
        return "Low", score

if st.button("Predict"):
    risk_level, score = simple_risk_predict(income, shocks, health, asset, edu)
    st.success(f"Predicted Vulnerability: **{risk_level}** (Score: {score})")

    # Simple guidance
    if risk_level == "High":
        st.info("This household may need immediate support or intervention.")
    elif risk_level == "Medium":
        st.info("This household may require monitoring or targeted support.")
    else:
        st.info("This household is relatively secure at the moment.")
