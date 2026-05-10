---
author: "Kyle Jones"
date_published: "April 20, 2024"
date_exported_from_medium: "November 10, 2025"
canonical_link: "https://medium.com/@kyle-t-jones/basic-data-analysis-using-pandas-library-61ed815b834a"
---

# Basic Data Analysis using Pandas Library in Python

Data analysis plays a crucial role in extracting meaningful insights from raw data, enabling informed decision-making in various fields...

### Basic Data Analysis using Pandas Library in Python
Data analysis plays a crucial role in extracting meaningful insights from raw data, enabling informed decision-making in various fields.\ The Python library that is most often used for data analysis is called Pandas (short for Panel Analysis).

Pandas is a widely used open-source library in Python that offers high-performance data manipulation and analysis capabilities. It provides easy-to-use data structures, such as DataFrame and Series, along with a rich set of functions for handling and analyzing data.

After completing this tutorial, you will know:

- How to use Pandas DataFrames to open \*.csv and \*.xlsx files
- How to apply functions to DataFrames to calcuate the mean and standard deviation
- How to make basic plots
- You will be able to confidently manipulate and analyze datasets for extracting valuable insights

Let's get started.

### Pandas basics
**Pandas** is all about **DataFrames** (df), which are analogous to tables in Excel or SQL, or to R's dataframe. Dataframes are made up of **Series** (i.e. columns) and can be manipulated with simple or complex transformations like filtering, aggregating, joining, and pivoting/unpivoting.

Pandas also integrates seamlessly with other popular libraries in the Python ecosystem, such as NumPy for numerical computations and Matplotlib for data visualization. This allows you to leverage the full power of Python for data analysis and create insightful visualizations of your data.

Whether you are dealing with small or large datasets, Pandas provides efficient and intuitive tools to explore, transform, and analyze your data. It is widely used in various domains, including finance, data science, research, and business analytics, making it an essential skill for anyone working with data in Python.

By mastering Pandas and its DataFrame functionality, you will have the ability to handle complex data analysis tasks, gain deeper insights into your data, and make data-driven decisions effectively.

So, embrace the power of Pandas and unlock the potential of your data!

#### Dataset and Columns
The "us-counties-recent.csv" dataset from the New York Times COVID-19 data repository provides recent COVID-19 data for counties in the United States. It is a valuable resource for analyzing and understanding the impact of the pandemic at a county level. The dataset includes the following columns:

1.  [**date**: The date of the recorded data.]
2.  [**county**: The name of the county.]
3.  [**state**: The name of the state.]
4.  [**fips**: The Federal Information Processing Standards (FIPS) code that uniquely identifies each county in the United States.]
5.  [**cases**: The total number of confirmed COVID-19 cases in the county up to the specified date.]
6.  [**deaths**: The total number of COVID-19 deaths in the county up to the specified date.]

These columns provide valuable information for analyzing the spread and impact of COVID-19 across different counties and states. By leveraging the Pandas library, we can easily load, manipulate, analyze, and visualize this dataset to gain insights into the trends and patterns of the pandemic at a granular level.

**Objective of the tutorial (e.g., analyzing COVID-19 data trends)**

The objective of this tutorial is to analyze COVID-19 data trends using the "us-counties-recent.csv" dataset from the New York Times. We will leverage the powerful data analysis capabilities of the Pandas library to gain insights into the spread and impact of the pandemic at a county level. By performing various data manipulation, aggregation, and visualization techniques, we aim to uncover patterns, identify hotspots, and track the progression of COVID-19 across different counties and states. Through this tutorial, you will learn how to load and preprocess the dataset, perform exploratory data analysis, calculate key statistics, create visualizations, and extract meaningful insights from the COVID-19 data.

#### Exercise: What do these DataFrame methods do? Try them out.
The .head() **method** above is just one of the many methods that can be applied to Pandas dataframes. In general, these methods return some transformation of the dataframe to which they are applied. Take a few minutes and play around with some of the methods below, using the sales dataframe.

See [https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) under "Methods" for a complete list.

Some useful methods:

.count() .describe() .info() .mean() .median() .nunique() .plot() .shift() .transpose()

Dataframes also have certain **attributes** which are accessed similarly, but without the (). What do these attributes represent?

.columns .dtypes .empty .shape .size .values

### How to Import Panda Library:
To import the Pandas library in Python, you can use the following line of code:

```python
import pandas as pd
```

This imports the Pandas library and assigns it the alias **"pd"**. Using the **"pd"** alias is a common convention in the Python community and makes it easier to reference Pandas functions and objects throughout your code. Once imported, you can access various Pandas functionalities for data manipulation, analysis, and visualization.

#### Reading file from Google Drive in Google Colab:
To read a CSV file from Google Drive in Google Colab and load it into a Pandas DataFrame, you can follow these steps:

Mount your Google Drive by running the following code in a Colab cell:

```python
from google.colab import drive
drive.mount(‘/content/drive’)
```

Mounted at /content/drive

2 --- After running the code, you will see a link. Click on the link and authenticate with your Google account to mount your Google Drive.

3 --- Once your Google Drive is mounted, you can access the files in it. Assuming the file "data/us-counties-recent.csv" is located in your Google Drive, you can read it into a Pandas DataFrame using the following code:

```python
import pandas as pd
 
 file_path = ‘/content/drive/MyDrive/KyleJonesCurrent/WriteUpContent/data/us-counties-recent.csv’
 df = pd.read_csv(file_path)
```

Make sure to update the **file_path** variable with the correct path to your CSV file.

By following these steps, you will be able to load the **"data/us-counties-recent.csv"** dataset from your Google Drive into a Pandas DataFrame in Google Colab.

Let's check if data is being retrieved from the .csv file by using 'head()' function as shown below:

``` 
df.head()
```

df.head() will fetched 5 rows from the dataset file. If you want to display a specific number of rows, you can pass an argument to the head() function. For example, to display the first 10 rows, you can use:

``` 
df.head(10)
```

This is a helpful way to quickly examine the structure and contents of your DataFrame.

We discussed the **column names** for the **COVID-19 dataset** you just loaded.

Let's talk about the structure of the **DataFrame** and **data types** too.

The **DataFrame** contains information about COVID-19 cases in various counties of the United States.

The **data types** for each column in the DataFrame can be determined using the dtypes attribute of the DataFrame. For example, you can use the following code:

``` 
df.dtypes
```

This displayed the data type of each column in the DataFrame. In the COVID-19 dataset, the **'date', 'county'**, and **'state'** columns are of type object (string), while the **'fips'** and **'deaths'** columns are of type float64 and **'cases'** column is of int64 type.

Understanding the structure, column names, and data types of the DataFrame is important as it helps you identify and work with the relevant information in your data analysis tasks.

Certainly! The 'describe()' function in Pandas provides an overview of the available statistics for the numerical columns in the DataFrame. It computes various summary statistics, including count, mean, standard deviation, minimum, quartiles, and maximum values.

To apply the 'describe()' function to your DataFrame, you can use the following code:

``` 
df.describe()
```

Here's what each statistic represents:

**count:** The number of non-null values in each column.

**mean**: The average value of each column.

**std:** The standard deviation, which measures the spread of values around the mean.

**min:** The minimum value in each column.

**25%:** The first quartile, also known as the lower quartile, representing the value below which 25% of the data falls.

**50%:** The second quartile, also known as the median, representing the value below which 50% of the data falls.

**75%:** The third quartile, also known as the upper quartile, representing the value below which 75% of the data falls.

**max:** The maximum value in each column.

### Key Difference between Panda Dataframe and Series:
In Pandas, a DataFrame and a Series are both fundamental data structures, but they have some key differences:

**Structure:** A DataFrame is a 2-dimensional tabular data structure that consists of rows and columns, similar to a table in a relational database or a spreadsheet. It can be seen as a collection of Series objects that share the same index. Each column in a DataFrame represents a Series. In contrast, a Series is a 1-dimensional labeled array-like object that can hold any data type. It has both a sequence of values and an associated index.

**Dimensions:** A DataFrame has two dimensions (rows and columns), while a Series has only one dimension (rows). A DataFrame can be thought of as a container for multiple Series objects, where each Series represents a column of data.

**Data Storage:** In terms of data storage, a DataFrame is a collection of Series objects with aligned indexes. Each column in a DataFrame is represented by a Series, where the index labels are shared. The data in a Series is stored as a one-dimensional NumPy array with an associated index.

**Operations:** Both DataFrames and Series support a wide range of operations, but the scope and behavior may differ. DataFrames provide more functionality and flexibility for working with structured, tabular data, such as filtering, aggregating, merging, and joining data from multiple columns. Series, on the other hand, are more suitable for working with a single column of data and performing operations like arithmetic calculations, statistical analysis, and data manipulation.

In summary, a DataFrame is a 2-dimensional data structure that holds multiple Series objects, while a Series is a 1-dimensional data structure representing a single column of data. DataFrames are suitable for handling complex, tabular data, whereas Series are useful for working with single-dimensional data and performing operations on individual columns.

```python
# Select just a single column (i.e. Series object) from a dataframe:
 df['fips']
```

#### Head():
\# The above series isn't very useful by itself, since we lose the date information. To select a subset of columns, pass in a list of columns:

``` 
df['deaths'].head(5)
```

#### Unique():
``` 
# What are all the unique product families? use unique() on a single series:
print(“Total number of records in county column : “,len(df[‘county’]))
print(“Name of unique records in county column : “,df[‘county’].unique())
print(“Total number of unique records in county column : “,len(df[‘county’].unique()))

Total number of records in county column : 97701
Name of unique records in county column : [‘Autauga’ ‘Baldwin’ ‘Barbour’ … ‘Uinta’ ‘Washakie’ ‘Weston’]
Total number of unique records in county column : 1932
```

#### Value_counts()
The **value_counts()** function in Pandas is used to get a count of unique values in a column of a DataFrame. It returns a Series object where the unique values in the column are the index labels, and the corresponding values are the counts of occurrences of each unique value.

This function will provide you with a count of each unique value in that column.

The **value_counts()** function is helpful for understanding the distribution of **categorical data** and identifying the most **common values** in a column. It can be used to perform exploratory data analysis and gain insights into the data.

``` 
df['cases'].value_counts()
```

#### Memory_usage()
The **memory_usage()** function in Pandas is used to determine the memory usage of each column in a DataFrame. It returns a Series object where the column names are the index labels, and the corresponding values represent the memory usage of each column in bytes.

By default, the **memory_usage()** function provides an approximation of the memory usage, which may not reflect the actual memory consumed by the data. However, by setting the deep parameter to True, you can obtain the accurate memory usage of each column, considering the underlying data types and object references.

Here's an example of how to use the **memory_usage()** function:

``` 
df.memory_usage(deep=True)
```

This will return a Series object showing the memory usage of each column in the DataFrame, considering the actual memory consumed by the data in bytes.

#### Sum():
The **sum()** function in Pandas is a method available on Series objects. It calculates and return a single value which is the sum of all the values in the Series. It is a convenient way to quickly compute the total sum of numerical data in a Series.

If the Series contains non-numeric data types, the function will attempt to perform the summation operation by converting the values to a suitable numeric representation.

This function is particularly useful when working with numeric data, such as financial data, sales figures, or any other data that can be aggregated using addition.

Here is an example of how to use the sum() function:

``` 
TotalCases = df['cases'].sum()
print(f"TotalCases : {TotalCases}")

TotalCases : 3104006437
```

The sum() function can also be applied to a subset of the Series by using boolean indexing or other filtering techniques to select specific elements before performing the summation.

Overall, the sum() function is a useful tool for quickly calculating the total sum of numerical data in a Series and is widely used in data analysis and mathematical operations.

### Filtering with row conditions:
The .loc() method in Pandas is a powerful tool for filtering DataFrames based on specific row conditions. It allows you to select rows that meet certain criteria, similar to using "if" statements in Excel's SUMIFS function or using conditions in a WHERE clause in SQL queries.

With the .loc() method, you can specify one or more conditions inside the brackets to filter the DataFrame. These conditions can be based on column values, logical operations, or a combination of both.

Here are some key points about using .loc() for filtering:

**Syntax:** The general syntax for using .loc() is df.loc\[row_condition, column_condition\], where row_condition specifies the filtering condition for rows and column_condition specifies the filtering condition for columns (optional).

**Row Condition:** The row_condition inside .loc() can be a single condition or a combination of multiple conditions using logical operators (& for "and", \| for "or", \~ for "not"). This allows you to create complex filtering expressions.

**Column Condition (optional):** The column_condition inside .loc() allows you to select specific columns based on a condition. This is optional, and if omitted, all columns will be included in the result.

**Here are some examples:**

1: Select rows where the 'state' column is 'New York':

``` 
ny_counties = df.loc[df['state'] == 'New York']
print(f"NewYork Counties : \n {ny_counties}")
```

2: Select rows where the 'cases' column is greater than 1000:

``` 
high_cases = df.loc[df['cases'] > 1000]
print(f'High Cases : \n {high_cases}')
```

3: Select rows where the 'state' column is 'California' and the 'deaths' column is greater than 100:

``` 
ca_high_deaths = df.loc[(df['state'] == 'California') & (df['deaths'] > 100)]
print(f"High Deaths : \n {ca_high_deaths}")
```

4: Select rows where the 'county' column is either 'Los Angeles' or 'San Francisco':

``` 
la_sf_counties = df.loc[df['county'].isin(['Los Angeles', 'San Francisco'])]
print(f"Los Angeles and San Francisco Counties : \n {la_sf_counties}")
```

5: Select rows where the **'cases'** column is less than or equal to 10 and update the **'deaths'** column to be 0:

``` 
low_cases = df.loc[df['cases'] <= 10]
low_cases.loc[:, 'deaths'] = 0
print(f"Low Cases : \n {low_cases}")
```

``` 
low_cases.loc[:, 'deaths'] = 0
```

These examples demonstrate how you can use the **.loc()** method to filter the DataFrame based on specific conditions and perform various operations on the filtered data.

### Examples:
1: Filter the 'us-counties-recent.csv' dataset to select rows where the 'state' column is 'California' and the 'cases' column is greater than 1000.\ 2: Create a new DataFrame called ca_high_cases containing the filtered data.\ 3: Display the first 10 rows of the ca_high_cases DataFrame.

Hint: Use the .loc() method with appropriate conditions to filter the DataFrame.

### Basic Visualization:
Pandas library can be used to perform basic visualization of data by the help of matplotlib.

```python
%matplotlib inline
import matplotlib.pyplot as plt
 
# Subset the DataFrame for a specific county
county_df = df[df['county'] == 'Los Angeles'].copy()
 
# Set the ‘date’ column as the index
county_df.set_index('date', inplace=True)
 
# Plot the daily new cases
county_df['cases'].plot()
 
# Customize the plot
plt.title('Daily New COVID-19 Cases in Los Angeles County')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
 
# Display the plot
plt.show()
```

In this example, we load the 'us-counties-recent.csv' dataset into a DataFrame called 'df'. Then, we create a subset of the DataFrame for a specific county (e.g., 'Los Angeles') and set the 'date' column as the index.

Next, we use the plot() method on the 'cases' column of the 'county_df' DataFrame to create a line plot showing the daily new COVID-19 cases in Los Angeles County over time.

We also customize the plot by adding a title, x-axis label, and y-axis label. Finally, we display the plot using plt.show().

This example demonstrates how to subset data for a specific county, set the index, and create a line plot to visualize the daily new COVID-19 cases. You can further expand on this example by exploring different columns, adding more customization options, or comparing multiple counties

### Exercise: what other kinds of plots can Pandas produce? Try making a few below.
Check out the API documentation for the pd.Series.plot method to find other allowable values of the "kind" argument:

[http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.Series.plot.html](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.Series.plot.html)

``` 
# Subset the DataFrame for a specific county
county_df = df[df['county'] == 'Los Angeles']
 
# Calculate the average cases per day and add it as a new column
county_df['avg_cases'] = county_df['cases'] / county_df['date'].nunique()
 
# Plot the units, operations, and average cases per day
county_df['cases', 'deaths', 'avg_cases']].plot(subplots=True)
 
# Customize the plot
plt.suptitle('COVID-19 Statistics in Los Angeles County')
plt.xlabel('Date')
plt.ylabel('Count')
 
# Display the plot
plt.show()
```

In this example, we calculate the average cases per day by dividing the 'cases' column by the number of unique dates in the 'date' column. We use the nunique() function to count the number of unique dates.

This example demonstrates how to calculate and plot multiple columns simultaneously, providing insights into the COVID-19 statistics in Los Angeles County. You can further customize the plot, explore different columns, or compare multiple counties by adapting the code to suit your needs.

``` 
# Histograms are simple to create
county_df['avg_cases'].hist(bins=20)
```

### Exporting Data:
If you want to export a DataFrame back to a text file, the syntax to do this is similar to pd.read_csv(). First, define the path / location where you want the file to be saved (including the filename):

``` 
path_to_save_data = '<your-path>'
df.to_csv(path_to_save_data, index=False)
```

Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).

#### Copying dataframe from panda to excel:
``` 
pip install pyperclip

# Sometimes you might want to quickly look at the data in Excel.
# Add it to the clipboard and paste it wherever you want!
 
df.to_clipboard()
df.cases.unique()
```

If you're running Python in a remote or virtual environment (such as google colab), ensure that the clipboard functionality is supported and properly configured in that environment.

### Exercises: Your turn!
Use the sales DataFrame to answer the following questions.

```python
# First read in the data
 import pandas as pd
 
 file_path = '<your-path>'
 df = pd.read_csv(file_path)
```

1\) What is the total number of cases (cases) reported in all counties?

2\) Display the top 10 rows of the dataset for the state of California.

3\) Plot a line graph showing the number of deaths (deaths) by date for a specific county.

4\) How many unique states are included in the dataset?

5\) Filter the dataset for counties in New York state. Plot a graph showing the number of cases, deaths, and hospitalizations by date for each county.

6\) Create a new dataframe called "recent_data" that contains only the rows with data from the last 7 days.\|

7\) Export the 'recent_data' dataframe to a CSV file named "us-counties-recentData.csv".

### Extensions
This section lists some ideas for extending the tutorial that you may wish to explore.

\* Describe three examples when Pandas would be better than using Excel.

\* Complete the next example that uses Pandas to import and visualize a dataset.

### Further Reading
This section provides more resources on the topic if you are looking to go deeper.

### Books
\* Python for Data Analysis, by William McKinney. [http://shop.oreilly.com/product/0636920023784.do](http://shop.oreilly.com/product/0636920023784.do)

### APIs
\* Pandas. [https://pandas.pydata.org/](https://pandas.pydata.org/)

### Additional Pandas Tutorials
\* [**Python for Quantitative Economics**](https://github.com/QuantEcon/lecture-python-programming.notebooks/blob/master/pandas.ipynb)

\* [**Intro to Pandas**](https://github.com/kthyng/python4geosciences/blob/master/materials/4_pandas.ipynb) from Python for Geosciences

### Summary
In this tutorial, you were introduced to the Pandas library. Specifically, you learned:

- How to use Pandas DataFrames to open \*.csv files
- How to apply functions to DataFrames to calculate the mean and standard deviation
- How to make basic plots

### Related Stories
- [[Getting to know Pandas for data analytics with Python](https://medium.com/@kylejones_47003/getting-to-know-pandas-for-data-analytics-with-python-7386da28dd33)]
- [[Introduction to Statistics for people who do Business Analytics](https://medium.com/@kylejones_47003/introduction-to-statistics-for-people-who-do-business-analytics-26878760a14a)]
- [[Linear Regression for Business Analysis](https://medium.com/@kylejones_47003/linear-regression-for-business-analysis-2407d9fe2942)]

### Thank you for being a part of the community
*Before you go:*

- Be sure to **clap** and **follow** the writer ️👏**️️**
- [Follow us: [**X**](https://x.com/inPlainEngHQ) \| [**LinkedIn**](https://www.linkedin.com/company/inplainenglish/) \| [**YouTube**](https://www.youtube.com/channel/UCtipWUghju290NWcn8jhyAw) \| [**Newsletter**](https://newsletter.plainenglish.io/) \| [**Podcast**](https://open.spotify.com/show/7qxylRWKhvZwMz2WuEoua0)]
- [[**Check out CoFeed, the smart way to stay up-to-date with the latest in tech**](https://cofeed.app/) **🧪**]
- [[**Start your own free AI-powered blog on Differ**](https://differ.blog/) 🚀]
- [[**Join our content creators community on Discord**](https://discord.gg/in-plain-english-709094664682340443) 🧑🏻‍💻]
- [For more content, visit [**plainenglish.io**](https://plainenglish.io/) + [**stackademic.com**](https://stackademic.com/)]
