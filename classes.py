"""Fishing Game by Same, Sarena, and Aspen
Class module, icludes: GameOver, Scoreboard, CastBar, and Button classes.
"""


from functions import music_end, game_over_sound
import pygame


class GameOver:
    def __init__(self, window_width, window_height) -> None:
        """A class that writes "GAME OVER" on the screen.

        Args:
            window_width (int): The x value of the screen.
            window_height (int): The y value of the screen.
        """
        self.font =pygame.font.SysFont("Times New Roman", 36)
        self.text_color = (255, 255, 255)
        self.position = (window_width//2, window_height//2)

    def draw(self,screen):
        """Draws the text onto the screen.

        Args:
            screen (pygame.display): Gives the function a screen to draw on.
        """
        music_end()
        game_over_sound()
        self.score_text = self.font.render("GAME OVER", True, self.text_color)
        screen.blit(self.score_text, self.position)

class Scoreboard:
    """Scoreboard for the game.
    """
    def __init__(self):
        """A class that writes the players score onto the screen.
        """
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.text_color = (255, 255, 255)
        self.position = (10, 10)

    def increase_score(self, points):
        """Updated the points as the player catches fish.

        Args:
            points (int): The integer vaule of the points earned from catching fish.
        """
        self.score += points

    def draw(self, screen):
        """Writes the score as text onto the screen. It updates everytime the player scores.

        Args:
            screen (pygame.display): A surface for the text to be written.
        """
        score_text = self.font.render("Score: " + str(self.score) + "/ 2000", True, self.text_color)
        screen.blit(score_text, self.position)

class CastBar:
    """Cast bar determine the strength of the players cast.
    """

    def __init__(self) -> None:
        """A class for the cast bar, an on screen
        object that tells the user how far the hook will land.
        """
        self.fill_height = 0
        self.bottom = 258
        self.top = 102
        self.color = (146, 240, 235)
        self.fill_color = (11, 252, 3)
        self.xpos = 42
        self.bar_ypos = 215
        self.minigame_fishpos = 42

    def draw(self, window):
        """Draws the cast bar onto the screen
        Args:
            window (pygame.display): A surface for the cast bar to be drawn on.
        """
        pygame.draw.rect(window, self.color, pygame.Rect(700, 100, 30, 120))

    def fill_up(self):
        '''
        Moves the cast game bar up
        '''
        if self.bar_ypos <= self.top:
            pass
        else:
            self.fill_height += 0.25
            self.bar_ypos -= 0.25

    def fill(self, window):
        """Fills the cast bar with color as the user holds
        down the button to indicate how far the hook will be cast.

        Args:
            window (pygame.display): A surface for the bar color to be drawn on.
        """
        self.rectangle = pygame.draw.rect(
                                        window, self.fill_color, pygame.Rect(
                                        702, self.bar_ypos, 26, self.fill_height))

class Button:
    """A button for user interaction with the screen.
    """
    def __init__(self, text, x, y, width, height, color):
        """A start screen button

        Args:
            text (str): Writing on the screen
            x (int): x-cor
            y (int): y-cor
            width (int): width of the button
            height (int): height of the button
            color (str): color of the button
        """
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = (150, 150, 150) # Grey
        self.clicked_color = (200, 200, 200)
        self.font = pygame.font.Font(None, 36)

    def draw(self, window):
        """Draws the button onto the screen

        Args:
            window (pygame.dispaly): A place to draw the button onto.
        """
        if self.is_mouse_over():
            pygame.draw.rect(window, self.hover_color, self.rect)
        else:
            pygame.draw.rect(window, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.centery))
        window.blit(text_surface, text_rect)

    def is_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    
