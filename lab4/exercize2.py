import pygame
from pygame.draw import *


def picture_draw():
    sky_and_ground_draw()
    moon_draw()
    clouds_draw()


def sky_and_ground_draw():
    rect(screen, (8, 25, 35), (0, 0, 800, 577))  # sky
    rect(screen, (37, 54, 5), (0, 577, 800, 423))  # ground


def moon_draw():
    circle(screen, (255, 255, 255), (510, 300), 130)  # moon


def clouds_draw():
    ellipse(screen, (110, 110, 110), (480, -20, 650, 110))  # light gray


pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1000))
pygame.display.set_caption("Alien and apple")

picture_draw()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
