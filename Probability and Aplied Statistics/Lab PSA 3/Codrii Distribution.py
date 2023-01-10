import random
import matplotlib.pyplot as plt

n = 100
average = 0
total_deers = []
found_deers_t = []


for untagged_deers in range(150, 1500):
    deers = []
    for i in range(untagged_deers):
        deers.append(1)
    for i in range(50):
        deers.append(0)
    average = 0
    for i in range(100):
        found_tag_deers = 0
        found_deers = random.sample(deers, k=200)
        for deer in found_deers:
            if deer == 0:
                found_tag_deers += 1
        average += found_tag_deers

    total_deers.append(len(deers))
    found_deers_t.append(average/100)



plt.plot(total_deers, found_deers_t)
plt.plot([200, 1550], [8, 8])
plt.xlabel('deers')
plt.ylabel('Tag deers')
plt.show()
#print(average/n)
