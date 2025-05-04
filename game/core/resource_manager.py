import pygame

from cats.cat_animations import CatAnimations

class ResourceManager:
    happy_icon = None
    food_bowl = None
    toy = None
    background = None


    @classmethod
    def load_all(cls):
        # Load all cat animation frames
        CatAnimations.load_all()

        # Load happy_meter icon
        icon = pygame.image.load('cats/images/happy_meter.png').convert_alpha()
        cls.happy_icon = pygame.transform.scale(icon, (75, 75))

        #Load game_icon
        game_icon = pygame.image.load('cats/images/pet.png').convert_alpha()
        pygame.display.set_icon(game_icon)

        # Load living room background
        background = pygame.image.load("cats/images/background.jpg").convert_alpha()
        cls.background = pygame.transform.scale(background, (640, 400)).convert()

        #Load food_bowl image...how do I make this image one bowl instead of 4
        food_bowl = pygame.image.load('cats/images/CatItems/CatToys/CatBowls.png').convert_alpha()
        cls.food_bowl = pygame.transform.scale(food_bowl,(75, 75))

        #Load toy image
        toy = pygame.image.load('cats/images/CatItems/CatToys/PinkBall.gif').convert_alpha()
        cls.toy = pygame.transform.scale(toy,(75,75))
        
