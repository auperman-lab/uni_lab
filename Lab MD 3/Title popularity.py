title = 'From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats.'
title = title.replace(':', '')
title = title.replace('.', '')
title = title.replace(',', '')
title = title.split()

f = open('interests.txt', 'r')

internet_interests = [line for line in f]
for i in range(len(internet_interests)):
    internet_interests[i] = internet_interests[i].replace('\n', '')

spectre = []

for word in title:
    for interes in internet_interests:
        if interes == word:
            spectre.append(interes)

print(spectre)

d = open('people_interests.txt', 'r')

people_interests = [line.split(':') for line in d]

dict_people_interests = {}
for i in range(len(people_interests)):
    people_interests[i][0] = people_interests[i][0][:-1]
    people_interests[i][0] = people_interests[i][0].replace(' ', '_')
    people_interests[i][1] = people_interests[i][1].replace('\n', '')
    dict_people_interests[people_interests[i][0]] = people_interests[i][1].split()

for name in dict_people_interests:
    intersection = 0
    for idea in spectre:
        if idea in dict_people_interests[name]:
            intersection += 1
    dict_people_interests[name] = intersection
    print(name, dict_people_interests[name])
