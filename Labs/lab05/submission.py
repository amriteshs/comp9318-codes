import numpy as np


def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function
    data = np.c_[np.ones(data.shape[0]), data]

    for _ in range(num_epochs):
        sigmoid = np.divide(1, np.add(1, np.exp(np.multiply(-1, np.dot(data, weights)))))
        error = np.subtract(labels, sigmoid)
        gradient = np.dot(np.transpose(data), error)
        weights = np.add(weights, np.multiply(gradient, learning_rate))

    return weights
