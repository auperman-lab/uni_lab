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

start1 = int(input('start is : '))
start = start1
final = int(input('final is : '))
stops = int(input('how many stops?'))

final_road = []
no_cycle = [start1]
no_more_stops = []

while start != final:
    no_cycle = []
    for i in final_road:
        no_cycle.append(i[0])
        no_cycle.append(i[1])
    possible_direction = []
    for i in prerequisites:
        if i[0] == start and i not in no_more_stops:
            possible_direction.append(i)
    minn = [0, 0, 9999999]
    for i in possible_direction:
        if i[2] < minn[2] and i[1] not in no_cycle:
            minn = i

    for i in no_more_stops:
        if i[0] != start and i[0] not in no_cycle:
            no_more_stops.remove(i)

    if minn != [0, 0, 9999999]:
        final_road.append(minn)
    if len(final_road) > stops+1 or minn == [0, 0, 9999999]:
        no_more_stops.append(final_road[-1])
        final_road = final_road[:-1]

        if len(final_road) == 0:
            start = start1
        else:
            start = final_road[-1][1]

    else:
        start = minn[1]
print(final_road)
