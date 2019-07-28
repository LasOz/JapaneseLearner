"""This is my own event handling class, I don't think it's very good"""

import pygame

class EventHandler:
    """This is my own event handling class, I don't think it's very good"""
    m_listenList = []

    def __init__(self):
        pass

    def add_to_listen(self, callback):
        """Provide a callback which takes a single pygame.event.Event argument
        This call back should take an event and check it and do something if it recieves
        A specific event"""
        self.m_listenList.append(callback)

    def check_events(self):
        """Take all events on the queue and check them against all the callbacks
        that have been added to the listen list"""
        for event in pygame.event.get():
            for callback in self.m_listenList:
                callback(event)
