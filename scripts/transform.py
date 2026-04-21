# scripts/transform.py

import os
import pandas as pd

RAW_DIR = "data/raw"
CLEAN_DIR = "data/clean"


def clean_dataframe(df):
    # === DROP NULLS ===
    df = df.dropna()

    # === STANDARDIZE TEXT ===
    df["anime"] = df["anime"].str.title()
    df["song"] = df["song"].str.title()
    df["type"] = df["type"].str.title()

    # === FIX TYPE VALUES ===
    df["type"] = df["type"].replace({
        "Op": "Opening",
        "Ed": "Ending"
    })

    # === CONVERT TYPES ===
    df["year"] = df["year"].astype(int)
    df["views"] = df["views"].astype(int)
    df["rating"] = df["rating"].astype(float)

    # === REMOVE DUPLICATES ===
    df = df.drop_duplicates()

    return df


def process_file(file_path, output_path):
    df = pd.read_csv(file_path)
    df_clean = clean_dataframe(df)
    df_clean.to_csv(output_path, index=False)


def main():
    os.makedirs(CLEAN_DIR, exist_ok=True)

    for file_name in os.listdir(RAW_DIR):
        if file_name.endswith(".csv"):
            input_path = os.path.join(RAW_DIR, file_name)
            output_path = os.path.join(CLEAN_DIR, file_name)

            process_file(input_path, output_path)
            print(f"Processed: {file_name}")


if __name__ == "__main__":
    main()