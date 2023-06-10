import pygame

class FisherCat:
    '''
    This class contains the methods and attributes 
    of the fisher man cat
    '''
    def __init__(self,x,y, window_x) -> None:
        self.image = pygame.image.load("Ship_full.png")
        self.rect = self.image.get_rect()
        self.xpos = x
        self.ypos = y
        self.win_x = window_x
    def move_left(self):
        if self.xpos == 0:
            pass
        else:
            self.xpos -= 0.5
            self.rect.center = (self.xpos, self.ypos)

    def move_right(self):
        if self.xpos == self.win_x:
            pass
        else:
            self.xpos += 0.5
            self.rect.center = (self.xpos, self.ypos)
    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def cast(self):
        pass