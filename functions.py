from model import folder_search
from pathlib import Path
from os import listdir
import pygame

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
