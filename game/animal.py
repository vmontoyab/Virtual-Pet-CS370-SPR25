from abc import ABC, abstractmethod
class Animal:
    def __init__(self, screen_width, screen_height):
        #screen_width and height params in order to
        # place animal in correct position within game
        self.screen_width = screen_width
        self.screen_height = screen_height

    @abstractmethod
    def update(self, screen_width, screen_height):
        pass

    @abstractmethod
    def draw(self, surface):
        pass