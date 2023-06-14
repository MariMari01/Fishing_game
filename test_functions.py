"""
Fishing Game Testing Module by Sam, Aspen, and Serena
Testing Module for Final Project
Tests all functions in functions.py, fisher_cat_class.py and fish_classes.py
For each passing test, there is a failing test.
"""
import functions as f
from fisher_cat_class import FisherCat
from fish_classes import Fish
import pygame

pygame.mixer.init()
pygame.font.init()

# Testing for functions.py.
def test_folder_search():
    """This function tests  folder_search() from functions.py
    """
    f.folder_search(folder_name="common_fish_game", file_name="common_blue_fish_game.png")

def test_folder_search_fail():
    """A failing test for folder_search() from functions.py.
    The file_name is missing ".png"
    """
    f.folder_search(folder_name="common_fish_game", file_name="common_blue_fish")

def test_background_music():
    """This function tests background_music() from functions.py
    """
    f.background_music()

def test_background_music_fail():
    """A failing test for background_music() from functions.py
    Adds an unneccessary parameter to background_music().
    """
    fail = True
    f.background_music(fail)

def test_music_end():
    """This function tests music_end() from functions.py
    """
    f.music_end()

def test_final_music_fail():
    """A failing test for final_music() from functions.py.
    This function is searching for a .wav file that is no longer in the folder
    """
    f.final_music()

def test_fish_caught_sound():
    """This function tests fish_caught_sound() from functions.py
    """
    f.fish_caught_sound()

def test_fish_caught_sound_fail():
    """A failing test for fish_caught_sound() from functions.py
    Adds an unneccessary parameter to fish_caught_sound().
    """
    fail = True
    f.fish_caught_sound(fail)

def test_game_over_sound():
    """This function tests game_over_sound() from functions.py
    """
    f.game_over_sound()

def test_game_over_sound_fail():
    """A failing test for game_over_sound() from functions.py
    Adds an unneccessary parameter to game_over_sound().
    """
    fail = True
    f.game_over_sound(fail)

def test_you_won_sound():
    """This function tests you_won_sound() from functions.py
    """
    f.you_won_sound()

def test_you_won_sound_fail():
    """A failing test for you_won_sound() from functions.py
    Adds an unneccessary parameter to you_won_sound().
    """
    fail = True
    f.you_won_sound(fail)

def test_cat_animation():
    """This function tests cat_animation() from functions.py
    """
    window = pygame.display.set_mode()
    x = 0
    y = 0
    f.cat_animation(window, x, y)

def test_cat_animation_fail():
    """A failing test for cat_animation() from functions.py
    Forgoes neccessary parameters for cat_animation().
    """
    f.cat_animation()

def test_game_won():
    """This function tests game_won() from the GameOver class in functions.py
    """
    screen = pygame.display.set_mode()
    window_width = 600
    window_height = 800
    f.game_won(screen, window_width, window_height)

def test_game_won_fail():
    """A failing test for game_over() from the GameOver class in functions.py
    Forgoes neccessary parameters for game_won().
    """
    f.game_won()

def test_game_over_draw():
    """This function tests draw() from the GameOver class in functions.py
    """
    screen = pygame.display.set_mode()
    window_width = 0
    window_height = 0
    test_game_over = f.GameOver(window_width, window_height)
    test_game_over.draw(screen)

def test_game_over_draw_fail():
    """A failing test for draw() from the GameOver class in functions.py
    Forgoes neccessary parameters for game_won() and GameOver().
    """
    test_game_over = f.GameOver()
    test_game_over.draw()

def test_scoreboard_increase_score():
    """This function tests increase_score() from the Scoreboard class in functions.py
    """
    points = 0
    test_increase_score = f.Scoreboard()
    test_increase_score.increase_score(points)

def test_scoreboard_increase_score_fail():
    """A failing test for increase_score() from the Scoreboard class in functions.py
    Forgoes neccessary parameters for increase_score() and Scoreboard().
    """
    test_increase_score = f.Scoreboard()
    test_increase_score.increase_score()

def test_scoreboard_draw():
    """This function tests draw() from the Scoreboard class in functions.py
    """
    screen = pygame.display.set_mode()
    scoreboard_draw = f.Scoreboard()
    scoreboard_draw.draw(screen)

def test_scoreboard_draw_fail():
    """A failing test for idraw() from the Scoreboard class in functions.py
    Forgoes neccessary parameters for draw() and Scoreboard().
    """
    scoreboard_draw = f.Scoreboard()
    scoreboard_draw.draw()

def test_castbar_draw():
    """This function tests draw() from the CastBar class in functions.py
    """
    screen = pygame.display.set_mode()
    castbar_draw = f.CastBar()
    castbar_draw.draw(screen)

def test_castbar_draw_fail():
    """A failing test for draw() from the CastBar class in functions.py
    Forgoes neccessary parameters for draw().
    """
    castbar_draw = f.CastBar()
    castbar_draw.draw()

def test_castbar_fill_up():
    """This function tests fill_up() from the CastBar class in functions.py
    """
    castbar_draw = f.CastBar()
    castbar_draw.fill_up()

def test_castbar_fill_up_fail():
    """A failing test for fill_up() from the CastBar class in functions.py
    Adds neccessary parameters for draw().
    """
    screen = pygame.display.set_mode()
    castbar_draw = f.CastBar()
    castbar_draw.fill_up(screen)

def test_castbar_fill():
    """This function tests fill() from the CastBar class in functions.py
    """
    screen = pygame.display.set_mode()
    castbar_draw = f.CastBar()
    castbar_draw.fill(screen)

def test_castbar_fill_fail():
    """A failing test for fill() from the CastBar class in functions.py
    Forgoes neccessary parameters for fill().
    """
    castbar_draw = f.CastBar()
    castbar_draw.fill()

# Testing for fish_classes.py
def test_fish_image_list_from_folder():
    """This function tests image_list_from_folder() from the Fish class in fish_classes.py
    """
    x = 0
    y = 0
    speed = 0
    points = 0
    fish = Fish(x, y, speed, points)
    fish.image_list_from_folder(folder_name="common_fish_game")

def test_fish_image_list_from_folder_fail():
    """A failing test for image_list_from_folder() from the Fish class in fish_classes.py
    The folder name has an addtional ".png" making the folder impossible to locate.
    """
    x = 0
    y = 0
    speed = 0
    points = 0
    fish = Fish(x, y, speed, points)
    fish.image_list_from_folder(folder_name="common_fish_game.png")

def test_fish_draw():
    """This function tests draw() from the Fish class in fish_classes.py
    """
    x = 0
    y = 0
    speed = 0
    points = 0
    screen = pygame.display.set_mode()
    fish = Fish(x, y, speed, points)
    fish.draw(screen)

def test_fish_draw_fail():
    """A failing test for draw() from the Fish class in fish_classes.py
    Forgoes neccessary parameters for draw().
    """
    x = "a"
    y = 0
    speed = 0
    points = 0
    screen = pygame.display.set_mode()
    fish = Fish(x, y, speed, points)
    fish.draw()

# Testing for fisher_cat_class.py
def test_fisher_cat_draw():
    """This function tests draw() from the FisherCat class in fisher_cat_classes.py
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    screen = pygame.display.set_mode()
    cat = FisherCat(x, y, window_x, window_y)
    cat.draw(screen)

def test_fisher_cat_draw_fail():
    """A failing test for draw() from the FisherCat class in fisher_cat_class.py
    Forgoes neccessary parameters for FisherCat().
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    screen = pygame.display.set_mode()
    cat = FisherCat()
    cat.draw(screen)

def test_fisher_cat_move_left():
    """This function tests move_left() from the FisherCat class in fisher_cat_classes.py
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    cat = FisherCat(x, y, window_x, window_y)
    cat.move_left()

def test_fisher_cat_move_left_fail():
    """A failing test for move_left() from the FisherCat class in fisher_cat_class.py
    Adds unneccessary parameters for move_left().
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    cat = FisherCat(x, y, window_x, window_y)
    cat.move_left(x, y)

def test_fisher_cat_move_right():
    """This function tests move_right() from the FisherCat class in fisher_cat_classes.py
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    cat = FisherCat(x, y, window_x, window_y)
    cat.move_right()

def test_fisher_cat_move_right_fail():
    """A failing test for move_left() from the FisherCat class in fisher_cat_class.py
    Adds unneccessary parameters for move_right().
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    cat = FisherCat(x, y, window_x, window_y)
    cat.move_right(cat)

def test_fisher_cat_reset_bob():
    """This function tests reset_bob() from the FisherCat class in fisher_cat_classes.py
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    cat = FisherCat(x, y, window_x, window_y)
    cat.reset_bob()

def test_fisher_cat_reset_bob_fail():
    """A failing test for reset_bob() from the FisherCat class in fisher_cat_class.py
    Adds an additional parameterto FisherCat().
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    screen = pygame.display.set_mode()
    cat = FisherCat(x, y, window_x, window_y, screen)
    cat.reset_bob()

def test_fisher_cat_ready_cast():
    """This function tests ready_cast() from the FisherCat class in fisher_cat_classes.py
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    cat = FisherCat(x, y, window_x, window_y)
    cat.ready_cast()

def test_fisher_cat_ready_cast_fail():
    """A failing test for reset_bob() from the FisherCat class in fisher_cat_class.py
    The parameters for window_x and window_y have been disgarded, and replaced with str instead of int.
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    cat = FisherCat(x, y, window_x="fail", window_y="fail")
    cat.ready_cast()

def test_cast():
    """This function tests cast() from the FisherCat class in fisher_cat_classes.py
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    cat = FisherCat(x, y, window_x, window_y)
    cat.cast()

def test_cast_fail():
    """A failing test for cast() from the FisherCat class in fisher_cat_class.py
    Adds an additional parameter to cast().
    """
    x = 0
    y = 0
    window_x = 0
    window_y = 0
    cat = FisherCat(x, y, window_x, window_y)
    cat.cast(x, y, window_x, window_y)
