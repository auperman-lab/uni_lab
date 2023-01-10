from random import randint
import matplotlib.pyplot as plt

profit1 = []
money = 0
n = 1000
tries = list(range(1, n+1))

for i in range(n):
    if randint(0, 38) < 18:
        money += 20
    else:
        money -= 20
    profit1.append(money)

money = 0
profit2 = []

for i in range(n):
    if randint(0, 38) == 0:
        money += 36
    else:
        money -= 1
    profit2.append(money)

plt.plot(tries, profit1, label="Bet on RED")
plt.plot(tries, profit2, label="Bet on 18")
plt.xlabel('Tries')
plt.ylabel('Profit')
plt.title('Casino Roulette')
plt.legend()
plt.show()
