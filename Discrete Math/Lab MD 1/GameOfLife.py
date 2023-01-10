import pygame
import numpy as np


def newgeneration(base, i):

    if base[i] == 0 and base[i+1] == 0 and base[i+2] == 0:
        return 0
    elif base[i] == 1 and base[i+1] == 0 and base[i+2] == 0:
        return 0
    elif base[i] == 1 and base[i+1] == 1 and base[i+2] == 1:
        return 0
    else:
        return 1


length = int(input('length'))
height = int(input('height'))
cell = int(input('cell'))
gen = np.random.randint(0, 2, length)

newgen = [0] + gen + [0]
total = []

for k in range(height):
    gen = []
    for j in range(len(newgen) - 2):
        gen.append(newgeneration(newgen, j))
    newgen = [0] + gen + [0]
    total.append(gen)

gen = np.random.randint(0, 2, length)
newgen = [0] + gen + [0]

black = [0, 0, 0]
white = [255, 255, 255]

pygame.init()

clock = pygame.time.Clock()
size = [cell * length, cell * height]
screen = pygame.display.set_mode(size)

run = True
screen.fill(white)
while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(white)
    for i in range(len(total)):
        for j in range(len(total[i])):
            if total[i][j] == 1:
                pygame.draw.rect(screen, black, (cell * i, cell * j, cell, cell))

    pygame.display.flip()
pygame.quit()
exit()
