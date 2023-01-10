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

for i in lines:
    print(i)

sorted_friends = sorted(friends.items(), key=lambda x: x[1], reverse=True)
print(sorted_friends[:10])
