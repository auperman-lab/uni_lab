import random

n = 100000
succes = 0

for i in range(n):
    point1 = random.random()
    point2 = random.random()
    point3 = random.random()
    mxpoint = max(point1, point2, point3)-0.5
    if mxpoint < 0:
        succes += 1
    else:
        if not mxpoint <= point3 and mxpoint <= point2 and mxpoint <= point1:
            succes += 1
print(succes/n)
