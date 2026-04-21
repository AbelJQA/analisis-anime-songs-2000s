# scripts/ingest.py

import os
import random
from datetime import datetime, timedelta

# === CONFIG ===
OUTPUT_DIR = "data/raw"
NUM_DAYS = 5
MIN_RECORDS = 20
MAX_RECORDS = 40

ANIMES = ["Naruto", "Bleach", "One Piece"]
SONGS = ["Blue Bird", "Asterisk", "We Are", "Go!!!", "Rolling Star"]
TYPES = ["Opening", "Ending"]


def generate_random_date(start_date, days_offset):
    return start_date + timedelta(days=days_offset)


def introduce_noise(value):
    """Introduce small random errors to simulate real-world data."""
    if random.random() < 0.1:
        return None  # missing value
    if isinstance(value, str) and random.random() < 0.1:
        return value.lower()  # inconsistent casing
    return value


def generate_record():
    anime = random.choice(ANIMES)
    song = random.choice(SONGS)
    year = random.randint(2000, 2010)
    song_type = random.choice(TYPES)
    views = random.randint(10000, 1000000)
    rating = round(random.uniform(1, 10), 1)

    return [
        introduce_noise(anime),
        introduce_noise(song),
        year,
        introduce_noise(song_type),
        introduce_noise(views),
        introduce_noise(rating),
    ]


def save_csv(file_path, records):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("anime,song,year,type,views,rating\n")
        for r in records:
            row = ",".join("" if v is None else str(v) for v in r)
            f.write(row + "\n")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    start_date = datetime(2026, 4, 1)

    for i in range(NUM_DAYS):
        date = generate_random_date(start_date, i)
        filename = date.strftime("%Y-%m-%d") + ".csv"
        file_path = os.path.join(OUTPUT_DIR, filename)

        num_records = random.randint(MIN_RECORDS, MAX_RECORDS)
        records = [generate_record() for _ in range(num_records)]

        save_csv(file_path, records)
        print(f"Generated: {file_path} with {num_records} records")


if __name__ == "__main__":
    main()