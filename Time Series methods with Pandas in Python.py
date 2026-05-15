"""Generated from Jupyter notebook: Time Series methods with Pandas in Python

Magics and shell lines are commented out. Run with a normal Python interpreter."""


# --- code cell ---

import numpy as np
import pandas as pd


def main():
    # Create a simple time series
    date_range = pd.date_range(start="2023-01-01", periods=10, freq="D")
    data = {"value": np.arange(10)}
    df = pd.DataFrame(data, index=date_range)

    # Shift data by one day to create a lagged feature
    df["lagged_value"] = df["value"].shift(1)

    df.head()


    # --- code cell ---

    # Compute a 3-day rolling mean
    df["rolling_mean"] = df["value"].rolling(window=3).mean()

    df.head()


    # --- code cell ---

    # Compute a 3-day rolling standard deviation
    df["rolling_std"] = df["value"].rolling(window=3).std()

    df.head()


    # --- code cell ---

    # Resample daily data to weekly sums
    weekly = df.resample("W").sum()
    weekly.head()


    # --- code cell ---

    # Resample weekly data to daily, filling missing values with interpolation
    upsampled = weekly.resample("D").interpolate("linear")
    upsampled.head()


    # --- code cell ---

    # Simulate missing data
    df.loc["2023-01-05", "value"] = np.nan

    # Fill missing values with the last available value
    df["forward_fill"] = df["value"].fillna(method="ffill")

    df.head()


    # --- code cell ---

    # Fill missing values with the mean of the column
    df["mean_fill"] = df["value"].fillna(df["value"].mean())

    df.head()


    # --- code cell ---

    # Combine techniques: Shift, resample, and fill missing values
    df["weekly_sum"] = df["value"].resample("W").sum()
    df["weekly_sum_shifted"] = df["weekly_sum"].shift(1).fillna(0)
    df["weekly_avg"] = df["weekly_sum"].rolling(window=2).mean()

    df.tail()


if __name__ == "__main__":
    main()
