"""
Generate random numbers with a given distribution function : F(x) = x^2, if x∈[0,0.5], and
F(x)=(x+1)/3, if x∈(0.5,2]. Write a function that returns a random number according to F(x).
Call this function 1000 times and calculate the average of the returned numbers, and count
the cases when the returned number equals 0.5. Plot the distribution functions.
"""
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_numbers(m: int = 1):
    print('running %s trails' % m)
    f_x_1, f_x_2 = np.empty(0, float), np.empty(0, float)
    for _ in range(m):
        rand_num = np.around(rd.uniform(0, 2), 1)
        if rand_num > 0.5:
            f_x_2 = np.append(f_x_2, rand_num)
        else:
            f_x_1 = np.append(f_x_1, rand_num)
    f_x_1 = np.power(f_x_1, 2)
    f_x_2 = np.divide(np.add(f_x_2, 1), 3)
    f_x = np.concatenate((f_x_1, f_x_2))
    print('average =', sum(f_x)/m)
    print('# fo times 0.5 came up = ', len(np.where(f_x == 0.5)))
    sd = np.std(f_x, ddof=1)
    mean = np.mean(f_x)
    t = np.random.normal(loc=mean, scale=sd, size=(1, 2))
    sns.distplot(t, hist=False)
    plt.show()


if __name__ == '__main__':
    generate_numbers(1000)

