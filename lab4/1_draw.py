import pygame
from pygame.draw import *


def drawface():
    circle(screen, (255, 255, 0), (250, 250), 150)  # yellow
    circle(screen, (0, 0, 0), (250, 250), 150, 3)  # black


def draweyes():
    circle(screen, (255, 0, 0), (180, 220), 35)  # red left
    circle(screen, (0, 0, 0), (180, 220), 12)  # black left
    circle(screen, (0, 0, 0), (180, 220), 35, 3)  # black left
    circle(screen, (255, 0, 0), (320, 220), 25)  # red right
    circle(screen, (0, 0, 0), (320, 220), 12)  # black right
    circle(screen, (0, 0, 0), (320, 220), 25, 3)  # black right


def drawmouth():
    rect(screen, (0, 0, 0), (180, 320, 140, 35))


def droweyebrows():
    line(screen, (0, 0, 0), (100, 125), (230, 199), 20)  # left
    line(screen, (0, 0, 0), (280, 195), (400, 165), 18)  # right


pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
screen.fill((192, 192, 192))

drawface()
draweyes()
drawmouth()
droweyebrows()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
