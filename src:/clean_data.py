from pathlib import Path
import pandas as pd

# Path to your raw data file
sample_data = Path("data/raw/sample_data.csv")

# Read the raw file
df = pd.read_csv(sample_data)

# Show the first few rows
print(df.head())