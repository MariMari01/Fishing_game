"""Fishing Game by Sam, Sarena, and Aspen
Main Module for the Fishing Game
"""

import pygame
import functions as f
from classes import Button
from show_controls import show_controls
from show_encyclopedia import show_encyclopedia
from show_story import show_story
from start_game import start_game


def main():
    """Game Function
    """
    pygame.init()
    pygame.mixer.init()

    # Window setup
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True
    pygame.display.set_caption('Fish Game - Main Menu')
    clock = pygame.time.Clock()

    # Load the background image
    bg_img = f.folder_search("misc_sprites_and_background", "start_screen_background.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Button setup
    button_width = 250
    button_height = 50
    button_margin = 20
    button_color = (0, 0, 50) # Dark Blue

    buttons = [
        Button("Start Game", WINDOW_WIDTH // 2 + 250 - button_width // 2,
               WINDOW_HEIGHT // 2 - 2.5 * button_height - 2 * button_margin,
               button_width, button_height, button_color),
        Button("Background Story", WINDOW_WIDTH // 2 + 250 - button_width // 2,
               WINDOW_HEIGHT // 2 - 1.5 * button_height - button_margin, button_width,
               button_height, button_color),
        Button("Fish Encyclopedia", WINDOW_WIDTH // 2 + 250 - button_width // 2,
               WINDOW_HEIGHT // 2 - 0.5 * button_height, button_width, button_height, button_color),
        Button("Controls", WINDOW_WIDTH // 2 + 250 - button_width // 2,
               WINDOW_HEIGHT // 2 + 0.5 * button_height + button_margin,
               button_width, button_height, button_color),
        Button("Quit", WINDOW_WIDTH // 2 + 250 - button_width // 2,
               WINDOW_HEIGHT // 2 + 1.5 * button_height + 2 * button_margin,
               button_width, button_height, button_color)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons:
                    if button.is_mouse_over():
                        if button.text == "Start Game":
                            start_game()
                        elif button.text == "Background Story":
                            show_story(main)
                        elif button.text == "Fish Encyclopedia":
                            show_encyclopedia(main)
                        elif button.text == "Controls":
                            show_controls(main)
                        elif button.text == "Quit":
                            pygame.quit()
                            return

        window.blit(background_image, (0, 0))

        for button in buttons:
            if button.is_mouse_over():
                button.draw(window)
            else:
                button.draw(window)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":

    main()
