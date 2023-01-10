x = input()
y = input()

if x == '0' or x == 'False' or x == 'false':
    x = False
else:
    x = True

if y == '0' or y == 'False' or y == 'false':
    y = False
else:
    y = True

z = (x and y) or (not x and not y)

print(z)
