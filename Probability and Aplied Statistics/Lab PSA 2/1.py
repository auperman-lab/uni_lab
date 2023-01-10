import matplotlib.pyplot as plt
from random import randint

n = 100000
nine = 0
ten = 0
for i in range(n):
    dice1 = randint(1, 7)
    dice2 = randint(1, 7)
    dice3 = randint(1, 7)
    if dice1 + dice2 + dice3 == 9:
        nine += 1
    if dice1 + dice2 + dice3 == 10:
        ten += 1

print(ten)
data = {'nine': 20, 'ten': 15}
courses = list(data.keys())
values = [nine, ten]

fig = plt.figure(figsize=(10, 5))

plt.bar(courses, values, color='maroon', width=0.3)

plt.xlabel("Summ of die")
plt.ylabel("Nr of times it happen")
plt.title("Interesting observastion")
plt.show()
