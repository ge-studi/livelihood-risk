from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

class Household(BaseModel):
    income: float
    shocks: int
    health_access: float
    asset_index: float
    education_level: int

# Optional: Add scaling info (adjust based on how model was trained)
# For example, if income was normalized between 0 and 1:
MAX_INCOME = 10000  # replace with max income used in training

@app.post("/predict")
def predict(h: Household):
    # Scale income to 0-1
    income_scaled = h.income / MAX_INCOME
    
    # Prepare input for model
    X = np.array([[income_scaled, h.shocks, h.health_access, h.asset_index, h.education_level]])
    
    # Predict vulnerability score
    y_pred = model.predict(X)[0]
    
    # Map numeric score to friendly text
    score = int(y_pred)
    if score >= 3:
        risk_level = "High"
    elif score == 2:
        risk_level = "Medium"
    else:
        risk_level = "Low"
    
    return {
        "vulnerability_score": score,
        "risk_level": risk_level,
        "message": {
            "Low": "This household is relatively secure at the moment.",
            "Medium": "This household may require monitoring or targeted support.",
            "High": "This household may need immediate support or intervention."
        }[risk_level]
    }
