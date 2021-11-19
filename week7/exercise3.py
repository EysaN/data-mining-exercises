"""
Exercise 3: Open dirtydata.csv and clean the data. Save the cleaned data set in a new file.
"""
import pandas as pd
import numpy as np
from datetime import datetime as dt


df = pd.read_csv("dirtydata.csv")
# print(df.head())
# print(df.tail())
# print(df.describe())

# clean the data
df.drop_duplicates(inplace=True)
df.to_csv("data_wo_dups.csv")

missing_values = ["n/a", "na", "-", "--", " ", ""]
df = pd.read_csv("data_wo_dups.csv", na_values=missing_values)
median = df['Calories'].median()
df['Calories'].fillna(median, inplace=True)

min_date = None
count = 0
for date in df['Date']:
    try:
        _date = dt.strptime(date, "'%Y/%m/%d'")
        min_date = _date if min_date is None or _date < min_date else min_date
    except (ValueError, TypeError) as e:
        df.loc[count, 'Date'] = np.nan
    count += 1

df['Date'].fillna(dt.strftime(min_date, "'%Y/%m/%d'"), inplace=True)

# Save the cleaned data set in a new file
df.to_csv("data_cleaned.csv")
