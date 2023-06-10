'''This file contains the class for the fishing 
cat player character
'''

import pygame

class FisherCat:
    '''
    This class contains the methods and attributes 
    of the fisher man cat
    '''
    def __init__(self,x,y, window_x) -> None:
        self.fishing_bob = pygame.image.load("fishing_bob.png")
        self.image = pygame.image.load("Ship_full.png")
        self.rect = self.image.get_rect()
        self.bob_rect = self.fishing_bob.get_rect()
        self.xpos = x
        self.ypos = y
        self.win_x = window_x
    
    def draw(self, screen):
        '''
        Draws the fisher cat object onto the screen
        '''
        screen.blit(self.fishing_bob, self.bob_rect)
        screen.blit(self.image, self.rect)

    def move_left(self):
        '''
        Moves the fisher cat left
        '''
        if self.xpos == 0:
            pass
        else:
            self.xpos -= 0.5
            self.rect.center = (self.xpos, self.ypos)
            self.bob_rect.center = (self.xpos, self.ypos)

    def move_right(self):
        '''
        Moves the fisher cat right
        '''
        if self.xpos == self.win_x:
            pass
        else:
            self.xpos += 0.5
            self.rect.center = (self.xpos, self.ypos)
            self.rect.center = (self.xpos, self.ypos)
            self.bob_rect.center = (self.xpos, self.ypos)


    def cast(self):
        '''
        Casts the fishing rod 
        '''
        self.bob_rect.center = (self.xpos, self.ypos + 400)
