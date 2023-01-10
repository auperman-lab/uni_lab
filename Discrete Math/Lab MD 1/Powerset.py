

def bincode(n):                                       #facem truth table binar
    table = []
    for i in range(2 ** n):
        table.append(str(bin(i)))
        table[i] = table[i].replace('0b', '')
        for j in range(0, n - len(table[i])):
            table[i] = '0' + table[i]

    return table


powset = []
set = list(map(str, input().split()))

bintable = bincode(len(set))


for i in range(len(bintable)):     # cream powset pe rand , la fiecare element din set se atribuie o pozitie in bintable
    row = list(bintable[i])
    powset = powset + ['']
    for j in range(len(set)):
        if row[j] == '1':
            powset[i] = powset[i]+str(set[j])


print(powset)
