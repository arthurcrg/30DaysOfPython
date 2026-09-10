# Pandas is and open-source data analysis and manipulation library for Python.
# It provides data structures and tools designed to work with table-like data which is Series and Data Frames.

import pandas as pd
import numpy as np

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)

# Creating pandas series with custom index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# Creating pandas series with a dictionary
dct = {'name':'Link','country':'Hyrule','city':'Kokiri Forest'}
s = pd.Series(dct)
print(s)

# Creating a constant pandas series
s = pd.Series(10, index = [1, 2, 3])
print(s)

# Creating a pandas series using linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

# DataFrames: 2D data structures with rows and columns

# Creating a dataframe from a list of lists
data = [['Link', 'Hyrule', 'Kokiri Forest'], 
        ['Zelda', 'Hyrule', 'Hyrule Castle'], 
        ['Ganondorf', 'Gerudo Desert', 'Gerudo Fortress']]
df = pd.DataFrame(data, columns=['Name', 'Country', 'City'])
print(df)

# Creating a dataframe from a dictionary
data = {'Name': ['Link', 'Zelda', 'Ganondorf'],
        'Country': ['Hyrule', 'Hyrule', 'Gerudo Desert'],
        'City': ['Kokiri Forest', 'Hyrule Castle', 'Gerudo Fortress']}
df = pd.DataFrame(data)
print(df)

# Creating a dataframe from a list of dictionaries
data = [{'Name': 'Link', 'Country': 'Hyrule', 'City': 'Kokiri Forest'},
        {'Name': 'Zelda', 'Country': 'Hyrule', 'City': 'Hyrule Castle'},
        {'Name': 'Ganondorf', 'Country': 'Gerudo Desert', 'City': 'Gerudo Fortress'}]
df = pd.DataFrame(data)
print(df)

# Reading CSV files using Pandas
import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)

# Data Exploration and Analysis
print(df.head()) # Display the first 5 rows of the dataframe
print(df.tail()) # Display the last 5 rows of the dataframe
print(df.shape) # Display the shape of the dataframe
print(df.info()) # Display information about the dataframe
print(df.columns) # Display the column names of the dataframe
height = df['Height'] # Accessing a specific column
print(height)
weight = df['Weight'] # Accessing a specific column
print(weight)
print(len(height) == len(weight)) # Check if the length of height and weight columns are equal
print(height.describe()) # Display statistical summary of the height column
print(weight.describe()) # Display statistical summary of the weight column
print(df.describe()) # Display statistical summary of the entire dataframe

# Modifying DataFrames
# To modify a DataFrame, you can use various methods such as adding or removing columns, renaming columns, and changing data types.
data = [ {'Name': 'Link', 'Country': 'Hyrule', 'City': 'Kokiri Forest'},
         {'Name': 'Zelda', 'Country': 'Hyrule', 'City': 'Hyrule Castle'},
         {'Name': 'Ganondorf', 'Country': 'Gerudo Desert', 'City': 'Gerudo Fortress'}]
df = pd.DataFrame(data)
print(df)

# Adding a new column to the DataFrame
df['Age'] = [17, 16, 35]
print(df)

# Modifying an existing column in the DataFrame
df['Age'] = df['Age'] + 1
print(df)

# Formatting DataFrame Columns
df['Age'] = round(df['Age'], 2) # Round the Age column to 2 decimal places
print(df)

# Checking data types of Column Values
print(df.dtypes) # Display the data types of each column in the DataFrame
df['Age'] = df['Age'].astype(float) # Change the data type of the Age column to float
print(df.dtypes) # Display the data types of each column in the DataFrame after modification

mean_age = df['Age'].mean() # Calculate the mean of the Age column
print(mean_age) # Display the mean age
