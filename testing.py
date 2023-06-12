import random
from pathlib import Path
from os import listdir

def image_list_from_folder(folder_name):
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
    return rand_choice

found_images = image_list_from_folder("common_fish_game")
print(found_images)


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


