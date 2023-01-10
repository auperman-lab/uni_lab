import random


def tenis(player, point):
    if random.random() <= point:
        player += 1
    else:
        return player
    return tenis(player, point)


ana = 0
dan = 0
wins = 0
n = int(input())

for i in range(n):
    while True:
        if ana < 25:
            ana = tenis(ana, 0.7)
        else:
            wins += 1
            break

        if dan < 25:
            dan = tenis(dan, 0.5)
        else:
            break
    ana = 0
    dan = 0
print()
print('Probability that Ana wins is', wins/n)
