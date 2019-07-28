"""This is a class I made for detecting what the keyboard as typed"""

import pygame

class Typer:  # pylint: disable=too-few-public-methods
    """This is a class I made for detecting what the keyboard as typed"""
    m_text = ""

    def __init__(self):
        pass

    def get_keystrokes(self, event):
        """This is a callback function to work with the event handler"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(self.m_text)
                self.m_text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.m_text = self.m_text[:-1]
            else:
                self.m_text += event.unicode
      