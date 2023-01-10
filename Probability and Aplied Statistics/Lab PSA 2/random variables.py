import random

n = 1000
avg_money = 0
for j in range(n):
    money = 0
    for i in range(n):
        x = random.uniform(0, 1)
        k = 1
        while True:
            y = random.uniform(0, 1)
            if y > x:
                break
            else:
                k += 1
        money += k - 1
    avg_money += money/n
print(avg_money / n)

