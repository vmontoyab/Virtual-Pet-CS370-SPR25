import pygame
from cat import Cat

# Initialize game window and set title
pygame.init()
pygame.display.set_caption('Virtual Pet!')
screen = pygame.display.set_mode((1280, 800))

# Set Icon
icon = pygame.image.load('images/pet.png').convert_alpha()
pygame.display.set_icon(icon)

# Load living room background
background = pygame.image.load("images/background2.jpg")
background = pygame.transform.scale(background, (1280, 800)).convert()

# Create clock and cat
clock = pygame.time.Clock()
cat = Cat(1280, 800, 1)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    cat.update(1280, 800)
    cat.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
