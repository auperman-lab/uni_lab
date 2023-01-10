import random

money = 0
offense = 0

for i in range(365):
    if random.random() > 0.02:
        if random.random() < 0.05:
            offense += 1
            if offense == 1:
                money += 50
            elif offense == 2:
                money += 150
            else:
                money += 300
    else:
        money += 6

    if random.random() > 0.02:
        if random.random() < 0.05:
            offense += 1
            if offense == 1:
                money += 50
            elif offense == 2:
                money += 150
            else:
                money += 300
    else:
        money += 6

print('Money that Jora Petrovici pays for troleibuz per year is : ', money)
print('Money that an uniformly chosen probability enjoyer pays for troleibuz per year is : ', 365*6*2)
