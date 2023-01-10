import random

n = 10000
succes = 0



for k in range(n):
    shufflist = random.sample(list(range(1, 101)), k=100)
    empty_seat = list(range(1, 101))
    for i in shufflist:
        if i == shufflist[0]:
            empty_seat.remove(random.choice(empty_seat))
        else:
            if i not in empty_seat:
                empty_seat.remove(random.choice(empty_seat))
            else:
                if i == shufflist[99]:
                    succes += 1
                    break
                empty_seat.remove(i)
        if shufflist[99] not in empty_seat:
            break
print(succes/n)
