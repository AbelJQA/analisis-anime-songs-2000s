# Anime Music Data Pipeline

## Overview

This project simulates a scalable data engineering pipeline for processing anime music data, inspired by series such as Naruto and Bleach. The goal is to demonstrate how data flows through different stages of a typical data pipeline: ingestion, transformation, and loading.

The pipeline processes daily batch data, introduces realistic data quality issues, and produces a clean dataset ready for analytics.

---

## Architecture

The pipeline follows a layered data architecture:

* Raw Layer: Stores ingested data as-is
* Clean Layer: Contains cleaned and standardized data
* Analytics Layer: Final dataset enriched with metrics

```
project/
  data/
    raw/
    clean/
    analytics/
  scripts/
```

---

## Data Generation

Data is synthetically generated to simulate real-world scenarios. Each day produces a new dataset containing:

* Anime title
* Song name
* Year
* Type (Opening / Ending)
* Views
* Rating

The dataset includes realistic issues such as:

* Missing values
* Inconsistent text formatting
* Random variations in data volume

---

## Pipeline Steps

### 1. Ingestion

Script: `ingest.py`

* Generates daily CSV files
* Stores them in the raw layer
* Simulates batch data arrival

---

### 2. Transformation

Script: `transform.py`

* Removes null values
* Standardizes text fields
* Fixes inconsistent categories
* Removes duplicates

---

### 3. Load / Analytics

Script: `load.py`

* Combines all cleaned datasets
* Adds date metadata
* Creates derived metrics:

  * Engagement score
  * Popularity categories

---

### 4. Pipeline Orchestration

Script: `pipeline.py`

Runs the full pipeline in sequence:

1. Ingestion
2. Transformation
3. Load

---

## How to Run

Run the full pipeline:

```
python scripts/pipeline.py
```

---

## Output

Final dataset is stored in:

```
data/analytics/final_dataset.csv
```

---

## Key Features

* Modular pipeline design
* Batch processing simulation
* Layered data architecture
* Synthetic data with realistic issues
* Scalable structure for future improvements

---

## Future Improvements

* Incremental processing
* Database integration (SQLite or PostgreSQL)
* Workflow orchestration (Airflow)
* Cloud storage integration
* Data validation and logging

---

## Purpose

This project is designed as a beginner-friendly yet scalable data engineering project, focusing on core concepts rather than complex infrastructure.
