import random

n = 10000
righthalf = 0
less5 = 0
exacly5 = 0

for i in range(n):
    x = random.random()
    y = random.random()
    if x >= 0.5:
        righthalf += 1
        if y >= 0.5:
            less5 += 1
            if x == 0.5 or y == 0.5:
                exacly5 += 1
print('Dart will land on right half with probability of : ', righthalf/n)
print('Dart will land not further than 5 inch from the center with probability of : ', less5/n)
print('Dart will land further than 5 inch from the center with probability of : ', (n - less5)/n)
print('Dart will land exactly on the 5 inch circle with probability of : ', exacly5/n)
