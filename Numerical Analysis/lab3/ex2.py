import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def eigenvector_centrality(G, tol=1.0e-6, weight='weight'):

    x = dict([(n, 1.0 / len(G)) for n in G])

    nnodes = G.number_of_nodes()

    while True:
        xlast = x
        x = dict.fromkeys(xlast, 0)

        for n in x:
            for nbr in G[n]:
                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)

        s = 1.0 / np.sqrt(sum(i**2 for i in x.values()))

        for i in x:
            x[i] *= s

        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < nnodes * tol:
            return x


names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah']

adj_matrix = [[0, 1, 1, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 0, 0, 0],
              [1, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 0]]
insta = nx.Graph()
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] == 1:
            insta.add_edge(i, j)


labels = {}
for nam in names:
    labels[names.index(nam)] = nam

x = eigenvector_centrality(insta)

x = dict((labels[key], value) for (key, value) in x.items())
print(sorted(x.items(), key=lambda x: x[1], reverse=True))

nx.draw(insta, labels=labels, with_labels=True)
plt.show()
