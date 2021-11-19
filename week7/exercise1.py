"""
Exercise 1: Create book.csv data file and read data into dataframe. Do data cleansing tasks on book
data.
1. Order by given field
2. Remove duplicates
3. Detect (and correct) missing and invalid fields
4. Do some lexical conversion
5. Save cleaned data in file
"""
import pandas as pd
import numpy as np


df = pd.read_csv("book.csv")
# 1. Order by given field
df.sort_values("isbn", inplace=True)

# 2. Remove duplicates
df.drop_duplicates(subset=['isbn'], inplace=True)
df.to_csv("book_WithoutDuplicates.csv")

# 3. Detect (and correct) missing and invalid fields
missing_values = ["n/a", "na", "-", "--", " ", ""]
df = pd.read_csv("book_WithoutDuplicates.csv", na_values=missing_values)
# Check if price is number - otherwise treat it as missing value
cnt = 0
for value in df['price']:
    try:
        int(value)
        if int(value) <= 0:  # price cannot be negative
            df.loc[cnt, 'price'] = np.nan
    except ValueError:
        df.loc[cnt, 'price'] = np.nan
    cnt += 1

# 4. Do some lexical conversion
df['title'] = df['title'].str.upper()
print(df)
df['title'] = df['title'].str.lower()
print(df)
df['title'] = df['title'].str.capitalize()
print(df)
df['price'] = pd.to_numeric(df['price'])

# 5. Save cleaned data in file
df.to_csv("book_cleaned.csv")