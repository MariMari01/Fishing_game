import pygame
from functions import background_music, fish_caught_sound, cat_animation
from fish_classes import Common, Uncommon, Rare
from ultimate_catch import UltimateCatch
from fisher_cat_class import FisherCat
from score import Scoreboard
from mini_game import mini_game
from model import folder_search
from button import Button

def main_menu():
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
    bg_img = folder_search("misc_sprites_and_background", "start_screen_background.png")
    background_image = pygame.image.load(bg_img)
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Button setup
    button_width = 250
    button_height = 50
    button_margin = 20
    button_color = (0, 0, 50) # Dark Blue

    buttons = [
        Button("Start Game", WINDOW_WIDTH // 2 + 250 - button_width // 2, WINDOW_HEIGHT // 2 - 2.5 * button_height - 2 * button_margin, button_width, button_height, button_color),
        Button("Background Story", WINDOW_WIDTH // 2 + 250 - button_width // 2, WINDOW_HEIGHT // 2 - 1.5 * button_height - button_margin, button_width, button_height, button_color),
        Button("Fish Encyclopedia", WINDOW_WIDTH // 2 + 250 - button_width // 2, WINDOW_HEIGHT // 2 - 0.5 * button_height, button_width, button_height, button_color),
        Button("Controls", WINDOW_WIDTH // 2 + 250 - button_width // 2, WINDOW_HEIGHT // 2 + 0.5 * button_height + button_margin, button_width, button_height, button_color),
        Button("Quit", WINDOW_WIDTH // 2 + 250 - button_width // 2, WINDOW_HEIGHT // 2 + 1.5 * button_height + 2 * button_margin, button_width, button_height, button_color)
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
                            show_story()
                        elif button.text == "Fish Encyclopedia":
                            show_encyclopedia()
                        elif button.text == "Controls":
                            show_controls()
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

def start_game():
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



    catching = False
    fish_caught_points = None
    # Create fish objects
    common_fish = Common(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 80)
    uncommon_fish = Uncommon(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70)
    rare_fish = Rare(WINDOW_WIDTH // 2 + 100, WINDOW_HEIGHT // 2 + 260)
    ultimate_catch = UltimateCatch(WINDOW_WIDTH // 2 +100, WINDOW_HEIGHT // 2 + 150)
    minigame = mini_game(5)



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
            if not catching and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    cat.move_right()
                elif event.key == pygame.K_a:
                    cat.move_left()
                elif event.key == pygame.K_e:
                    cat.ready_cast()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    cat_animation(window, cat.rect.left, cat.rect.top)
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
        
        minigame.draw(window)
        if catching:
            minigame.fill(window)
        # Draw the scoreboard
        scoreboard.draw(window)
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

