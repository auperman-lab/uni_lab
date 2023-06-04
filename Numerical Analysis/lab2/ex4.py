import csv
import numpy as np
from dijkstar import Graph, find_path
graph = Graph()


def distance_matrix(x0, y0, x1, y1):
    obs = np.vstack((x0, y0)).T
    interp = np.vstack((x1, y1)).T

    d0 = np.subtract.outer(obs[:, 0], interp[:, 0])
    d1 = np.subtract.outer(obs[:, 1], interp[:, 1])

    return np.hypot(d0, d1)


def simple_idw(xa, ya, za, xi, yi):
    dist = distance_matrix(xa, ya, xi, yi)

    weights = 1.0 / dist
    weights /= weights.sum(axis=0)

    zi = weights.T @ za
    return zi


xy, z = [], []
with open('map.csv', 'r') as csv_file:
    file = csv.DictReader(csv_file)
    line_count = 0
    for row in file:
        xy.append([int((row['Coordinate'].split('; '))[0][-1]), int((row['Coordinate'].split('; '))[1][0])])

        if row['Elevation'] == ' NaN':
            z.append(0)
        else:
            z.append(int(row['Elevation']))

for i in range(len(z)):
    if z[i] == 0:
        aa = xy[i]
        xx, yy = [], []
        zz = []
        for j in range(len(z)):
            if xy[i][1]-1 <= xy[j][1] <= xy[i][1]+1 and xy[i][0]-1 <= xy[j][0] <= xy[i][0]+1 and z[j] != 0:
                xx.append(xy[j][0])
                yy.append(xy[j][1])
                zz.append(z[j])
        z[i] = simple_idw(xx, yy, zz, xy[i][0], xy[i][1])[0]
        print(xy[i], z[i])

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for node in xy:
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if neighbor in xy:
            graph.add_edge(str(node), str(neighbor), z[xy.index(neighbor)]-z[xy.index(node)])

print(find_path(graph, str(xy[0]), str(xy[-1])))
