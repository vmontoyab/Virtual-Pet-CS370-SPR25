# game/cat.py

import pygame
from .animal import Animal

class Cat(Animal):
    def __init__(self, x, y, speed_x=2, speed_y=0, size=50):
        super().__init__(x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.size = size

    def update(self, screen_width, screen_height):
        # Simple horizontal movement + bounce
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0:
            self.x = 0
            self.speed_x *= -1
        elif self.x + self.size > screen_width:
            self.x = screen_width - self.size
            self.speed_x *= -1

    def draw(self, surface):
        """
        purple circle for now since I don't know how to like have a cat drawn
        """
        radius = self.size // 2
        center_x = self.x + radius
        center_y = self.y + radius
        pygame.draw.circle(surface, (128, 0, 128), (center_x, center_y), radius)