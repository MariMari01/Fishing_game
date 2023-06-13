'''
This file contains the class for the fishing 
cat player character
'''
import pygame
from model import folder_search
class FisherCat:
    '''
    This class contains the methods and attributes 
    of the fisher man cat
    '''
    def __init__(self,x,y, window_x, window_y) -> None:
        self.fishing_hook = folder_search("misc_sprites_and_background", "fishing_hook.png")
        self.fishing_bob = pygame.image.load(self.fishing_hook)

        self.cat_ship = folder_search("misc_sprites_and_background", "ship_cat_1.png")
        self.image = pygame.image.load(self.cat_ship)

        self.rect = self.image.get_rect()
        self.bob_rect = self.fishing_bob.get_rect()


        self.xpos = x
        self.ypos = y

        self.cast_distance = 0
        self.win_x = window_x
        self.win_y = window_y

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


    def reset_bob(self):
        self.bob_rect.center = (self.xpos, self.ypos)


    def ready_cast(self):
        '''
        readies the cast by increasing the distance the bob is thrown
        while read_cast is being called. 
        '''
        self.bob_rect.center = (self.xpos, self.ypos)
        self.cast_distance += 1
        if self.cast_distance >= self.win_y - self.ypos:
            self.cast_distance = self.win_y - self.ypos - 30


    def cast(self):
        '''
        Casts the fishing rod 
        '''

        self.bob_rect.center = (self.xpos, self.ypos + self.cast_distance)
        self.cast_distance = 0
