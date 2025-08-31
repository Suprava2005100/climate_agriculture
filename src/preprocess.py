import pandas as pd

# 1. Load dataset (make sure file name matches your CSV in raw/)
df = pd.read_csv("../raw/climate_change_agriculture.csv")

# 2. Show info before cleaning
print("Before cleaning:")
print(df.info())
print(df.head())

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Handle missing values
df = df.fillna(df.mean(numeric_only=True))  # fill numbers with mean
df = df.fillna("Unknown")  # fill text with 'Unknown'

# 5. Save cleaned data
df.to_csv("../data/preprocessed.csv", index=False)

print("✅ Preprocessing complete. File saved in data/preprocessed.csv")
