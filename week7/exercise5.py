"""
Exercise 5: Analyze your data in data.csv. Is there linear correlation between any of the statistical
variables? Calculate correlation matrix and regression where applicable
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv("data.csv")

df.drop_duplicates(inplace=True)
median = df['Calories'].median()
df['Calories'].fillna(median, inplace=True)

# df.plot()
# plt.show()
#
# plt.scatter(x=df['Duration'], y=df['Calories'])
# plt.show()
#
# df["Duration"].plot(kind='hist')
# plt.title('Duration histogram')
# plt.show()
# df["Pulse"].plot(kind='hist')
# plt.title('Pulse histogram')
# plt.show()
# df["Calories"].plot(kind='hist')
# plt.title('Calories histogram')
# plt.show()

sns.set(style='white', context='paper', palette='deep')

# Correlation matrix
corrMatrix = df.corr()
print(corrMatrix)

# Visualizing correlation matrix
sns.heatmap(corrMatrix, annot=True)
plt.show()

# Analysing correlation between Duration and Calories
# sns.jointplot(x="Duration", y="Calories", data=df)
# plt.show()
#
# plt.scatter(x="Duration", y="Calories", data=df)
# plt.show()

# Correlation coefficient
corr = np.corrcoef(df["Duration"], df["Calories"])[0, 1]
print("Correlation between Duration and Calories:", round(corr, 2))

# Significance of correlation coefficient
ttest, pval = stats.ttest_ind(df["Duration"], df["Calories"])
print("Independent t-test:", ttest, pval)

X = df['Duration'].values.reshape(-1,1)
y = df['Calories'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor=LinearRegression()
regressor.fit(X_train, y_train)  # training the algorithm

# To retrieve the intercept:
print(regressor.intercept_)
# For retrieving the slope:
print(regressor.coef_)
# Prediction
y_pred = regressor.predict(X_test)

# Visualization
plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()
