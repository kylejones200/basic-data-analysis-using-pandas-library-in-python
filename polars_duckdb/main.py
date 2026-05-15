#!/usr/bin/env python3
"""Basic data analysis — Polars + DuckDB rewrite of ../main.py"""

import argparse
import yaml
import logging
import numpy as np
import polars as pl
from pathlib import Path

from core import load_data, calculate_summary_statistics, plot_data_distribution

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def load_config(config_path: Path = None) -> dict:
    if config_path is None:
        config_path = Path(__file__).parent.parent / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Basic data analysis — Polars + DuckDB")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--data-path", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    config = load_config(args.config)
    output_dir = Path(args.output_dir) if args.output_dir else Path(config["output"]["figures_dir"])
    output_dir.mkdir(exist_ok=True)

    if args.data_path and args.data_path.exists():
        df = load_data(args.data_path)
    elif config["data"]["generate_synthetic"]:
        rng = np.random.default_rng(config["data"]["seed"])
        n = config["data"]["n_rows"]
        df = pl.DataFrame({
            "id": list(range(n)),
            "value1": rng.normal(100, 15, n).tolist(),
            "value2": rng.exponential(2, n).tolist(),
            "category": rng.choice(["A", "B", "C"], n).tolist(),
        })
    else:
        raise ValueError("No data source specified")

    logging.info(f"Shape: {df.shape}")
    logging.info(f"Schema: {df.schema}")

    stats = calculate_summary_statistics(df)
    logging.info(f"Memory: {stats['memory_bytes'] / 1024**2:.2f} MB")
    logging.info(f"Null counts:\n{stats['null_counts']}")
    if stats["aggregates"] is not None:
        logging.info(f"Aggregates:\n{stats['aggregates']}")

    for col in df.columns:
        plot_data_distribution(df, col, f"Distribution of {col}",
                               output_dir / f"distribution_{col}.png")

    logging.info(f"Analysis complete. Figures saved to {output_dir}")


if __name__ == "__main__":
    main()
