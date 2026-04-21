# scripts/load.py

import os
import pandas as pd

CLEAN_DIR = "data/clean"
ANALYTICS_DIR = "data/analytics"


def load_all_data():
    dfs = []

    for file_name in os.listdir(CLEAN_DIR):
        if file_name.endswith(".csv"):
            file_path = os.path.join(CLEAN_DIR, file_name)
            df = pd.read_csv(file_path)

            # === ADD DATE COLUMN FROM FILENAME ===
            df["date"] = file_name.replace(".csv", "")

            dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def create_metrics(df):
    # === ENGAGEMENT SCORE ===
    df["engagement_score"] = df["views"] * df["rating"]

    # === POPULARITY CATEGORY ===
    df["popularity"] = pd.cut(
        df["views"],
        bins=[0, 100000, 500000, 1000000],
        labels=["Low", "Medium", "High"]
    )

    return df


def main():
    os.makedirs(ANALYTICS_DIR, exist_ok=True)

    df = load_all_data()
    df = create_metrics(df)

    output_path = os.path.join(ANALYTICS_DIR, "final_dataset.csv")
    df.to_csv(output_path, index=False)

    print(f"Final dataset created at: {output_path}")


if __name__ == "__main__":
    main()