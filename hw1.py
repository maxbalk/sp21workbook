import numpy as np
from numpy import log2

xy = np.array(
    [[2/32, 2/32, 4/32, 8/32],
    [1/32, 4/32, 2/32, 1/32],
    [1/32, 0/32, 1/32, 2/32],
    [1/32, 1/32, 1/32, 1/32]])

px = [0,0,0,0]
for x in range(4):
    for y in range(4):
        px[x] += xy[y][x]

py = [0,0,0,0]
for y in range(4):
    for x in range(4):
        py[y] += xy[y][x]

Hx = 0
for i, p in enumerate(px):
    Hx += (p * log2(1/p))

print(Hx)