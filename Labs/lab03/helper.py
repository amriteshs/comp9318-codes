import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from lab03 import submission as sub


def dot_product(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return 1 / res

def compute_error(data, labels, k):
    n, d = data.shape
    centers = []
    for i in range(k):
        centers.append([0 for j in range(d)])

    for i in range(n):
        centers[labels[i]] = [x + y for x, y in zip(centers[labels[i]], data[i])]

    error = 0
    for i in range(n):
        error += sub.dot_product(centers[labels[i]], data[i])
    return error


if __name__ == '__main__':
    data = np.loadtxt('asset/data.txt', dtype=float)
    k = 3

    print(sub.hc(data, k))
    # print(compute_error(data, sub.hc(data, k), k))

    Z = linkage(data, method='complete', metric=dot_product)
    print([i - 1 for i in list(fcluster(Z, k, criterion='maxclust'))])
