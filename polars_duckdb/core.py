"""Basic data analysis using Polars and DuckDB."""

import duckdb
import polars as pl
import matplotlib.pyplot as plt
import logging
from pathlib import Path
from typing import Dict

logging.basicConfig(level=logging.INFO, format='%(message)s')


def load_data(file_path: Path) -> pl.DataFrame:
    return pl.read_csv(file_path)


def calculate_summary_statistics(df: pl.DataFrame) -> Dict:
    numeric_cols = [c for c, t in zip(df.columns, df.dtypes) if t.is_numeric()]

    if numeric_cols:
        per_col = ", ".join(
            f"AVG({c}) AS mean_{c}, STDDEV_SAMP({c}) AS std_{c}, "
            f"MIN({c}) AS min_{c}, MAX({c}) AS max_{c}"
            for c in numeric_cols
        )
        aggregates = duckdb.sql(f"SELECT COUNT(*) AS n_rows, {per_col} FROM df").pl()
    else:
        aggregates = None

    return {
        "shape": df.shape,
        "schema": df.schema,
        "null_counts": df.null_count(),
        "memory_bytes": df.estimated_size(),
        "aggregates": aggregates,
    }


def plot_data_distribution(df: pl.DataFrame, column: str, title: str, output_path: Path):
    fig, ax = plt.subplots(figsize=(10, 6))
    col = df[column]

    if col.dtype.is_numeric():
        ax.hist(col.drop_nulls().to_numpy(), bins=30, color="#4A90A4", alpha=0.7, edgecolor='none')
    else:
        counts = (
            duckdb.sql(
                f'SELECT "{column}", COUNT(*) AS n FROM df GROUP BY "{column}" ORDER BY n DESC LIMIT 10'
            ).pl()
        )
        ax.bar(counts[column].to_list(), counts["n"].to_list(), color="#4A90A4", alpha=0.7, edgecolor='none')
        ax.tick_params(axis='x', rotation=45)

    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(output_path, dpi=100, bbox_inches="tight")
    plt.close()
