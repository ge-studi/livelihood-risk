# fake_api.py
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/get_data")
def get_data():
    # simulate 10 household records
    data = []
    for _ in range(500):
        data.append({
            "income": round(random.uniform(500, 4000), 2),
            "shocks": random.randint(0, 5),
            "health_access": round(random.uniform(0, 1), 2),
            "asset_index": round(random.uniform(0, 1), 2),
            "education_level": random.randint(0, 4),
            "high_vulnerability": random.choice([0, 1])
        })
    return data
