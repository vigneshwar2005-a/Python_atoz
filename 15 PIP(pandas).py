# Pandas

'''Pandas is a Python library that helps you work with data
 in tables. Your document introduces Pandas as a tool for analyzing,
cleaning, exploring, and manipulating datasets

Pandas is built on top of another package called NumPy, which means that
Pandas is fast and efficient for numerical data. It also has a lot 
of built-in functionality for working with data, such as filtering,
grouping, and aggregating data.
'''

import pandas as pd # Import Pandas

# Series

'''A Series is like one column in an Excel sheet'''

# Create a Series

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

# Create a Series with custom index

index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)
print(series)


# DataFrame

'''A Series is like one column. A DataFrame is like the entire Excel table, 
containing multiple columns and rows.'''

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)
print(df)

# loc

'''The loc function is used to access a group of rows
 and columns by labels or a boolean array.'''

print(df.loc[0])  # Access the first row

# Named index

data = {
"calories": [420, 380, 390],
"duration": [50, 40, 45]
}
df = pd.DataFrame(
data,index=["day1", "day2", "day3"]
)
print(df)


# Selection by label

print(df.loc["day1"])  # Access the row with index "day1"

# Selection by position

print(df.iloc[0])  # Access the first row by position

# Filtering

print(df[df['calories'] > 400])  # Access rows where 'calories' is greater than 400

# Filtering by multiple conditions

print(df[(df['calories'] > 400) & (df['duration'] < 50)])  




# Data Cleaning

'''Data cleaning is the process of identifying and correcting errors, 
inconsistencies, and inaccuracies in a dataset.'''


import pandas as pd

data = {
"Name": ["Arun", "Priya", "Rahul", "Sneha", "Arun", "Karthik"],
"Age": [20, 21, None, 20, 20, 200],
"Marks": [85, 92, 45, None, 85, 78],
"City": ["Chennai", "Chennai", "Chennai","Mumbai", "Chennai", "Chennai"]
}

df = pd.DataFrame(data)

print(df) # Nan - Not an number 

# Handling Missing Data

print(df.isnull())  # Check for missing values

# Drop rows with missing values

df_cleaned = df.dropna() # dropna means drop the rows with missing values
print(df_cleaned)


# Fill missing values with a specific value

df_filled = df.fillna(0)  # Fill missing values with 0
print(df_filled)


# Remove duplicates

df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)

