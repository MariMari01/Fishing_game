import pygame
import random
from fish_classes import Fish

class UltimateCatch(Fish):
    def __init__(self, x, y):
        super().__init__(x, y, speed=10, points=50)
        self.found_fish = self.image_list_from_folder("ultimate_fish_game")
        self.image = pygame.image.load(self.found_fish)
