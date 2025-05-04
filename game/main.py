import pygame
from core.resource_manager import ResourceManager
from core.render import Render
from core.pet_state import PetState
from cats.cat import Cat
from cats.cat_animations import CatAnimations

# Initialize game window and set title
pygame.init()
pygame.display.set_caption('Virtual Pet!')
screen = pygame.display.set_mode((640, 400))

# Set Icon
icon = pygame.image.load('cats/images/pet.png').convert_alpha()
pygame.display.set_icon(icon)

# Load living room background
background = pygame.image.load("cats/images/background.jpg")
background = pygame.transform.scale(background, (640, 400)).convert()

# Load animations and other UI elements, create clock and cat
ResourceManager.load_all()
clock = pygame.time.Clock()
cat = Cat()
cat_state = PetState()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cat.action("jump")
            elif event.button == 3:
                    cat.action("idle")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cat.action("walk")

    if(not cat_state.is_alive):
        cat.action("die")
    
    screen.blit(background, (0, 0))
    Render.draw_happiness_bar(screen)

    cat.update()
    cat_state.update()
    cat.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
