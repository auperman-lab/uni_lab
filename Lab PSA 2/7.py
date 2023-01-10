import matplotlib.pyplot as plt
import random

nrsucces = []
for i in range(31):
    nrsucces.append(0)
    data = list(range(35, 66))

for i in range(1000):
    succes = 0
    for j in range(100):
        if random.random() > 0.5:
            succes += 1
    if 35 <= succes <= 65:
        nrsucces[succes - 35] += 1



fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data, nrsucces, color='maroon', width=0.7)

plt.xlabel("Nr of Heads")
plt.ylabel("Nr of times it happen")
plt.title("Nr of Heads")
plt.show()
