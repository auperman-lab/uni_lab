import hashlib
import random

table = []
hashtable = []
i = True

while True:       # prosta facem birthday paradox
    bday = str(random.randrange(1, 366))
    encript = hashlib.md5(bday.encode()).hexdigest()
    encript = encript[:10]
    if encript in hashtable:
        print(bday)
        print(encript)
        print(len(table)+1)
        table.append(bday)
        hashtable.append(encript)
        break
    else:
        table.append(bday)
        hashtable.append(encript)
