import math
import numpy as np

r = 6.5
x = 2

def fx(y):
    theta = math.acos(y / r)
    return r * math.sin(theta)

def fy(x):
    theta = math.asin(x / r)
    return r * math.cos(theta)

for x in np.arange(-r,r,0.5):
    y = math.floor(fy(x) * 10) / 10
    print(f"M{x},{-y}V{y}", end=' ')
print()
for y in np.arange(-r,r,0.5):
    x = math.floor(fx(y) * 10) / 10
    print(f"M{-x},{y}H{x}", end=' ')
