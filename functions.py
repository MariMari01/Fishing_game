"""Fishing Game by Sam, Sarena, and Aspen
Misc. Functions for the game.
"""

from pathlib import Path
from os import listdir
import pygame


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
    try:
        path = Path(folder_name)
        abs_path = Path(path).resolve()
        for images in listdir(abs_path):
            if images == file_name:
                found_image = images
        str_abs_path = str(abs_path)
        file_abs = str_abs_path + "/" + found_image # Concatonates the file to the absolute path
        return file_abs
    except NameError:
        return "Wrong file name"

def background_music():
    """Allows the background music to play throughout the gameplay.
    """
    bg_music_file = folder_search("sound_files", "background_music.wav")
    pygame.mixer.music.load(bg_music_file)
    pygame.mixer.music.play()

def music_end():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

def final_music():
    final_music_file = folder_search("sound_files", "ultimate_catch.wav")
    pygame.mixer.music.load(final_music_file)
    pygame.mixer.music.play()

def fish_caught_sound():
    """Allows a splash sound to play when the function is called.
    """
    sound_effect = folder_search("sound_files", "splash_sound.wav")
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(sound_effect))

def game_over_sound():
    """Plays when the user loses the game
    """
    sound_effect = folder_search("sound_files", "game_over_sound.wav")
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(sound_effect))

def you_won_sound():
    """Allows a splash sound to play when the function is called.
    """
    sound_effect = folder_search("sound_files", "you_won_sound.wav")
    pygame.mixer.Channel(2).play(pygame.mixer.Sound(sound_effect))

def cat_animation(window, x,y):
    """Animates the cat while it casts the fishing line

    Args:
        x (object.rect.left): The x coordinate of the cat.
        y (object.rect.top): The y coordinate of the cat.
    """
    ship_cat1 = folder_search("misc_sprites_and_background", "ship_cat_1.png")
    ship_cat2 = folder_search("misc_sprites_and_background", "ship_cat_2.png")
    ship_cat3 = folder_search("misc_sprites_and_background", "ship_cat_3.png")

    cat_ship_sprite = [pygame.image.load(ship_cat2),
                        pygame.image.load(ship_cat3),
                        pygame.image.load(ship_cat2),
                        pygame.image.load(ship_cat1)]
    clock = pygame.time.Clock()
    value = 0
    run = True
    while run:
        if value >= len(cat_ship_sprite):
            value = 0
            run = False
        clock.tick(len(cat_ship_sprite))
        image = cat_ship_sprite[value]
        window.blit(image, (x,y))
        pygame.display.update()
        value += 1

def game_won(screen, window_width, window_height):
    """Triggers the game won.
    """
    font = pygame.font.SysFont("Times New Roman", 36)
    text_color = (255, 255, 255)
    position = (window_width//2, window_height//2)
    score_text = font.render("YOU WON", True, text_color)
    screen.blit(score_text, position)
    music_end()
    you_won_sound()

