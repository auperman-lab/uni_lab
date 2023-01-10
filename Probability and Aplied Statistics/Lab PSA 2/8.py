import random

n = 10000
succes = 0
members = 10
permutation = list(range(0, members))

for i in range(n):
    lunch = list(random.sample(permutation, k=members))
    dinner = random.sample(permutation, k=members)
    lunch.append(lunch[0])
    lunch.insert(0, lunch[members-1])
    dinner.append(dinner[0])
    dinner.insert(0, dinner[members - 1])
    print(lunch)
    print(dinner)
    print()
    cond = True
    rlunch = lunch[::-1]

    for j in range(len(lunch)-1):
        for k in range(len(lunch)-1):
            if (dinner[k] == lunch[j] and dinner[k+1] == lunch[j+1]) or (dinner[k] == rlunch[j] and dinner[k+1] == rlunch[j+1]):
                succes += 1
                cond = False
                break
        if not cond:
            break

print(1-(succes/n))

