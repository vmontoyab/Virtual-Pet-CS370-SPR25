import pygame
from core.resource_manager import ResourceManager
from core.pet_state import PetState

# Responsible for drawing interactive elements: happiness bar, happy_meter icon, bowl, play icon.
class Render:

    BAR_X = 30
    BAR_Y = 75
    BAR_WIDTH = 20
    BAR_HEIGHT = 250
    BORDER = 2

    @classmethod
    def draw_happiness_bar(cls, screen, pet_state: PetState):
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

        # Compute happiness ratio
        ratio = pet_state.happiness / PetState.MAX_HAPPINESS
        # Ensure ratio is between 0-100 by clamping
        clamped_ratio = max(0.0, min(1.0, ratio))
        # Translate happiness: 0-100 into its pixel equivalent
        filled_height = int(clamped_ratio * Render.BAR_HEIGHT)

        pygame.draw.rect(
            screen,
            (50, 200, 50),  
            (
                Render.BAR_X,
                Render.BAR_Y + (Render.BAR_HEIGHT - filled_height),
                Render.BAR_WIDTH,
                filled_height
            )
        )
