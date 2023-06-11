import pygame
from fish_classes import Fish

class UltimateCatch(Fish):
    def __init__(self, x, y):
        super().__init__(x, y-100, speed=10, points=50)
        self.image = pygame.image.load('ultimate_catch.png')  # Replace 'moonfish.png' with the actual image file name

