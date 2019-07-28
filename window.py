"""This is a module I made for higher level abstraction interaction with the game window
And easy use of common commands"""

import pygame

def load_image(location: str):
    """loads the given image"""
    return pygame.image.load(location)

def write_on_screen(screen: pygame.Surface, word: str, position: (int, int)):
    """Writes text on the screen in a Japanese compatable font"""
    font = pygame.font.SysFont("msgothicmsuigothicmspgothic", 50)
    textsurface = font.render(word, True, (255, 255, 255), (0, 0, 0))
    screen.blit(textsurface, position)

def play_sound(soundfile: str):
    """plays the sound file provided"""
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()

def get_clock():
    """get the pygame clock object"""
    return pygame.time.Clock()

class GameWindow:
    """A class to manage the window of the game"""

    screen: pygame.Surface = None
    logo: pygame.Surface = None
    closed: bool = False

    def was_closed(self, event: pygame.event.Event):
        """this is a calback given to the event listener to check when the game is closed"""
        if event.type == pygame.QUIT:
            self.closed = True

    def __init__(self, w: int, h: int):
        pygame.init()
        pygame.display.set_caption(type(self).__name__)
        self.screen = pygame.display.set_mode((w, h))

    def __enter__(self):
        print("Starting window")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.screen = None
        self.logo = None
        print("Exiting Window")
        return True

    def set_logo(self, location: str):
        """Sets the logo of the window and displays it immediately"""
        self.logo = pygame.image.load(location)
        pygame.display.set_icon(self.logo)

    def blit_to_scale(self, image: pygame.Surface, position: (int, int)):
        """scales the screen to fit within the bounds of the window"""
        surface = pygame.transform.scale(image, self.screen.get_size())
        self.screen.blit(surface, position)

    def flip(self):
        """refreshes the display (loads the next frame and readies the next for editing)"""
        pygame.display.flip()
