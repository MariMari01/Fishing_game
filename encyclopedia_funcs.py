"""Fishing Game by Same, Sarena, and Aspen
Encyclopedia for the start screen.
"""
import pygame
import functions as f
from classes import Button

def common_fish(func1, func2):
    """Code to show the fish encyclopedia goes here
    """

    pygame.init()
    pygame.mixer.init()

    # Window setup
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption('Fish Game - Fish Encyclpedia')
    clock = pygame.time.Clock()

    # Load the background image
    bg_img = f.folder_search("common_fish_encyclopedia", "all_common_fish.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Button setup
    button_width = 250
    button_height = 50
    button_margin = 20
    button_color = (0, 0, 50) # Dark Blue

    button = Button("Back", WINDOW_WIDTH // 2 - button_width // 2,
                    WINDOW_HEIGHT // 2 + 3.5 * button_height + 2 * button_margin,
                    button_width, button_height, button_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.is_mouse_over():
                    if button.text == "Back":
                        func1(func2)
                        return

        window.blit(background_image, (0, 0))

        if button.is_mouse_over():
            button.draw(window)
        else:
            button.draw(window)

        pygame.display.flip()
        clock.tick(60)

def uncommon_fish(func1,func2):
    """Code to show the fish encyclopedia goes here
    """

    pygame.init()
    pygame.mixer.init()

    # Window setup
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True
    pygame.display.set_caption('Fish Game - Fish Encyclpedia')
    clock = pygame.time.Clock()

    # Load the background image
    bg_img = f.folder_search("uncommon_fish_encyclopedia", "all_uncommon_fish.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Button setup
    button_width = 250
    button_height = 50
    button_margin = 20
    button_color = (0, 0, 50) # Dark Blue

    button = Button("Back", WINDOW_WIDTH // 2 - button_width // 2,
                    WINDOW_HEIGHT // 2 + 3.5 * button_height + 2 * button_margin,
                    button_width, button_height, button_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.is_mouse_over():
                    if button.text == "Back":
                        func1(func2)
                        return

        window.blit(background_image, (0, 0))

        if button.is_mouse_over():
            button.draw(window)
        else:
            button.draw(window)

        pygame.display.flip()
        clock.tick(60)

def rare_fish(func1,func2):
    """Code to show the fish encyclopedia goes here
    """

    pygame.init()
    pygame.mixer.init()

    # Window setup
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True
    pygame.display.set_caption('Fish Game - Fish Encyclpedia')
    clock = pygame.time.Clock()

    # Load the background image
    bg_img = f.folder_search("rare_fish_encyclopedia", "all_rare_fish.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Button setup
    button_width = 250
    button_height = 50
    button_margin = 20
    button_color = (0, 0, 50) # Dark Blue

    button = Button("Back", WINDOW_WIDTH // 2 - button_width // 2,
                    WINDOW_HEIGHT // 2 + 3.5 * button_height + 2 * button_margin,
                    button_width, button_height, button_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.is_mouse_over():
                    if button.text == "Back":
                        func1(func2)
                        return

        window.blit(background_image, (0, 0))

        if button.is_mouse_over():
            button.draw(window)
        else:
            button.draw(window)

        pygame.display.flip()
        clock.tick(60)

def ultimate_fish(func1,func2):
    """Code to show the fish encyclopedia goes here
    """
    # 
    pygame.init()
    pygame.mixer.init()

    # Window setup
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True
    pygame.display.set_caption('Fish Game - Fish Encyclpedia')
    clock = pygame.time.Clock()

    # Load the background image
    bg_img = f.folder_search("ultimate_fish_encyclopedia", "all_ultimate_fish.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Button setup
    button_width = 250
    button_height = 50
    button_margin = 20
    button_color = (0, 0, 50) # Dark Blue

    button = Button("Back", WINDOW_WIDTH // 2 - button_width // 2,
                    WINDOW_HEIGHT // 2 + 3.5 * button_height + 2 * button_margin, button_width,
                    button_height, button_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.is_mouse_over():
                    if button.text == "Back":
                        func1(func2)
                        return

        window.blit(background_image, (0, 0))

        if button.is_mouse_over():
            button.draw(window)
        else:
            button.draw(window)

        pygame.display.flip()
        clock.tick(60)
