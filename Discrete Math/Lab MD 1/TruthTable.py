from prettytable import PrettyTable


def bincode(n):
    table = []
    for i in range(2 ** n):
        table.append(str(bin(i)))
        table[i] = table[i].replace('0b', '')
        for j in range(0, n - len(table[i])):
            table[i] = '0' + table[i]

    return table


code = input()

var = []
result = []

for i in range(len(code)):                  # aflam cate variabile sunt
    a = code[i]
    if code[i] >= 'a' and code[i] <= 'z':
        if code[i] in var:
            print()
        else:
            var.append(code[i])


code1 = code

bintable = bincode(len(var))

for elem in bintable:
    row = list(elem)
    for j in range(len(var)):
        code1 = code1.replace(var[j], row[j]) # inlocuim pe rand varibilele cu 0 sau 1
    result.append(int(eval(code1.replace('!', ' not ').replace('+', ' or ').replace('*', ' and '))))
    code1 = code

tab = PrettyTable()
tab.field_names = var
for i in bintable:
    row = list(i)
    tab.add_row(row)
code = code.replace(' not ', '!').replace(' or ', '+').replace(' and ', '*')
tab.add_column(code, result)
print(tab)
