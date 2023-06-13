import pygame
import random


class mini_game:

    def __init__(self, speed) -> None:
        self.speed = speed
        self.fill_height = 80
        self.bottom = 258
        self.top = 42
        self.color = (28, 5, 128)
        self.fill_color = (11, 252, 3)
        self.xpos = 42
        self.bar_ypos = 42
        self.minigame_fishpos = 42

    def draw(self, window):
        # Drawing Rectangle
        pygame.draw.rect(window, self.color, pygame.Rect(680, 40, 30, 300))

    def move_down(self, rect):
        '''
        Moves the minigame bar down
        '''
        if self.bar_ypos >= self.bottom:
            pass
        else:
            self.bar_ypos += 0.5
            rect.center = (self.xpos, self.bar_ypos)


    def move_up(self, rect):
        '''
        Moves the mini game bar up
        '''
        if self.bar_ypos <= self.top:
            pass
        else:
            self.bar_ypos -= 0.5
            rect.center = (self.xpos, self.bar_ypos)


    def move_minigame_fish(self):
        chooser = random.randint(0,1)

        if chooser != 0 and self.minigame_fishpos >= self.top:
            self.minigame_fishpos -= self.speed
            self.fish_rect.center = (self.xpos, self.minigame_fishpos)
            chooser = random.randint(0,1)
        elif chooser == 0 and self.minigame_fishpos <= self.bottom:
            self.minigame_fishpos += self.speed
            self.fish_rect.center = (self.xpos, self.minigame_fishpos)
            chooser = random.randint(0,1)
        else:
            pass
        pygame.display.flip()

    def fill(self, window):
        self.rectangle = pygame.draw.rect(window, self.fill_color, pygame.Rect(682, self.bar_ypos, 26, self.fill_height))
    
    def draw_minigame_fish(self, window):
        self.fish_rect = pygame.draw.rect(window, (255, 226, 148), pygame.Rect(682, self.minigame_fishpos, 26, 10))
