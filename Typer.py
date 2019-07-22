import pygame

class Typer:
    m_text = ""

    def __init__(self):
        pass

    def get_keystrokes(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(self.m_text)
                self.m_text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.m_text = self.m_text[:-1]
            else:
                self.m_text += event.unicode
      