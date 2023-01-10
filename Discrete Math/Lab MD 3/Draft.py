import pygame
import sys



def draw_big_circle(color, x, y, w=4, h=4):
    pygame.draw.rect(screen, color, pygame.Rect(x - 12 * w, y, 2 * 12 * w, 3 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 11 * w, y + 3 * h, 2 * 11 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 10 * w, y + 5 * h, 2 * 10 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 9 * w, y + 7 * h, 2 * 9 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 8 * w, y + 8 * h, 2 * 8 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 7 * w, y + 9 * h, 2 * 7 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 5 * w, y + 10 * h, 2 * 5 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y + 11 * h, 2 * 3 * w, 1 * h))

    pygame.draw.rect(screen, color, pygame.Rect(x - 12 * w, y - 3 * h, 2 * 12 * w, 3 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 11 * w, y - 5 * h, 2 * 11 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 10 * w, y - 7 * h, 2 * 10 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 9 * w, y - 8 * h, 2 * 9 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 8 * w, y - 9 * h, 2 * 8 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 7 * w, y - 10 * h, 2 * 7 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 5 * w, y - 11 * h, 2 * 5 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y - 12 * h, 2 * 3 * w, 1 * h))


def draw_small_circle(color, x, y, w=4, h=4):
    pygame.draw.rect(screen, color, pygame.Rect(x - 8 * w, y, 2 * 8 * w, 3 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 7 * w, y + 3 * h, 2 * 7 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 6 * w, y + 5 * h, 2 * 6 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 5 * w, y + 6 * h, 2 * 5 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y + 7 * h, 2 * 3 * w, 1 * h))

    pygame.draw.rect(screen, color, pygame.Rect(x - 8 * w, y - 3 * h, 2 * 8 * w, 3 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 7 * w, y - 5 * h, 2 * 7 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 6 * w, y - 6 * h, 2 * 6 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 5 * w, y - 7 * h, 2 * 5 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y - 8 * h, 2 * 3 * w, 1 * h))


def draw_token(color, x, y, w=4, h=4):
    pygame.draw.rect(screen, color, pygame.Rect(x - 4 * w, y - 2 * h, 8 * w, 4 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y - 3 * h, 6 * w, h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 2 * w, y - 4 * h, 4 * w, h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y + 2 * h, 6 * w, h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 2 * w, y + 3 * h, 4 * w, h))


def draw_box(x, y, w, h, p=30):

    pygame.draw.line(screen, WHITE, (x - w/2 + 2*w/p, y + h/2), (x + w/2 - 2*w/p, y + h/2))
    pygame.draw.line(screen, WHITE, (x - w/2 + 2*w/p, y - h/2), (x + w/2 - 2*w/p, y - h/2))
    pygame.draw.line(screen, WHITE, (x - w/2, y + h/2 - 2*h/p), (x - w/2, y - h/2 + 2*h/p))
    pygame.draw.line(screen, WHITE, (x + w/2, y + h/2 - 2*h/p), (x + w/2, y - h/2 + 2*h/p))

    pygame.draw.line(screen, WHITE, (x - w/2 + 2*w/p, y + h/2), (x - w/2 + 2*w/p, y + h/2 - h/p))
    pygame.draw.line(screen, WHITE, (x - w/2 + w/p, y + h/2 - h/p), (x - w/2 + w/p, y + h/2 - 2*h/p))
    pygame.draw.line(screen, WHITE, (x - w/2 + w/p, y + h/2 - h/p), (x - w/2 + 2*w/p, y + h/2 - h/p))
    pygame.draw.line(screen, WHITE, (x - w/2, y + h/2 - 2*h/p), (x - w/2 + w/p, y + h/2 - 2*h/p))

    pygame.draw.line(screen, WHITE, (x + w/2 - 2*w/p, y + h/2), (x + w/2 - 2*w/p, y + h/2 - h/p))
    pygame.draw.line(screen, WHITE, (x + w/2 - w/p, y + h/2 - h/p), (x + w/2 - w/p, y + h/2 - 2*h/p))
    pygame.draw.line(screen, WHITE, (x + w/2 - w/p, y + h/2 - h/p), (x + w/2 - 2*w/p, y + h/2 - h/p))
    pygame.draw.line(screen, WHITE, (x + w/2, y + h/2 - 2*h/p), (x + w/2 - w/p, y + h/2 - 2*h/p))

    pygame.draw.line(screen, WHITE, (x + w/2 - 2*w/p, y - h/2), (x + w/2 - 2*w/p, y - h/2 + h/p))
    pygame.draw.line(screen, WHITE, (x + w/2 - w/p, y - h/2 + h/p), (x + w/2 - w/p, y - h/2 + 2*h/p))
    pygame.draw.line(screen, WHITE, (x + w/2 - w/p, y - h/2 + h/p), (x + w/2 - 2*w/p, y - h/2 + h/p))
    pygame.draw.line(screen, WHITE, (x + w/2, y - h/2 + 2*h/p), (x + w/2 - w/p, y - h/2 + 2*h/p))

    pygame.draw.line(screen, WHITE, (x - w/2 + 2*w/p, y - h/2), (x - w/2 + 2*w/p, y - h/2 + h/p))
    pygame.draw.line(screen, WHITE, (x - w/2 + w/p, y - h/2 + h/p), (x - w/2 + w/p, y - h/2 + 2*h/p))
    pygame.draw.line(screen, WHITE, (x - w/2 + w/p, y - h/2 + h/p), (x - w/2 + 2*w/p, y - h/2 + h/p))
    pygame.draw.line(screen, WHITE, (x - w/2, y - h/2 + 2*h/p), (x - w/2 + w/p, y - h/2 + 2*h/p))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
RED = (252, 0, 0)
PINK = (252, 180, 255)
CYAN = (0, 252, 255)
ORANGE = (252, 180, 85)
YELLOW = (252, 252, 0)
GREEN = (0, 252, 0)


pygame.init()
screen = pygame.display.set_mode((400, 400))

font1 = pygame.font.Font('/Users/nmacrii/Desktop/PixelEmulator.ttf', 20)
MM = font1.render('MasterMind', True, WHITE)

screen.fill(BLACK)
screen.blit(MM, (0, 0))
list = [0, 1, 2, 3]
print(list[2:])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
