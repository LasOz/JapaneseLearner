import pygame

def load_image(location):
    try:
        return pygame.image.load(location + ".jpg")
    except:
        return pygame.image.load(location + ".png")

def scale_screen(screen):
    return pygame.transform.scale(screen, (500,500))

def write_on_screen(screen, word, position):
    font = pygame.font.SysFont("msgothicmsuigothicmspgothic", 50)
    textsurface = font.render(word, True, (255, 255, 255), (0, 0, 0))
    screen.blit(textsurface, position)

def play_sound(soundfile : str):
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()

#A class to manage the window of the game
class game_window:
    screen = None
    logo = None

    def was_closed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def __init__(self, w, h):
        pygame.init()
        pygame.display.set_caption(type(self).__name__)
        self.screen = pygame.display.set_mode((w,h))

    def __enter__(self):
        print("Starting window")
        return self

    def __exit__(self, type, value, traceback):
        self.screen = None
        self.logo = None
        print("Exiting Window")
        return True

    def set_logo(self, location):
        self.logo = pygame.image.load(location)
        pygame.display.set_icon(self.logo)

    def flip(self):
        pygame.display.flip()
