import pygame

class Fish:
    def __init__(self, x, y, speed, points):
        self.x = x
        self.y = y
        self.image = pygame.image.load('blue_fish.png')  # Replace 'fish.png' with the actual image file name
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = speed
        self.points = points

    def update(self, screen_width, screen_height):
        self.x += self.speed
        if self.x > screen_width:
            self.x = 0
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
class AtlanticBass(Fish):
    def __init__(self, x, y):
        super().__init__(x, y, speed=3, points=10)
        pygame.image.load('blue_fish.png')  # Replace 'red_snapper.png' with the actual image file name


class Clownfish(Fish):
    def __init__(self, x, y):
        super().__init__(x, y, speed=5, points=15)
        self.image = pygame.image.load('orange_fish.png')  # Replace 'cod.png' with the actual image file name


class HighFinBandedShark(Fish):
    def __init__(self, x, y):
        super().__init__(x, y, speed=2, points=5)
        self.image = pygame.image.load('black_fish.png')  # Replace 'moonfish.png' with the actual image file name


# Get image from sprite sheet
# sprite_sheet_image = pygame.image.load('global.png').convert_alpha()
# def get_image(sheet, frame, width, height, scale):
#     image = pygame.Surface((width, height)).convert_alpha()
#     image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
#     image = pygame.transform.scale(image, (width * scale, height * scale))
#     return image
# frame_0 = get_image(sprite_sheet_image, 0, 18, 16, 3)
# frame_1 = get_image(sprite_sheet_image, 1, 16, 16, 3)
# frame_2 = get_image(sprite_sheet_image, 2, 15, 16, 3)