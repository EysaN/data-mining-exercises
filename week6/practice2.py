"""
We are flipping coin until it turns to its head. If it happens for the n-th time of flipping, the
player gains 2n dollars. Simulate m games (that is we are playing until flipping m heads).
What will be the average gain if m=100, m=10000 and m=1000000?
"""
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns


def flip_coin(m: int = 1):
    print('doing %s flips' % m)
    heads_flips = []
    for _ in range(m):
        counter = 0
        while 1:
            # considering 0 is tail and 1 is heads
            flip = random.randint(0, 1)
            counter += 1
            if flip == 1:
                break
        heads_flips.append(counter)
    print('the average gain is', 2*sum(heads_flips)/m)
    sd = np.std(heads_flips, ddof=1)
    mean = np.mean(heads_flips)
    t = np.random.normal(loc=mean, scale=sd, size=(1, 2))
    sns.distplot(t, hist=False)
    plt.show()


if __name__ == '__main__':
    flip_coin(100)
    flip_coin(10000)
    flip_coin(1000000)

