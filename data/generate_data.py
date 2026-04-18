import pandas as pd
import numpy as np
import os

# Ensure folder exists
os.makedirs("data", exist_ok=True)

# Create date range
dates = pd.date_range(start="2023-01-01", periods=365)

# Generate data
df = pd.DataFrame({
    "date": dates,
    "qty_sold": np.random.poisson(lam=20, size=len(dates))
})

# Check before saving
print(df.head())

# Save file
file_path = "data/retail_data.csv"
df.to_csv(file_path, index=False)

# Confirm saved
print(f"Dataset saved at: {file_path}")
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")