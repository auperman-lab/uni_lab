def checkstr(pas, str):
    for i in str:
        if i in pas:
            return True
    return False


password = input()
steps = 0
duplicates = 0
special = 0
i = 0

while i < len(password) - 2:
    if password[i] == password[i + 1] == password[i + 2]:
        duplicates += 1
        i += 2
    i += 1

if not checkstr(password, '~`!@#$%^&*()-_+={}[]|\;:"<>,./?'):
    special += 1
if not checkstr(password, '0123456789'):
    special += 1
if not checkstr(password, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    special += 1
if not checkstr(password, 'abcdefghijklmnopqrstuvwxyz'):
    special += 1

if len(password) <= 8:

    steps = max(special, duplicates, 8 - len(password))

elif len(password) <= 20:

    steps = max(special, duplicates)
else:

    steps = max(special, duplicates, len(password)-20)

if steps == 0:
    print("good")
else:
    print(steps)
