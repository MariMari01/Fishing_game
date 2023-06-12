'''
File: Final_main.py
Authors: Sarena, Aspen, and Sam
This file contains the main build for the fishing game. 
'''

import pygame

from pathlib import Path
from os import listdir

from fish_classes import Common, Uncommon, Rare
from ultimate_catch import UltimateCatch
from fisher_cat_class import FisherCat
from score import Scoreboard

pygame.init()
pygame.mixer.init()

#Window set up
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
run = True
pygame.display.set_caption('Fish Game')
clock = pygame.time.Clock()

def folder_search(folder_name, file_name):
    """Function creeates an absolute path for a folder
    and searches the folder for a file.

    Args:
        folder_name (folder file): A folder that holds files for the game
        file_name (.png or .wav): A file that will be used in the game,
        either a .png or a .wav file

    Returns:
        str: The absolute path and file name are returned as strings.
    """
    path = Path(folder_name)
    abs_path = Path(path).resolve()
    for images in listdir(abs_path):
        if images == file_name:
            found_image = images
    str_abs_path = str(abs_path)
    file_abs = str_abs_path + "/" + found_image # Concatonates the file to the absolute path
    return file_abs

# Load the background image
bg_img = folder_search("misc_sprites_and_background", "background.png")
background_image = pygame.image.load(bg_img)
# Resize the background image to fit the window
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

def background_music():
    """Allows the background music to play throughout the gameplay.
    """
    bg_music_file = folder_search("sound_files", "background_music.wav")
    pygame.mixer.music.load(bg_music_file)
    pygame.mixer.music.play(-1)

def fish_caught_sound():
    """Allows a splash sound to play when the function is called.
    """
    sound_effect = folder_search("sound_files", "splash_sound.wav")
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(sound_effect))

# Create fish objects
common_fish = Common(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 80)
uncommon_fish = Uncommon(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70)
rare_fish = Rare(WINDOW_WIDTH // 2 + 100, WINDOW_HEIGHT // 2 + 260)
ultimate_catch = UltimateCatch(WINDOW_WIDTH // 2 +100, WINDOW_HEIGHT // 2 + 150)

#Create cat fisherman
cat = FisherCat(150, 100, WINDOW_WIDTH, WINDOW_HEIGHT)

# Create the scoreboard object
scoreboard = Scoreboard()

pygame.key.set_repeat(True)
background_music()

while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                cat.move_right()
            elif event.key == pygame.K_a:
                cat.move_left()
            elif event.key == pygame.K_e:
                cat.ready_cast()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                cat.cast()

    # Check for collision between the fishing bob and the fish
    if cat.bob_rect.colliderect(common_fish.rect):
        fish_caught_sound()
        scoreboard.increase_score(common_fish.points)
        cat.reset_bob()
    if cat.bob_rect.colliderect(uncommon_fish.rect):
        fish_caught_sound()
        scoreboard.increase_score(uncommon_fish.points)
        cat.reset_bob()
    if cat.bob_rect.colliderect(rare_fish.rect):
        fish_caught_sound()
        scoreboard.increase_score(rare_fish.points)
        cat.reset_bob()
    if cat.bob_rect.colliderect(ultimate_catch.rect):
        fish_caught_sound()
        scoreboard.increase_score(ultimate_catch.points)
        cat.reset_bob()

    # Update fish positions
    common_fish.update(WINDOW_WIDTH, WINDOW_HEIGHT)
    uncommon_fish.update(WINDOW_WIDTH, WINDOW_HEIGHT)
    rare_fish.update(WINDOW_WIDTH, WINDOW_HEIGHT)
    ultimate_catch.update(WINDOW_WIDTH,WINDOW_HEIGHT)

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Draw the fish
    # -----------------------------------------------------------
    # Uncomment ultimate_catch to see how it looks on screen!
    # -----------------------------------------------------------
    common_fish.draw(window)
    uncommon_fish.draw(window)
    rare_fish.draw(window)
    # ultimate_catch.draw(window)
    cat.draw(window)

    # Draw the scoreboard
    scoreboard.draw(window)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
pygame.quit()

