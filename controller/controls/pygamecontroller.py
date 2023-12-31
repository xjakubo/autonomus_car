import pygame
import sys

class Pygame_Controller:

    SCREEN_WIDTH, SCREEN_HEIGHT = 400,300

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,
                                               self.SCREEN_HEIGHT))
        pygame.display.set_caption("Test pilot")

    def checkForControllerInput(self) -> tuple:
        speed = 0
        direction = 0
        steerprecentage = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            speed = 40
            direction = True
            steerprecentage = -100
        if keys[pygame.K_a]:
            steerprecentage = -100
        if keys[pygame.K_s]:
            speed = 40
            direction = False
        if keys[pygame.K_d]:
            steerprecentage = 100
        if keys[pygame.K_q]:
            speed = 100
            direction = True
        return speed, direction, steerprecentage

    def checkForOtherEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
