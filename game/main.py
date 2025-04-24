import pygame
from cat import Cat
from cat_animations import CatAnimations

# Initialize game window and set title
pygame.init()
pygame.display.set_caption('Virtual Pet!')
screen = pygame.display.set_mode((640, 400))

# Set Icon
icon = pygame.image.load('images/pet.png').convert_alpha()
pygame.display.set_icon(icon)

# Load living room background
background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(background, (640, 400)).convert()

# Load animations, create clock and cat
CatAnimations.load_all()
clock = pygame.time.Clock()
cat = Cat(640, 400, .5)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    cat.update()
    cat.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
