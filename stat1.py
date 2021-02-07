import numpy as np

X = [(6,.55), (8,.11), (9,.21), (11,.13)]

def dist_var(X):
    var = 0
    mean = 0
    for x, p in X:
       var += (x**2 * p)
       mean += x*p
    return var - mean**2

def stdev(var):
    return np.power(var, 1/2)