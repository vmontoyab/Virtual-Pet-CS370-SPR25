import pygame

from cats.cat_animations import CatAnimations

class ResourceManager:
    happy_icon = None

    @classmethod
    def load_all(cls):
        # Load all cat animation frames
        CatAnimations.load_all()

        # Load happy_meter icon
        icon = pygame.image.load('cats/images/happy_meter.png').convert_alpha()
        cls.happy_icon = pygame.transform.scale(icon, (75, 75))
