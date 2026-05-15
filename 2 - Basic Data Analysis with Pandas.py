"""Generated from Jupyter notebook: Summary

Magics and shell lines are commented out. Run with a normal Python interpreter."""


# --- code cell ---

# installing the libraries we need
# ! pip install -r requirements.txt  # Jupyter-only


# --- code cell ---

import pandas as pd


def main():
    # %matplotlib inline  # Jupyter-only


    # --- code cell ---

    # Read data into Python from .txt
    sales = pd.read_csv("data/sales_fake.csv")


    # --- code cell ---

    # View the first 10 rows of the dataframe (see also: tail)
    sales.head(10)


    # --- code cell ---

    ### CODE FOR ABOVE EXERCISE ###


    # --- code cell ---

    # Select just a single column (i.e. Series object) from a dataframe:
    sales["units"]


    # --- code cell ---

    # The above series isn't very useful by itself, since we lose the date information.  To select a subset of columns, pass in a list of columns:
    col_list = ["order_day", "gl", "ops"]
    sales[col_list].head()

    # Or equivalently:
    sales[["order_day", "gl", "ops"]].head()


    # --- code cell ---

    # What are all the unique product families? use unique() on a single series:
    sales["product_family"].unique()


    # --- code cell ---

    # Or get the count of observations from each product family.  Note that the .value_counts() method only works if applied to a Series - not a DataFrame.
    # What happens if you try to call .value_counts() on a DataFrame?
    sales["product_family"].value_counts()


    # --- code cell ---

    # Print the total sales for the year.  The .sum() method works on both Series and DataFrames.
    sales["ops"].sum()


    # --- code cell ---

    # Operations on the series that make up a dataframe generally work as you'd expect.

    # E.g. add a column for country
    sales["country"] = "US"

    sales.head()


    # --- code cell ---

    # Adding calculated columns is easy, too.  First, calculate the ASP and print the results:
    sales["ops"] / sales["units"]


    # --- duplicate code cell omitted (identical to earlier cell) ---


    # --- code cell ---

    # Filter only for the pantry GL and name this view pantry:
    pantry = sales.loc[sales["gl"] == "Pantry"]
    pantry.head()


    # --- code cell ---

    # to add multiple conditions, wrap each condition in () and combine them together with &

    sales.loc[(sales["order_day"] == "7/24/20") & (sales["gl"] == "Apparel")]


    # --- duplicate code cell omitted (identical to earlier cell) ---


    # --- code cell ---

    # In the background, Pandas uses a Python package called matplotlib to make plotting convenient.
    # Since our toys df is indexed on date, Pandas automatically treats date as the x-axis.

    toys = sales[sales["gl"] == "Toys"].copy()
    toys.set_index("order_day", inplace=True)
    toys["ops"].plot()


    # --- duplicate code cell omitted (identical to earlier cell) ---


    # --- code cell ---

    # Or we can plot multiple metrics with a shared axis using subplots=True.
    # With a single line of code, Pandas can create detailed visualizations
    toys["asp"] = toys["ops"] / toys["units"]
    toys[["units", "ops", "asp"]].plot(subplots=True)


    # --- code cell ---

    # Histograms are simple to create

    toys["units"].hist(bins=20)


    # --- code cell ---

    # If you want to export a DataFrame back to a text file, the syntax to do this is similar to pd.read_csv().
    # First, define the path / location where you want the file to be saved (including the filename):

    path_to_save_data = "data/sales_fake_output.csv"

    sales.to_csv(path_to_save_data, index=False)


    # --- code cell ---

    # Sometimes you might want to quickly look at the data in Excel.
    # Add it to the clipboard and paste it wherever you want!

    sales.to_clipboard()


    # --- code cell ---

    # First read in the data
    sales = pd.read_csv("data/sales_fake.csv")


if __name__ == "__main__":
    main()
