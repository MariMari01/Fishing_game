import pygame
import random
from pathlib import Path
from os import listdir

class Fish:
    def __init__(self, x, y, speed, points):
        self.x = x
        self.y = y
        self.image_choice = self.image_list_from_folder("common_fish_game")
        self.image = pygame.image.load(self.image_choice)  # Replace 'fish.png' with the actual image file name
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
    
    def image_list_from_folder(self,folder_name):
        """Function creeates an absolute path for a folder
        and creates a list of the images found.

        Args:
            folder_name (folder file): A folder that holds files for the game
            file_name (.png or .wav): A file that will be used in the game,
            either a .png or a .wav file

        Returns:
            str: The absolute path and file name are returned as strings.
        """
        path = Path(folder_name)
        abs_path = Path(path).resolve()
        file_images = []
        for images in listdir(abs_path):
            file_images.append(images)
        rand_choice = random.choice(file_images)
        str_abs_path = str(abs_path)
        image_choice = str_abs_path + "/" + rand_choice
        return image_choice


class Common(Fish):
    def __init__(self, x, y):
        super().__init__(x, y-50, speed=2, points=5)
        self.found_fish = self.image_list_from_folder("common_fish_game")
        pygame.image.load(self.found_fish)  # Replace 'red_snapper.png' with the actual image file name


class Uncommon(Fish):
    def __init__(self, x, y):
        super().__init__(x, y-200, speed=4, points=10)
        self.found_fish = self.image_list_from_folder("uncommon_fish_game")
        self.image = pygame.image.load(self.found_fish)  # Replace 'cod.png' with the actual image file name


class Rare(Fish):
    def __init__(self, x, y):
        super().__init__(x, y+200, speed=6, points=15)
        self.found_fish = self.image_list_from_folder("rare_fish_game")
        self.image = pygame.image.load(self.found_fish)  # Replace 'moonfish.png' with the actual image file name
