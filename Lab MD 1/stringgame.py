
def nonrepstr(string):
    pos = []
    mx = 0
    start = 0
    for i in range(len(string)):
        if string[i] in pos:
            start = max(start, pos[string[i]]+1)
        mx = max(mx, i - start + 1)
        pos[string[i]] = i
    return mx


def longsubstr(string):
    pos = []
    mx = ''
    for k in range(1, len(string)):
        for i in range(len(string) - k + 1):
            check = string[i:k+i]
            if check not in pos:
                pos.append(check)
            elif len(check) > len(mx):
                mx = check
    if len(mx) == 1:
        mx = ''

    return mx


qwerty = input()

print(longsubstr(qwerty))
print(nonrepstr(qwerty))
