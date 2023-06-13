import pygame

class Button:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = (150, 150, 150) # Grey
        self.clicked_color = (200, 200, 200)
        self.font = pygame.font.Font(None, 36)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.centery)) # Center text
        window.blit(text_surface, text_rect)

    def is_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
