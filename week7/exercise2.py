"""
Exercise 2: Data visualization. Generate a data set with gamma distribution and plot the data on histogram.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate data on commute times.
scale, size = 10, 1000
commutes = pd.Series(np.random.gamma(scale, size=size) ** 1.5)

commutes.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')
plt.title('Commute Times for 1,000 Commuters')
plt.xlabel('Counts')
plt.ylabel('Commute Time')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Generate dataset with normal/Laplace distribution
# and plot the data on histogram
# Let's say we have 1000 commuters and
# their daily commuting times in seconds
d = np.random.normal(loc=40, scale=10, size=1000)

sns.histplot(d, stat="density", kde=True, bins=int(180/5), color='darkblue', cbar_kws={'edgecolor': 'black'},
             line_kws={'linewidth': 4})
"""
# Homework: give title for the diagram
# and label the axes
# x-axis : counts
# y-axis : density
"""
plt.title('A density plot of 1,000 Commuters')
plt.xlabel('Counts')
plt.ylabel('density')
plt.show()
