from random import randint
print('')

succes1 = 0
succes2 = 0
succes3 = 0
succes4 = 0
succes5 = 0
succes6 = 0
succes7 = 0
succes8 = 0
n = int(input())

for i in range(n):
    shoot = randint(2, 6)
    if shoot != 5:
        succes1 += 1

    shoot = randint(0, 6)
    if shoot != 0 and shoot != 1:
        succes2 += 1

    bullet1 = randint(0, 5)
    bullet2 = randint(0, 5)
    shoot = randint(0, 5)
    if shoot != bullet1 and shoot != bullet2:
        succes3 += 1

    bullet1 = randint(0, 5)
    bullet2 = randint(0, 5)
    shoot = randint(0, 6)
    if shoot != bullet1 and shoot != bullet2:
        succes4 += 1

    shoot = randint(2, 5)
    if shoot != 4:
        succes5 += 1

    shoot = randint(0, 5)
    if shoot != 0 and shoot != 1:
        succes6 += 1

    bullet1 = randint(0, 4)
    bullet2 = randint(0, 4)
    shoot = randint(0, 4)
    if shoot != bullet1 and shoot != bullet2:
        succes7 += 1

    bullet1 = randint(0, 4)
    bullet2 = randint(0, 4)
    shoot = randint(0, 5)
    if shoot != bullet1 and shoot != bullet2:
        succes8 += 1




print('Probability if there are 2 adjacent bullets in a 6 slot revolver:')
print('   1.if we dont spin the barrel', succes1/n)
print('   2.if we spin the barrel', succes2/n)
print('')
print('Probability if there are 2 not adjacent bullets in a 6 slot revolver:')
print('   1.if we dont spin the barrel', succes3/n)
print('   2.if we spin the barrel', succes4/n)
print('')
print('Probability if there are 2 adjacent bullets in a 5 slot revolver:')
print('   1.if we dont spin the barrel', succes5/n)
print('   2.if we spin the barrel', succes6/n)
print('')
print('Probability if there are 2 not adjacent bullets in a 5 slot revolver:')
print('   1.if we dont spin the barrel', succes7/n)
print('   2.if we spin the barrel', succes8/n)
