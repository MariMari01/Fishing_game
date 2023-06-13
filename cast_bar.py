import pygame
import random


class CastBar:

    def __init__(self) -> None:
        self.fill_height = 0
        self.bottom = 258
        self.top = 102
        self.color = (146, 240, 235)
        self.fill_color = (11, 252, 3)
        self.xpos = 42
        self.bar_ypos = 215
        self.minigame_fishpos = 42

    def draw(self, window):
        # Drawing Rectangle
        pygame.draw.rect(window, self.color, pygame.Rect(700, 100, 30, 120))

    def fill_up(self):
        '''
        Moves the mini game bar up
        '''
        if self.bar_ypos <= self.top:
            pass
        else:
            self.fill_height += 0.25
            self.bar_ypos -= 0.25

    def fill(self, window):
        self.rectangle = pygame.draw.rect(window, self.fill_color, pygame.Rect(702, self.bar_ypos, 26, self.fill_height))
    
