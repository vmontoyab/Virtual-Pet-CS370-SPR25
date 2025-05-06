import pygame
from core.resource_manager import ResourceManager

# Responsible for drawing interactive elements: happiness bar, happy_meter icon, bowl, play icon.
class Render:

    BAR_X = 30
    BAR_Y = 75
    BAR_WIDTH = 20
    BAR_HEIGHT = 250
    BORDER = 2

    @classmethod
    def draw_happiness_bar(cls, screen):
        screen.blit(ResourceManager.happy_icon, (cls.BAR_X-25, cls.BAR_Y-75))

        # Draws a white border with x,y,width,and height
        pygame.draw.rect(screen, (255,255,255),
            (cls.BAR_X-cls.BORDER, cls.BAR_Y-cls.BORDER,
            cls.BAR_WIDTH+cls.BORDER*2, cls.BAR_HEIGHT+cls.BORDER*2)
        )
        
        # Unfilled bar = dark grey background
        pygame.draw.rect(screen, (50,50,50),
            (cls.BAR_X, cls.BAR_Y, cls.BAR_WIDTH, cls.BAR_HEIGHT)
        )
        # Fill bar with green color to begin with 
        pygame.draw.rect(screen, (50,200,50),
            (cls.BAR_X, cls.BAR_Y, cls.BAR_WIDTH, cls.BAR_HEIGHT)
        )

    @classmethod   
    def draw_food_bowl(cls, screen):          #location on screen, cropped area of picture, size of image
        screen.blit(ResourceManager.food_bowl, (485,300),(cls.BAR_X+9, cls.BAR_Y-85, 50,50))

    @classmethod
    def draw_toy(cls, screen):
        screen.blit(ResourceManager.toy, (cls.BAR_X-25, cls.BAR_Y-75))