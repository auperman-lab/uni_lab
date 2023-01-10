def shortest_path_bfs(graph, start, end, depth):
    newrow = []
    for strt in start:
        for node in graph[strt]:
            condition = False
            for dep in depth:
                if node in dep:
                    condition = True
            if node == end:
                return len(depth)
            elif not condition:
                newrow.append(node)
    depth.append(list(newrow))
    return shortest_path_bfs(graph, depth[-1], end, depth)


f = open('matrix.txt', 'r')
lines = [line.split() for line in f]

i = 0

friends = {}

while i in range(len(lines)):
    if i == 0:
        lines.remove(lines[i])
    lines[i].remove('|')
    lines[i][0] += '_' + lines[i][1]
    lines[i].remove(lines[i][1])
    j = 1
    summ = 0
    while j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])
        summ += lines[i][j]
        j += 1
    friends[lines[i][0]] = summ

    i += 1

graph = {}

for i in range(len(lines)):
    graph[lines[i][0]] = []
    for j in range(len(lines[i])):
        if lines[i][j] == 1:
            graph[lines[i][0]] += [lines[j-1][0]]


rating = {}
for name in graph.keys():
    rating[name] = 0
    for connection in graph.keys():
        if name != connection:
            rating[name] += shortest_path_bfs(graph, [name], connection, [name]) - 1

d = open('influence.txt', 'r')

popularity_among = [line.split(':') for line in d]

influence = {}
for row in popularity_among:
    row[0] = row[0][:-1]
    row[0] = row[0].replace(' ', '_')
    row[1] = row[1].replace(' ', '')
    row[1] = row[1].replace('\n', '')
    row[1] = float(row[1])
    influence[row[0]] = row[1]



updated_rating = {}

for name in rating:
    updated_rating[name] = rating[name] * influence[name] * friends[name] * 0.5
    print(name, updated_rating[name])
