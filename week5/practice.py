import numpy as np
from numpy import random


x = random.randint(100) # generate random int from 0 to 100
print(x)
x=random.randint(100, size=(5)) # generate an array of 5 random integers from 0 to 100
print(x)
x = random.randint(100, size=(3, 5)) # generate 2D array with 3 rows each containing 5 ints
print(x)
x = random.rand() # generate random float from 0 to 1
print(x)
x = random.rand(5) # generate an array of 5 random floats
print(x)
x = random.rand(3, 5) # generate 2D array with 3 rows each containing 5 random floats
print(x)
x = random.choice([3, 5, 7, 9]) # returns one of the values randomly
print(x)
x = random.choice([3, 5, 7, 9], size=(3, 5)) #creates 2D array with given shape from list
print(x)
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr) # changes the original array
print(arr)
print(random.permutation(arr)) # returns random permutation, leaving the array unchanged
#
# arr = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
# hist,bins = np.histogram(arr,bins = [0,20,40,60,80,100]) # numeric repr. of histogram
# print(hist) # result: [3 4 5 2 1]
# print(bins) # result: [0 20 40 60 80 100]
# # bin: rectangles of equal horizontal size corresponding to class interval in the histogram
# from matplotlib import pyplot as plt
# plt.hist(arr, bins = [0,20,40,60,80,100]) # converts histogram into a graph
# plt.title("histogram")
# # plt.show()
#
# print('-'*100)
#
# from matplotlib import pyplot as plt
# x = np.arange(1,11)
# y = 2 * x + 5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x,y) # continuous line
# plt.plot(x,y,"ob") # circles represent points in blue
# # plt.show()
#
#
# x = [5,8,10]
# y = [12,16,6]
# x2 = [6,9,11]
# y2 = [6,15,7]
# plt.bar(x, y, align = 'center')
# plt.bar(x2, y2, color = 'g', align = 'center')
# plt.title('Bar graph')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# # plt.show()
#
import matplotlib.pyplot as plt
import seaborn as sns
# sns.distplot([0, 1, 2, 3, 4, 5], hist=False) # default setting: hist = True
# # Takes as input an array and plots a curve corresponding to the distr. of points in the array
# # plt.show()

# x = random.normal(loc=1, scale=2, size=(2, 3))
# sns.distplot(random.normal(size=1000), hist=False) # Visualize random normal distribution
# plt.show()
#
# x = random.binomial(n=10, p=0.5, size=10)
# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
# plt.show()

# x = random.poisson(lam=2, size=10)
# sns.distplot(random.poisson(lam=2, size=10), kde=False)
# plt.show()

# x = random.uniform(size=(2, 3))
# sns.distplot(random.uniform(size=1000),hist=False)
# plt.show()

# x = random.logistic(loc=1, scale=2, size=(2, 3))
# sns.distplot(random.logistic(size=1000),hist=False)
# plt.show()

# x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
# sns.distplot(x, hist=True, kde=False)
# plt.show()

# x = random.exponential(scale=2, size=(2, 3))
# sns.distplot(random.exponential(size=1000),hist=False)
# plt.show()

# x = random.chisquare(df=2, size=(2, 3))
# sns.distplot(random.chisquare(df=1, size=1000), hist=False)
# plt.show()

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
# newarr = np.sum([arr1, arr2])
# print(newarr)
# newarr = np.sum([arr1, arr2], axis=1)
# print(newarr)
