import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def nearest_neighbour():
    # https://www.youtube.com/watch?v=EEUXKG97YRw&t=1628s
    size = 3
    x = np.random.random((size,3))
    diff = x.reshape(size, 1, 3) - x
    D = (diff ** 2).sum(2)
    i = np.arange(size)
    D[i, i] = np.inf
    i = np.argmin(D, 1)
    print(D)
    print(i)


def main():
    points = nearest_neighbour()
    '''
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    xs, ys, zs = points[:, 0], points[:, 1], points[:, 2]
    ax.scatter3D(xs, ys, zs)
    plt.show()
    '''


if __name__ == '__main__':
    main()
