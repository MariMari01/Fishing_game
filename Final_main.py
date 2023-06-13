'''
File: Final_main.py
Authors: Sarena, Aspen, and Sam
This file contains the main build for the fishing game. 
'''

import pygame
from functions import background_music, fish_caught_sound, cat_animation
from fish_classes import Common, Uncommon, Rare
from ultimate_catch import UltimateCatch
from fisher_cat_class import FisherCat
from score import Scoreboard
#from mini_game import mini_game
from model import folder_search
from cast_bar import CastBar
pygame.init()
pygame.mixer.init()

#Window set up
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
run = True
pygame.display.set_caption('Fish Game')
clock = pygame.time.Clock()


# Load the background image
bg_img = folder_search("misc_sprites_and_background", "background.png")
background_image = pygame.image.load(bg_img)
# Resize the background image to fit the window
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))


castbar = CastBar()
# Create fish objects
common_fish = Common(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 80)
uncommon_fish = Uncommon(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70)
rare_fish = Rare(WINDOW_WIDTH // 2 + 100, WINDOW_HEIGHT // 2 + 260)
ultimate_catch = UltimateCatch(WINDOW_WIDTH // 2 +100, WINDOW_HEIGHT // 2 + 150)
#minigame = mini_game(5)



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
                castbar.move_up()
                cat.ready_cast()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                castbar.fill_height = 0
                castbar.bar_ypos = 215
                cat_animation(window, cat.rect.left, cat.rect.top)
                cat.cast()
    # Check for collision between the fishing bob and the fish
    if cat.bob_rect.colliderect(common_fish.rect):

        fish_caught_sound()

        fish_caught_points = common_fish.points
        cat.reset_bob()
        scoreboard.increase_score(fish_caught_points)
        fish_caught_sound()
    if cat.bob_rect.colliderect(uncommon_fish.rect):

        fish_caught_sound()

        fish_caught_points = uncommon_fish.points
        cat.reset_bob()
        scoreboard.increase_score(fish_caught_points)
        fish_caught_sound()
    if cat.bob_rect.colliderect(rare_fish.rect):

        fish_caught_sound()

        fish_caught_points = rare_fish.points
        cat.reset_bob()
        scoreboard.increase_score(fish_caught_points)
        fish_caught_sound()
    if cat.bob_rect.colliderect(ultimate_catch.rect):

        fish_caught_sound()

        fish_caught_points = ultimate_catch.points
        cat.reset_bob()
        scoreboard.increase_score(fish_caught_points)
        fish_caught_sound()


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
    #ultimate_catch.draw(window)
    cat.draw(window)
    castbar.draw(window)
    castbar.fill(window)

    # Draw the scoreboard
    scoreboard.draw(window)
    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
pygame.quit()
