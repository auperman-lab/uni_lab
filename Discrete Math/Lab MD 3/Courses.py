courses = input()
courses = courses.split()
prerequisites = []
for i in courses:
    twoc = i.split(',')
    for j in range(len(twoc)):
        twoc[j] = twoc[j].replace('[', '')
        twoc[j] = twoc[j].replace(']', '')
        twoc[j] = int(twoc[j])
    prerequisites.append(twoc)

arange = []

cycle = False

for k in range(len(prerequisites)):
    i = 0
    icond = False
    dictcond = False
    dict = [k]
    arange.append([prerequisites[k]])
    firstelem = prerequisites[k][0]
    lastelem = prerequisites[k][1]

    while i in range(len(prerequisites)):
        if prerequisites[i][0] == lastelem and i not in dict:
            arange[k].append(prerequisites[i])
            var = i+1
            while var in range(len(prerequisites)):
                if prerequisites[var][0] == lastelem and var not in dict:
                    arange[k].append(prerequisites[var])
                var += 1
            lastelem = prerequisites[i][1]
            icond = True
            dictcond = True
        if prerequisites[i][1] == firstelem and i not in dict:
            arange[k].insert(0, prerequisites[i])
            var = i + 1
            while var in range(len(prerequisites)):
                if prerequisites[var][1] == firstelem and var not in dict:
                    arange[k].insert(0, prerequisites[var])
                var += 1
            firstelem = prerequisites[i][0]
            icond = True
            dictcond = True
        if dictcond:
            dict.append(i)
            dictcond = False
        i += 1
        if icond:
            i = 0
            icond = False
    newlist = []
    for i in arange[k]:
        if i in newlist:
            cycle = True
            break
        else:
            newlist.append(i)

for i in arange:
    print(i)

if cycle:
    print(not cycle)
else:
    print(not cycle)
