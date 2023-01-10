import random

n = 10000
succes = 0

for i in range(n):
    breakp1 = random.random()
    if breakp1 < 1-breakp1:
        while True:
            breakp2 = random.random()
            if breakp2 > breakp1:
                break
        breakp1, breakp2 = breakp2, breakp1
        if breakp1 > 1 - breakp1 and 1 - breakp2 > breakp2 and 1 - breakp1 + breakp2 > breakp1 - breakp2:
            succes += 1
    else:
        while True:
            breakp2 = random.random()
            if breakp2 < breakp1:
                break
        if breakp1 > 1 - breakp1 and 1 - breakp2 > breakp2 and 1 - breakp1 + breakp2 > breakp1 - breakp2:
            succes += 1

print(succes/n)
