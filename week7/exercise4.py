"""
Exercise 4: Create categories of numeric data, i.e. label numeric data with categorical data. Open
the cleaned data.csv and add categories according to Calories.
If Calories <= Q1 → few
If Calories > Q1 and Calories < Q3 → normal
If Calories >= Q3 → high
        a) Insert a new column into the data frame to store the appropriate text.
        b) Calculate group mean Calories.
"""
import pandas as pd


df = pd.read_csv("data_cleaned.csv")
q_1 = df['Calories'].quantile(q=0.25)
q_2 = df['Calories'].median()
q_3 = df['Calories'].quantile(q=0.75)
q_4 = df['Calories'].max()

print(df.describe())

df['Category'] = pd.cut(x=df['Calories'], bins=[0, q_1, q_3, q_4], labels=['few', 'normal', 'high'])

print(df.info)

print(df.groupby(['Category']).mean())

df.to_csv("data_categorized.csv")
