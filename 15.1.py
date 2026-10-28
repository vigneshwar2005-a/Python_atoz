import pandas as pd
df = pd.read_csv('doctors.csv')
print(df)

# To view the first 5 rows of the DataFrame, you can use the
# head() function:

print(df.head())

# To view the last 5 rows of the DataFrame, you can use the
# tail() function:

print(df.tail())

# To view the column names of the DataFrame, you can use the
# columns attribute:

print(df.columns)

# To view the data types of each column in the DataFrame, you can use the
# dtypes attribute:

print(df.dtypes)

# To view the shape of the DataFrame (number of rows and columns), you can use the
# shape attribute:

print(df.shape)

# To view the summary statistics of the DataFrame, you can use the
# describe() function:

print(df.describe())

# To view the unique values in a column, you can use the
# unique() function:        

print(df['doctor_id'].unique())

# To view the number of unique values in a column, you can use the
# nunique() function:

print(df['doctor_id'].nunique())

# To view the value counts of a column, you can use the
# value_counts() function:  

print(df['doctor_id'].value_counts())

# To view the correlation between columns in the DataFrame, you can use the
# corr() function:

print(df.corr())    
