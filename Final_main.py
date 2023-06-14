'''
File: Final_main.py
Authors: Sarena, Aspen, and Sam
This file contains the main build for the fishing game. 
'''


import pygame
import functions as f
from fish_classes import Common, Uncommon, Rare, UltimateCatch
from fisher_cat_class import FisherCat
from button import Button


def main_menu():
    pygame.init()
    pygame.mixer.init()

    #Window set up
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True
    pygame.display.set_caption('Fish Game')

    # Set up for the timer functon
    clock = pygame.time.Clock()
    # Change counter for testing
    counter = 113
    font = pygame.font.SysFont(None, 36)
    text_color = (255, 255, 255)
    position = (640, 11)
    text = font.render("Time: " + str(counter), True, text_color)
    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)


    # Load the background image
    bg_img = f.folder_search("misc_sprites_and_background", "background.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    castbar = f.CastBar()
    # Create fish objects
    common_fish = Common(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 80)
    uncommon_fish = Uncommon(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70)
    rare_fish = Rare(WINDOW_WIDTH // 2 + 100, WINDOW_HEIGHT // 2 + 260)
    ultimate_catch = UltimateCatch(WINDOW_WIDTH // 2 +100, WINDOW_HEIGHT // 2 + 150)
    game_over = f.GameOver(WINDOW_WIDTH, WINDOW_HEIGHT)

    #Create cat fisherman
    cat = FisherCat(150, 100, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Create the scoreboard object
    scoreboard = f.Scoreboard()

    pygame.key.set_repeat(True)
    f.background_music()

    catching = False
    fish_caught_points = None
    game_is_over = False
    catch_points = 0
    while run:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == timer_event:
                counter -= 1
                text = font.render("Time: " + str(counter), True, text_color)
                # Change scoreboard.score for testing
                if counter <= 0 and scoreboard.score < 2000:
                    pygame.time.set_timer(timer_event, 0)
                    game_is_over = True
                    game_over.draw(window)
                if counter <= 0 and scoreboard.score >= 2000:
                    pygame.time.set_timer(timer_event, 0)
                    game_is_over = True
                    f.game_won(window, WINDOW_WIDTH, WINDOW_HEIGHT)

            if counter > 0 and event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    cat.move_right()
                elif event.key == pygame.K_a:
                    cat.move_left()
                elif event.key == pygame.K_e:
                    castbar.fill_up()
                    cat.ready_cast()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    castbar.fill_height = 0
                    castbar.bar_ypos = 215
                    f.cat_animation(window, cat.rect.left, cat.rect.top)
                    cat.cast()
        # Check for collision between the fishing bob and the fish
        if cat.bob_rect.colliderect(common_fish.rect):
            catch_points = True
            f.fish_caught_sound()
            fish_caught_points = common_fish.points
            cat.reset_bob()
            scoreboard.increase_score(fish_caught_points)

        if cat.bob_rect.colliderect(uncommon_fish.rect):
            catching = True
            f.fish_caught_sound()
            fish_caught_points = uncommon_fish.points
            cat.reset_bob()
            scoreboard.increase_score(fish_caught_points)

        if cat.bob_rect.colliderect(rare_fish.rect):
            catching = True
            f.fish_caught_sound()
            fish_caught_points = rare_fish.points
            cat.reset_bob()
            scoreboard.increase_score(fish_caught_points)

        if cat.bob_rect.colliderect(ultimate_catch.rect):
            catching = True
            f.fish_caught_sound()
            fish_caught_points = ultimate_catch.points
            cat.reset_bob()
            scoreboard.increase_score(fish_caught_points)



        # Update fish positions
        common_fish.update(WINDOW_WIDTH, WINDOW_HEIGHT)
        uncommon_fish.update(WINDOW_WIDTH, WINDOW_HEIGHT)
        rare_fish.update(WINDOW_WIDTH, WINDOW_HEIGHT)
        ultimate_catch.update(WINDOW_WIDTH,WINDOW_HEIGHT)

        # Draw the background image
        if not game_is_over:
            window.blit(background_image, (0, 0))

        # Draw the fish
            common_fish.draw(window)
            uncommon_fish.draw(window)
            rare_fish.draw(window)
            ultimate_catch.draw(window)

            cat.draw(window)
            castbar.draw(window)
            castbar.fill(window)

        # Draw the scoreboard
            scoreboard.draw(window)
        window.blit(text, position)
        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)
    pygame.quit()

def show_story():
    # Code to display the background story goes here
    # Game code goes here
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



def show_encyclopedia():
    # Code to show the fish encyclopedia goes here
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
    bg_img = folder_search("misc_sprites_and_background", "background.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Button setup
    button_width = 250
    button_height = 50
    button_margin = 20
    button_color = (0, 0, 50) # Dark Blue

    buttons = [
        Button("Common Fish", WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 2.5 * button_height - 2 * button_margin, button_width, button_height, button_color),
        Button("Uncommon Fish", WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 1.5 * button_height - button_margin, button_width, button_height, button_color),
        Button("Rare Fish", WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 0.5 * button_height, button_width, button_height, button_color),
        Button("Ultimate Fish", WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 0.5 * button_height + button_margin, button_width, button_height, button_color),
        Button("Back", WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 1.5 * button_height + 2 * button_margin, button_width, button_height, button_color)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons:
                    if button.is_mouse_over():
                        if button.text == "Common Fish":
                            common_fish()
                        elif button.text == "Uncommon Fish":
                            uncommon_fish()
                        elif button.text == "Rare Fish":
                            rare_fish()
                        elif button.text == "Ultimate Fish":
                            ultimate_fish()
                        elif button.text == "Back":
                            main_menu()
                            return

        window.blit(background_image, (0, 0))

        for button in buttons:
            if button.is_mouse_over():
                button.draw(window)
            else:
                button.draw(window)

        pygame.display.flip()
        clock.tick(60)

def common_fish():
    pass

def uncommon_fish():
    pass

def rare_fish():
    pass

def ultimate_fish():
    pass



def show_controls():
    # Code to show the controls goes here
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
    bg_img = folder_search("misc_sprites_and_background", "background.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))


main_menu()

