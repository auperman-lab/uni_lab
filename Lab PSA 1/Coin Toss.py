import random


def profit(bet):
    money = 0
    for j in range(n):
        tails = 0
        money -= bet
        while True:
            if random.random() > 0.5:
                tails += 1
            else:
                money += 2 ** (tails+1)
                break

    return money


n = 1000

print(profit(15))
