import pygame
from pygame.locals import *

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.text_color = (255, 255, 255)
        self.position = (10, 10)

    def increase_score(self, points):
        self.score += points

    def draw(self, screen):
        score_text = self.font.render("Score: " + str(self.score), True, self.text_color)
        screen.blit(score_text, self.position)
