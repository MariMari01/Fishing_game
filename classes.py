
import pygame

class GameOver:
    def __init__(self, window_width, window_height) -> None:
        self.font =pygame.font.SysFont("Times New Roman", 36)
        self.text_color = (255, 255, 255)
        self.position = (window_width//2, window_height//2)

    def draw(self,screen):
        music_end()
        game_over_sound()
        self.score_text = self.font.render("GAME OVER", True, self.text_color)
        screen.blit(self.score_text, self.position)




class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.text_color = (255, 255, 255)
        self.position = (10, 10)

    def increase_score(self, points):
        self.score += points

    def draw(self, screen):
        score_text = self.font.render("Score: " + str(self.score) + "/ 2000", True, self.text_color)
        screen.blit(score_text, self.position)




class CastBar:

    def __init__(self) -> None:
        self.fill_height = 0
        self.bottom = 258
        self.top = 102
        self.color = (146, 240, 235)
        self.fill_color = (11, 252, 3)
        self.xpos = 42
        self.bar_ypos = 215
        self.minigame_fishpos = 42




    def draw(self, window):
        # Drawing Rectangle
        pygame.draw.rect(window, self.color, pygame.Rect(700, 100, 30, 120))

    def fill_up(self):
        '''
        Moves the mini game bar up
        '''
        if self.bar_ypos <= self.top:
            pass
        else:
            self.fill_height += 0.25
            self.bar_ypos -= 0.25

    def fill(self, window):
        self.rectangle = pygame.draw.rect(window, self.fill_color, pygame.Rect(702, self.bar_ypos, 26, self.fill_height))



class Button:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = (150, 150, 150) # Grey
        self.clicked_color = (200, 200, 200)
        self.font = pygame.font.Font(None, 36)

    def draw(self, window):
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
    
    