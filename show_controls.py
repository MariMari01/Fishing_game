import pygame
import functions as f
from classes import Button

def show_controls(func):
    """Displays the controls for the game."""
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
    bg_img = f.folder_search("misc_sprites_and_background", "controls_background.png")
    background_image = pygame.image.load(bg_img)
    # Resize the background image to fit the window
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Button setup
    button_width = 250
    button_height = 50
    button_margin = 20
    button_color = (0, 0, 50) # Dark Blue

    button = Button("Back", WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 3.5 * button_height + 2 * button_margin, button_width, button_height, button_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.is_mouse_over():
                    if button.text == "Back":
                        func()
                        return

        window.blit(background_image, (0, 0))

        if button.is_mouse_over():
            button.draw(window)
        else:
            button.draw(window)

        pygame.display.flip()
        clock.tick(60)
