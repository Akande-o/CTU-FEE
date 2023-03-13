#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


def perceptron(X, y, max_iterations):
    """
    w, b = perceptron(X, y, max_iterations)

    Perceptron algorithm.
    Implements the perceptron algorithm
    (http://en.wikipedia.org/wiki/Perceptron)

    :param X:               d-dimensional observations, (d, number_of_observations) np array
    :param y:               labels of the observations (0 or 1), (n,) np array
    :param max_iterations:  number of algorithm iterations (scalar)
    :return w:              w - weights, (d,) np array
    :return b:              b - bias, python float
    """
    w_init = np.zeros(X.shape[0]+1)
    y = np.where(y==1, -1, 1)
    k = np.where(y==-1)
    Y = X.copy()
    Y[:,k] = -Y[:, k]
    Y = np.append(Y, [y], axis=0)
    for i in range(max_iterations):
        z = np.matmul(w_init, Y)
        j = np.where(z <= 0)[0]
        if len(j) == 0:
            w = w_init[:Y.shape[0]-1]
            b = w_init[Y.shape[0]-1]
            return w, b
        j = np.min(j)
        w_init += Y[:, j]


    return np.nan, np.nan


def lift_dimension(X):
    """
    Z = lift_dimension(X)

    Lifts the dimensionality of the feature space from 2 to 5 dimensions

    :param X:   observations in the original space
                2-dimensional observations, (2, number_of_observations) np array
    :return Z:  observations in the lifted feature space, (5, number_of_observations) np array
    """
    
    Z = np.append(X, [np.square(X[0]), X[0]*X[1], np.square(X[1])], axis=0)
    return Z


def classif_quadrat_perc(tst, model):
    """
    K = classif_quadrat_perc(tst, model)

    Classifies test samples using the quadratic discriminative function

    :param tst:     2-dimensional observations, (2, n) np array
    :param model:   dictionary with the trained perceptron classifier (parameters of the discriminative function)
                        model['w'] - weights vector, np array (d, )
                        model['b'] - bias term, python float
    :return:        Y - classification result (contains either 0 or 1), (n,) np array
    """
    X = lift_dimension(tst)
    Y = np.matmul(model['w'], X) + model['b']
    Y = np.where(Y>0, 0, 1)
    return Y



################################################################################
#####                                                                      #####
#####             Below this line are already prepared methods             #####
#####                                                                      #####
################################################################################

def pboundary(X, y, model, figsize=None, style_0='bx', style_1='r+'):
    """
    pboundary(X, y, model)

    Plot boundaries for perceptron decision strategy

    :param X:       d-dimensional observations, (d, number_of_observations) np array
    :param y:       labels of the observations (0 or 1), (n,) np array
    :param model:   dictionary with the trained perceptron classifier (parameters of the discriminative function)
                        model['w'] - weights vector, np array (d, )
                        model['b'] - bias term, python float
    """

    plt.figure(figsize=figsize)
    plt.plot(X[0, y == 0], X[1, y == 0], style_0, ms=10)
    plt.plot(X[0, y == 1], X[1, y == 1], style_1, ms=10)

    minx, maxx = plt.xlim()
    miny, maxy = plt.ylim()

    epsilon = 0.1 * np.maximum(np.abs(maxx - minx), np.abs(maxy - miny))

    x_space = np.linspace(minx - epsilon, maxx + epsilon, 1000)
    y_space = np.linspace(miny - epsilon, maxy + epsilon, 1000)
    x_grid, y_grid = np.meshgrid(x_space, y_space)

    x_grid_fl = x_grid.reshape([1, -1])
    y_grid_fl = y_grid.reshape([1, -1])

    X_grid = np.concatenate([x_grid_fl, y_grid_fl], axis=0)
    Y_grid = classif_quadrat_perc(X_grid, model)
    Y_grid = Y_grid.reshape([1000, 1000])

    blurred_Y_grid = ndimage.gaussian_filter(Y_grid, sigma=0)

    plt.contour(x_grid, y_grid, blurred_Y_grid, colors=['black'])
    plt.xlim(minx, maxx)
    plt.ylim(miny, maxy)
# X = np.array([[1, 1, 2, 2], [1, 3, 5, 6]])
# y = np.array([0, 0, 1, 1])
# # X = np.array([[3, 1, 2, 2], [2, 3, 5, 6]])
# # y = np.array([0, 0, 1, 0])
# w, b = perceptron(X, y, 100)
# print('your solution may differs\nw: ', w, '\nb: ', b)
# X = np.array([[1, 0, 2], [3, 5, 1]])
# Z = lift_dimension(X)
# print(Z)