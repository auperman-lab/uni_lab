import random

n = 100000
realroots = 0
positiveroots = 0

for i in range(n):
    b = random.uniform(-1, 1)
    c = random.uniform(-1, 1)
    if b**2 - 4 * c >= 0:
        realroots += 1
        if -1*b - (b**2 - 4 * c)**0.5 > 0 and -1*b + (b**2 - 4 * c)**0.5 > 0:
            positiveroots += 1
print('P of real roots is: ', realroots/n)
print('P of positive roots is :', positiveroots/n)
