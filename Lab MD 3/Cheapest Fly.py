def find_all_paths(graph, start, end, path=[], vert=[]):
    path = path + [vert]
    if start == end:
        return [path]
    startvertex = []
    for i in graph:
        if i[0] == start:
            startvertex.append(i)
    paths = []
    for vertex in startvertex:
        if vertex not in path:
            newpaths = find_all_paths(graph, vertex[1], end, path, vertex)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


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

start = int(input('start is : '))
final = int(input('final is : '))
stops = int(input('how many stops?'))

#[0,1] [0,3] [1,2] [3,1] [1,4] [4,2] [2,6] [2,5] [5,6]
#[0,1,5] [0,3,2] [1,2,5] [3,1,2] [1,4,1] [4,2,1]

gooff_job = find_all_paths(prerequisites, start, final)
path = 0
while path in range(len(gooff_job)):
    gooff_job[path].remove(gooff_job[path][0])
    if len(gooff_job[path]) > stops + 1:
        gooff_job.remove(gooff_job[path])
        path -= 1
    path += 1

minn = 999999
for path in gooff_job:
    summ = 0
    for vertex in path:
        print(vertex)
        summ += vertex[2]
    if summ < minn:
        minn = summ
        result = path
    print(summ)
    print()

print(result)
