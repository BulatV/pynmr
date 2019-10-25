#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import numpy as np
import matplotlib.pyplot as plt


def main():
    print('hello world!')
    random_plot(-10, 10, 10000)


def random_plot(mmin=0, mmax=1, llength=100):
    x = np.arange(llength)
    y = np.random.random_sample(llength) * (mmax - mmin) + mmin

    fig, ax = plt.subplots()
    ax.plot(x, y, '.g', alpha=0.85, lw=3.5)
    plt.title('Random numbers from {} to {}'.format(str(mmin), str(mmax)), loc='center')
    plt.show()


if __name__ == '__main__':
    main()
