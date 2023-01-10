def bfs(graph, start, end, depth):
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
    return bfs(graph, depth[-1], end, depth)




graph = {'D1': {'D2', 'C1'},
         'D2': {'C2', 'D1'},
         'C1': {'C2', 'B1', 'D1'},
         'C2': {'D2', 'C1', 'B2'},
         'B1': {'C1', 'B2'},
         'B2': {'B1', 'A2', 'C2'},
         'A2': {'B2', 'A1'},
         'A1': {'A2'}}
start = 'A1'
finish = 'B2'

alexa = bfs(graph, [start], 'B2', [start])
print(alexa)