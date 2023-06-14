import pygame
from pygame.locals import *

class Credit:
    """Represents a credit entry."""

    def __init__(self, text, font, color, position):
        """
        Initialize a Credit object.

        Args:
            text (str): The text of the credit.
            font (pygame.font.Font): The font object used to render the text.
            color (tuple): The color of the text in RGB format.
            position (dict): The position of the credit on the screen.
        """
        self.text = text
        self.font = font
        self.color = color
        self.position = position
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(**self.position)

    def update(self):
        """Update the position of the credit by moving it upward."""
        self.rect.move_ip(0, -1)

class CreditsScreen:
    """Represents the screen displaying the credits."""

    def __init__(self, width, height, title, font_size, font_color, background_image, credits_file):
        """
        Initialize a CreditsScreen object.

        Args:
            width (int): The width of the screen in pixels.
            height (int): The height of the screen in pixels.
            title (str): The title of the window.
            font_size (int): The size of the font used for the credits.
            font_color (tuple): The color of the text in RGB format.
            background_image (str): The path to the background image file.
            credits_file (str): The path to the text file containing the credits.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("Arial", font_size)
        self.font_color = font_color
        self.background_image = pygame.image.load(background_image).convert()  # Load the background image
        self.credits = self.load_credits(credits_file)

    def load_credits(self, filename):
        """
        Load the credits from a text file.

        Args:
            filename (str): The path to the text file containing the credits.

        Returns:
            list: A list of credit entries.
        """
        with open(filename, 'r') as file:
            credit_list = file.read().splitlines()
        return credit_list

    def create_credit_objects(self):
        """
        Create Credit objects for each credit entry.

        Returns:
            list: A list of Credit objects.
        """
        credit_objects = []
        for i, line in enumerate(self.credits):
            credit = Credit(line, self.font, self.font_color, {"centerx": self.screen.get_rect().centerx, "y": self.screen.get_rect().bottom + i * 45})
            credit_objects.append(credit)
        return credit_objects

    def run(self):
        """Run the main loop to display the credits."""
        credit_objects = self.create_credit_objects()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    return

            self.screen.blit(self.background_image, (0, 0))  # Draw the background image

            all_off_screen = True
            for credit in credit_objects:
                credit.update()
                if credit.rect.bottom > 0:
                    all_off_screen = False
                self.screen.blit(credit.surface, credit.rect)

            if all_off_screen:
                pygame.quit()
                return

            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    bg_img = f.folder_search("misc_sprites_and_background", "background.png")
    credits_screen = CreditsScreen(800, 600, "End credits", 40, (255, 255, 255), bg_img, "credits.txt")
    credits_screen.run()            
