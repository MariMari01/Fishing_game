'''
File: Final_main.py
Authors: Sarena, Aspen, and Sam
This file contains the main build for the fishing game. 
'''



import pygame
from fish_classes import AtlanticBass, Clownfish, HighFinBandedShark
from fisher_cat_class import FisherCat
from score import Scoreboard


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()

#Window set up
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
run = True
pygame.display.set_caption('Fish Game')
clock = pygame.time.Clock()


# Load the background image
background_image = pygame.image.load('background.jpg')  # Replace 'background.png' with the actual image file name

# Resize the background image to fit the window
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Create fish objects
atlantic_bass = AtlanticBass(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 150)
clownfish = Clownfish(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)
high_fin_banded_shark = HighFinBandedShark(WINDOW_WIDTH // 2 + 100, WINDOW_HEIGHT // 2 + 75)

#Create cat fisherman
cat = FisherCat(150, 100, WINDOW_WIDTH, WINDOW_HEIGHT)

# Create the scoreboard object
scoreboard = Scoreboard()

pygame.key.set_repeat(True)


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
    if cat.bob_rect.colliderect(atlantic_bass.rect):
        scoreboard.increase_score(atlantic_bass.points)
        
    if cat.bob_rect.colliderect(clownfish.rect):
        scoreboard.increase_score(clownfish.points)
        
    if cat.bob_rect.colliderect(high_fin_banded_shark.rect):
        scoreboard.increase_score(high_fin_banded_shark.points)
        
    # Update fish positions
    atlantic_bass.update(WINDOW_WIDTH, WINDOW_HEIGHT)
    clownfish.update(WINDOW_WIDTH, WINDOW_HEIGHT)
    high_fin_banded_shark.update(WINDOW_WIDTH, WINDOW_HEIGHT)

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Draw the fish
    atlantic_bass.draw(window)
    clownfish.draw(window)
    high_fin_banded_shark.draw(window)
    cat.draw(window)
    
    # Draw the scoreboard
    scoreboard.draw(window)
    
    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

pygame.quit()   
