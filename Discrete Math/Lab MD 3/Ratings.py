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
        j += 1

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

for name in rating:
    print(name, rating[name])

