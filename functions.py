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
    path = Path(folder_name)
    abs_path = Path(path).resolve()
    for images in listdir(abs_path):
        if images == file_name:
            found_image = images
    str_abs_path = str(abs_path)
    file_abs = str_abs_path + "/" + found_image # Concatonates the file to the absolute path
    return file_abs
    

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
