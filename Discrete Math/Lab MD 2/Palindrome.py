str = input()
invstr = str[::-1]
i = len(str)
while i >= 0:
    workinvstr = invstr[:len(invstr)-i]
    print(workinvstr)
    workstr = workinvstr + str
    if workstr == workstr[::-1]:
        print(workstr)
        break
    i -= 1
