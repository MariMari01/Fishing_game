'''
File: Final_main.py
Authors: Sarena, Aspen, and Sam
This file contains the main build for the fishing game. 
'''
import time
import pygame
from functions import folder_search, background_music, fish_caught_sound, music_end, GameOver, final_music
from fish_classes import Common, Uncommon, Rare
from ultimate_catch import UltimateCatch
from fisher_cat_class import FisherCat
from score import Scoreboard
from mini_game import mini_game


pygame.init()

#Clock variables
clock = pygame.time.Clock()
counter = 113
font = pygame.font.SysFont(None, 36)
text_color = (255, 255, 255)
position = (640, 11)
text = font.render("Time: " + str(counter), True, text_color)
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

pygame.mixer.init()

#Window set up
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
run = True
pygame.display.set_caption('Fish Game')


# Load the background image
bg_img = folder_search("misc_sprites_and_background", "background.png")
background_image = pygame.image.load(bg_img)
# Resize the background image to fit the window
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))



catching = False
fish_caught_points = None
# Create fish objects
common_fish = Common(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 80)
uncommon_fish = Uncommon(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70)
rare_fish = Rare(WINDOW_WIDTH // 2 + 100, WINDOW_HEIGHT // 2 + 260)
ultimate_catch = UltimateCatch(WINDOW_WIDTH // 2 +100, WINDOW_HEIGHT // 2 + 150)
minigame = mini_game(5)
game_over = GameOver(WINDOW_WIDTH, WINDOW_HEIGHT)



#Create cat fisherman
cat = FisherCat(150, 100, WINDOW_WIDTH, WINDOW_HEIGHT)

# Create the scoreboard object
scoreboard = Scoreboard()

pygame.key.set_repeat(True)
background_music()

catch_points = 0

while run:
    pygame.display.update()

    if catching:
        minigame.draw_minigame_fish(window)
        if minigame.rectangle.colliderect(minigame.fish_rect):
            catch_points += 0.5

            print(catch_points)
        if catch_points >= 100:
            scoreboard.increase_score(fish_caught_points)
            fish_caught_sound()
            catch_points = 0
            catching = False

        minigame.move_minigame_fish()

    for event in pygame.event.get():
        if catching and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                minigame.move_up(minigame.rectangle)
            if event.key == pygame.K_s:
                minigame.move_down(minigame.rectangle)

        if event.type == pygame.QUIT:
            run = False
        elif event.type == timer_event:
            counter -= 1
            text = font.render("Time: " + str(counter), True, text_color)
            if counter == 0 and scoreboard.score < 1000:
                pygame.time.set_timer(timer_event, 0)
                game_over.draw(window)

        if not catching and counter > 0 and event.type  == pygame.KEYDOWN:
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
        catching = True
        fish_caught_sound()
        minigame.speed = 5
        fish_caught_points = common_fish.points
        cat.reset_bob()

    if cat.bob_rect.colliderect(uncommon_fish.rect):
        catching = True
        fish_caught_sound()
        minigame.speed = 7
        fish_caught_points = uncommon_fish.points
        cat.reset_bob()

    if cat.bob_rect.colliderect(rare_fish.rect):
        catching = True
        fish_caught_sound()
        minigame.speed = 10
        fish_caught_points = rare_fish.points
        cat.reset_bob()

    if cat.bob_rect.colliderect(ultimate_catch.rect):
        catching = True
        fish_caught_sound()
        minigame.speed = 15
        fish_caught_points = ultimate_catch.points
        cat.reset_bob()
        ultimate_catch.game_won(window, WINDOW_WIDTH, WINDOW_HEIGHT)
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
    cat.draw(window)
    ultimate_catch.draw(window)


    minigame.draw(window)
    if catching:
        minigame.fill(window)
    # Draw the scoreboard
    scoreboard.draw(window)
    window.blit(text, position)
    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
pygame.quit()

