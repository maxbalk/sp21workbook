import numpy as np

xy = np.array([
    [2/32, 2/32, 4/32, 8/32],
    [1/32, 4/32, 2/32, 1/32],
    [1/32, 0/32, 1/32, 2/32],
    [1/32, 1/32, 1/32, 1/32]])

px = np.zeros(4)
py = np.zeros(4)
Hxy = 0
Hx = 0
Hy = 0

for x, row in enumerate(xy):
    for y, p in enumerate(row):
        px[x] += xy[y][x]
        py[y] += xy[y][x]
        if p != 0:
            Hxy += p * np.log2(1/p)

for i, p in enumerate(px):
    Hx += px[i] * np.log2(1/px[i])
    Hy += py[i] * np.log2(1/py[i])

print("H(x) = {}".format(Hx))
print("H(y) = {}".format(Hy))
print("H(xy) = {}".format(Hxy))
print("H(x|y) = {}".format(Hxy - Hy))
print("H(y|x) = {}".format(Hxy - Hx))
print("I(x,y) = {}".format(Hx + Hy - Hxy))


x = [1,2,2,3,3,3,4,4,4,4]
y = np.power(x, 2)
z = np.power(x, 3)
Hx = 0
Hy = 0
Hz = 0
for i, val in enumerate(x):
    Hx += (val/len(x)) * np.log2( len(x)/val )
    Hy += (val/len(y)) * np.log2( len(y)/val )
    Hz += (val/len(z)) * np.log2( len(z)/val )

print("\nhx = {}".format(Hx))
print("hy = {}".format(Hy))
print("hz = {}".format(Hz))

import string
chars = string.printable
