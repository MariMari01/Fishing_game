"""Fishing Game by Sam, Sarena, and Aspen
Fish parent class and Common, Uncommon, Rare, and Ultimate child classes.
"""

from pathlib import Path
from os import listdir
import random
import pygame


class Fish:
    """Fish parent class for common, uncommon, rare, and ultimate fish.
    """

    def __init__(self, x, y, speed, points):
        """Speed, location, and points for fish subclasses.
        """
        self.x = x
        self.y = y
        self.folder_name = "common_fish_game"
        self.image_choice = self.image_list_from_folder(self.folder_name)
        # Replace 'self.image_choice' with the image file name and path
        self.image = pygame.image.load(self.image_choice)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = speed
        self.points = points

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

    def draw(self, screen):
        """Draws the fish onto the screen
        """
        screen.blit(self.image, self.rect)

class Common(Fish):
    """Common Fish
    """
    def __init__(self, x, y):
        """Speed and points for common fish.
        """
        super().__init__(x, y, speed=2, points=5)
        self.found_fish = self.image_list_from_folder("common_fish_game")
        pygame.image.load(self.found_fish)

    def update(self, screen_width, screen_height):
        """Updates the screen.
        """
        self.x += self.speed
        if self.x >= screen_width:
            self.found_fish = self.image_list_from_folder("common_fish_game")
            self.image = pygame.image.load(self.found_fish)
            self.x = 0
            rand_int = random.randint(-180, 170)
            self.y = 383 + rand_int
        self.rect.center = (self.x, self.y)

class Uncommon(Fish):
    """Uncommon Fish
    """
    def __init__(self, x, y):
        """Speed and points for uncommon fish.
        """
        super().__init__(x, y, speed=6, points=10)
        self.found_fish = self.image_list_from_folder("uncommon_fish_game")
        self.image = pygame.image.load(self.found_fish)

    def update(self, screen_width, screen_height):
        """Updates the location of uncommon fish.
        """
        self.x += self.speed
        if self.x >= screen_width:
            self.found_fish = self.image_list_from_folder("uncommon_fish_game")
            self.image = pygame.image.load(self.found_fish)
            self.x = 0
            rand_int = random.randint(-180, 170)
            self.y = 383 + rand_int
        self.rect.center = (self.x, self.y)

class Rare(Fish):
    """Rare fish
    """
    def __init__(self, x, y):
        """Speed and Points of the rare fish.
        """
        super().__init__(x, y, speed=8, points=15)
        self.found_fish = self.image_list_from_folder("rare_fish_game")
        self.image = pygame.image.load(self.found_fish)

    def update(self, screen_width, screen_height):
        """Updates the screen for rare fish.
        """
        self.x += self.speed
        if self.x >= screen_width:
            self.found_fish = self.image_list_from_folder("rare_fish_game")
            self.image = pygame.image.load(self.found_fish)
            self.x = 0
            rand_int = random.randint(-180, 170)
            self.y = 383 + rand_int
        self.rect.center = (self.x, self.y)

class UltimateCatch(Fish):
    """Fish worth the most points

    """
    def __init__(self, x, y):
        """Points speed for ultimate catch

        """
        super().__init__(x, y, speed=15, points=100)
        self.found_fish = self.image_list_from_folder("ultimate_fish_game")
        self.image = pygame.image.load(self.found_fish)

    def update(self, screen_width, screen_height):
        """Updates ultimate catch as it is on screen.
        """
        self.x += self.speed
        if self.x >= screen_width:
            self.found_fish = self.image_list_from_folder("ultimate_fish_game")
            self.image = pygame.image.load(self.found_fish)
            self.x = 0
            rand_int = random.randint(-180, 170)
            self.y = 383 + rand_int

        self.rect.center = (self.x, self.y)

