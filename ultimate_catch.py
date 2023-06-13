import pygame
import random
import time
from fish_classes import Fish

class UltimateCatch(Fish):
    def __init__(self, x, y):
        super().__init__(x, y, speed=20, points=500)
        self.found_fish = self.image_list_from_folder("ultimate_fish_game")
        self.image = pygame.image.load(self.found_fish)
    
    def update(self, screen_width, screen_height):
        self.x += self.speed
        if self.x >= screen_width:
            self.found_fish = self.image_list_from_folder("ultimate_fish_game")
            self.image = pygame.image.load(self.found_fish)
            self.x = 0
            rand_int = random.randint(-180, 170)
            self.y = 383 + rand_int

        self.rect.center = (self.x, self.y)
