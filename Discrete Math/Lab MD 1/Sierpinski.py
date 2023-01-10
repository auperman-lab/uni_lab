

def triangle(n, basetriangle, y):
    tr = []        # in acesta adaugam spatii la urma pentru a concatena cu triunghiul initial
    dr = []        # in acesta copiem triunghiul dar fara spatii din fata
    hr = []        # pur si simplu unim acele doua
    for i in range(len(basetriangle)):
        tr.append(basetriangle[i][0])
        dr.append(basetriangle[i][0])
        j = 2**y-1-2*i
        while j > 0:
            tr[i] = tr[i]+' '
            j -= 1
        w = 2**(y-1)-1-i
        dr[i] = dr[i].replace(' ', '', w)

    for i in range(len(basetriangle)):  # aflam anumit cate spatii adaugam in fata ca triunghiul de sus
        for j in range((2**(y-2))):
            basetriangle[i][0] = '  ' + basetriangle[i][0]
        hr.append([tr[i] + dr[i]])

    basetriangle = basetriangle + hr
    if y == n:
        return basetriangle
    else:
        return triangle(n, basetriangle, y + 1)  # yey recursie


x = [['   △'], ['  △ △'], [' △   △'], ['△ △ △ △']]   # deci noi avem triangle nostru care se repeta
n = int(input())

if n == 1:
    print(' △')
    print('△ △')
elif n == 2:
    for i in x:
        for j in i:
            print(j, end=" ")
        print()
else:
    x = triangle(n, x, 3)
    for i in x:
        for j in i:
            print(j, end=" ")
        print()
