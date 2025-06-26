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
    
@app.post("/predict")
def predict(h: Household):
    X = np.array([[h.income, h.shocks, h.health_access, h.asset_index, h.education_level]])
    y_pred = model.predict(X)[0]
    return {"vulnerability_score": int(y_pred)}
