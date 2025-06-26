# clean_data.py
import pandas as pd

# Read simulated data
df = pd.read_csv("data/fetched_data.csv")

df.dropna(inplace=True)
df = df[df['income'] > 0]

# Save cleaned version
df.to_csv("data/cleaned_data.csv", index=False)

