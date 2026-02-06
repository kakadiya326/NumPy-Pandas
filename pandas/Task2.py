# 📝 PRACTICE TASKS (IMPORTANT 💪)
# Find total missing values per column
# Fill missing age with median
# Replace NA in Marks with average
# Remove duplicate records
# Convert all column names to lowercase

import pandas as pd

try:
    # Load CSV with custom NA values
    df = pd.read_csv(
        "students_messy.csv",
        na_values=["NA", " ", "", "NaN"]
    )

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Convert columns to numeric
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["marks"] = pd.to_numeric(df["marks"], errors="coerce")

    # Total missing values per column
    print("Missing values per column:")
    print(df.isna().sum())

    # Fill missing age with median
    df["age"] = df["age"].fillna(df["age"].median())

    # Replace NA in marks with average
    df["marks"] = df["marks"].fillna(df["marks"].mean())

    # Remove duplicate records
    df = df.drop_duplicates()

    print("\nCleaned DataFrame:")
    print(df)

except Exception as e:
    print("Error:", e)

