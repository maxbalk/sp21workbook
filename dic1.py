import numpy as np

def one_dim_entropy(px: list):
    Hx = 0
    for i, p in enumerate(px):
        Hx += p * np.log2(1/p)
    return Hx

"""           """
""" PROBLEM 2 """
"""           """
xy = np.array([
    [2/32, 2/32, 4/32, 8/32],
    [1/32, 4/32, 2/32, 1/32],
    [1/32, 0/32, 1/32, 2/32],
    [1/32, 1/32, 1/32, 1/32]])

px = np.zeros(4)
py = np.zeros(4)
Hxy = 0

for x, row in enumerate(xy):
    for y, p in enumerate(row):
        px[x] += xy[y][x]
        py[y] += xy[y][x]
        if p != 0:
            Hxy += p * np.log2(1/p)

Hx = one_dim_entropy(px)
Hy = one_dim_entropy(py)
print("Problem 2")
print("H(x) = {}".format(Hx))
print("H(y) = {}".format(Hy))
print("H(xy) = {}".format(Hxy))
print("H(x|y) = {}".format(Hxy - Hy))
print("H(y|x) = {}".format(Hxy - Hx))
print("I(x,y) = {}".format(Hx + Hy - Hxy))




"""           """
""" PROBLEM 4 """
"""           """
x = [1,2,2,3,3,3,4,4,4,4]
y = [1,4,4,9,9,9,16,16,16,16]
Hx = 0
Hy = 0
for i, val in enumerate(x):
    Hx += (val/len(x)) * np.log2( len(x)/val )
for i, val in enumerate(y):
    Hy += (y.count(val)/len(y)) * np.log2( len(y)/y.count(val) )
print("Problem 4:")    
print("\nH(X) = {}".format(Hx))
print("H(X^2) = {}".format(Hy))
print("the information contained in g(X)) is at most equal to the information in X. Our best case scenario, and goal, is to remove or reduce parts of the source but not lose any information\n")



"""           """
""" PROBLEM 5 """
"""           """
from chardet import detect
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

filename = 'state.txt'
f = open(filename, 'r', encoding = get_encoding_type(filename))
contents = f.read()
counts = {}
for char in contents:
    if char not in counts:
        counts[char] = 0
    counts[char] += 1

Px = {}
nchars = len(contents)
for key, value in counts.items():
    Px[key] = value/nchars

Htext = one_dim_entropy(Px.values())
print("problem 5")
print("entropy of the text file is {}".format(Htext))
