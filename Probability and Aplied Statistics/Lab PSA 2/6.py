import random

n = 1000000
succes = 0

for i in range(n):
    x = random.random()
    y = random.random()
    if 0.25 < x < 0.75 and 0.25 < y < 0.75:
        succes += 1
print('P of winning is : ', succes/n)
print('E(x) is : ', succes/n - 0.25 * (1 - succes/n))
