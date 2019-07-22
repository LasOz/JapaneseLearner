import pygame

class EventHandler:
    m_listenList = []

    def __init__(self):
        pass

    def add_to_listen(self, callback):
        self.m_listenList.append(callback)

    def check_events(self):
        for event in pygame.event.get():
            for callback in self.m_listenList:
                callback(event)

