import random

n = 100000
succes = 0

for i in range(n):
    breakp1 = random.random()
    breakp2 = random.random()
    if breakp1 < breakp2:
        breakp1, breakp2 = breakp2, breakp1
    if breakp1 > 1 - breakp1 and 1 - breakp2 > breakp2 and 1 - breakp1 + breakp2 > breakp1 - breakp2:
        succes += 1
print(succes/n)
