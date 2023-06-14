"""Fishing game by Sam, Sarena, and Aspen
Start Screen Encylopedia
"""
import pygame
import functions as f
from classes import Button
import encyclopedia_funcs as e


def show_encyclopedia(func):
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
    bg_img = f.folder_search("misc_sprites_and_background", "background.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Button setup
    button_width = 250
    button_height = 50
    button_margin = 20
    button_color = (0, 0, 50) # Dark Blue

    buttons = [
        Button("Common Fish", WINDOW_WIDTH // 2 - button_width // 2,
               WINDOW_HEIGHT // 2 - 2.5 * button_height - 2 * button_margin, button_width,
               button_height, button_color),
        Button("Uncommon Fish", WINDOW_WIDTH // 2 - button_width // 2,
               WINDOW_HEIGHT // 2 - 1.5 * button_height - button_margin,
               button_width, button_height, button_color),
        Button("Rare Fish", WINDOW_WIDTH // 2 - button_width // 2,
               WINDOW_HEIGHT // 2 - 0.5 * button_height, button_width,
               button_height, button_color),
        Button("Ultimate Fish", WINDOW_WIDTH // 2 - button_width // 2,
               WINDOW_HEIGHT // 2 + 0.5 * button_height + button_margin,
               button_width, button_height, button_color),
        Button("Back", WINDOW_WIDTH // 2 - button_width // 2,
               WINDOW_HEIGHT // 2 + 1.5 * button_height + 2 * button_margin,
               button_width, button_height, button_color)
    ]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons:
                    if button.is_mouse_over():
                        if button.text == "Common Fish":
                            e.common_fish(show_encyclopedia, func)
                        elif button.text == "Uncommon Fish":
                            e.uncommon_fish(show_encyclopedia, func)
                        elif button.text == "Rare Fish":
                            e.rare_fish(show_encyclopedia, func)
                        elif button.text == "Ultimate Fish":
                            e.ultimate_fish(show_encyclopedia, func)
                        elif button.text == "Back":
                            func()
                            return

        window.blit(background_image, (0, 0))

        for button in buttons:
            if button.is_mouse_over():
                button.draw(window)
            else:
                button.draw(window)

        pygame.display.flip()
        clock.tick(60)


