# fetch_data.py
import requests
import pandas as pd

print("📥 Fetching data from fake API...")

try:
    response = requests.get("http://localhost:8000/get_data")
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list):
        df = pd.DataFrame(data)
        df.to_csv("data/raw_data.csv", index=False)
        print("Data saved to data/raw_data.csv")
    else:
        raise ValueError("Unexpected data format: Expected a list of dictionaries")

except Exception as e:
    print("Failed to fetch data:", e)
