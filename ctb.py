import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 0.5
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def main():
    global my_score
    my_score = 0
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Cycle start!')
                click(event)

        new_ball()
        pygame.display.update()
        screen.fill(BLACK)

    pygame.quit()


def new_ball():
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    global x_event, y_event
    x_event, y_event = event.pos
    print("ball xyr",x, y, r)
    print("my event pos", x_event, y_event)
    ptx = abs(x_event - x)
    pty = abs(y_event - y)
    print("ptxpty", ptx, pty)

    if ptx < r and pty < r:
        my_score += 1
        print("score", my_score)


main()

