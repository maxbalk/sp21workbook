from math import comb as nCr, e, factorial

X = [(6,.55), (8,.11), (9,.21), (11,.13)] #example from webwork
def dist_var(X):
    """
    calculates variance of a discrete distribution with a given density
     - param X: iterable of tuples consisting of (x value, p of x)
    """
    E_of_xsquared = 0
    mean = 0
    for x, p in X:
       E_of_xsquared += (x**2 * p)
       mean += x*p
    return E_of_xsquared - mean**2

def geom_PDF(p, x):
    return (1-p)**(x-1) * p

def geom_CDF(p, N):
    """
    p = probability of success per trial \n
    returns probability first success requires at most N trials
    """
    result = 0
    for i in range(1, N+1):
        result += ((1-p)**(i-1))*p
    return result

def bino_PDF(p, x, N):
    """
    given p chance of success,\n
    return probability of EXACTLY x success in N trials
    """
    return nCr(N, x) * (p**x) * (1-p)**(N-x)

def bino_CDF(p, k, N):
    """
    given p chance of success,\n
    return probability of AT MOST k success in N trials
    """
    result = 0.0
    for i in range(0, k+1):
        result += nCr(N, i) * (p**i) * (1-p)**(N-i)
    return result


def hypergeo_PDF(k, K, n, N):
    return (nCr(K, k) * nCr(N-K, n-k)) / nCr(N, n)

def poi_PDF(lam, k):
    return (lam**k / e**lam) / factorial(k)

def poi_CDF(lam, k):
    """probability of at most k"""
    result = 0
    for i in range(0, k+1):
        result += lam**i / factorial(i)
    return result / e**lam