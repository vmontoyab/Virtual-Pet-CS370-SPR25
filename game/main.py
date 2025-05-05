import pygame
import sys
import time
from core.resource_manager import ResourceManager
from core.render import Render
from core.pet_state import PetState
from cats.cat import Cat
from cats.cat_animations import CatAnimations

# Import sensor modules (try/except to allow fallback when not on RPi)
SENSORS_AVAILABLE = False
try:
    import sys
    import os
    
    # Add parent directory to path to allow importing from sensors
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.append(parent_dir)
    
    from sensors.ultrasonic import read_distance, setup as setup_ultrasonic, cleanup as cleanup_ultrasonic
    from sensors.sound import sound_detected, setup as setup_sound, cleanup as cleanup_sound
    
    # Initialize sensors
    setup_ultrasonic()
    setup_sound()
    SENSORS_AVAILABLE = True
    print("Sensors initialized successfully")
except (ImportError, RuntimeError) as e:
    print(f"Sensors not available: {e}")
    print("Using keyboard controls only.")

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

# Sensor control constants
PROXIMITY_THRESHOLD = 30  # cm - how close hand needs to be to feed cat
SOUND_COOLDOWN = 30  # frames between sound-triggered actions

# Game state
sound_cooldown_timer = 0
is_feeding = False

# Game loop
running = True
try:
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
                elif event.key == pygame.K_f:  # Add keyboard control for feeding
                    cat_state.feed()
                    is_feeding = True
                    cat.action("idle")  # Cat stays still while eating

        # Sensor inputs (when available)
        if SENSORS_AVAILABLE:
            # Ultrasonic sensor (proximity) for feeding
            distance = read_distance()
            if distance is not None and distance < PROXIMITY_THRESHOLD and not is_feeding:
                cat_state.feed()
                is_feeding = True
                cat.action("idle")  # Cat stays still while eating
                print(f"Hand detected at {distance}cm - Feeding cat")
                
            # Sound sensor for playing/jumping
            if sound_detected() and sound_cooldown_timer <= 0:
                cat.action("jump")  # Jump when hearing a loud sound
                sound_cooldown_timer = SOUND_COOLDOWN
                print("Sound detected - Cat jumps!")
                
            # Decrement sound cooldown timer
            if sound_cooldown_timer > 0:
                sound_cooldown_timer -= 1

        # If cat is eating and finishes, update state
        if is_feeding and not cat_state.is_feeding:
            is_feeding = False
            
        # Cat dies when happiness reaches zero
        if not cat_state.is_alive:
            cat.action("die")
        
        screen.blit(background, (0, 0))
        Render.draw_happiness_bar(screen)

        cat.update()
        cat_state.update()
        cat.draw(screen)
        pygame.display.flip()
        clock.tick(60)

finally:
    # Clean up GPIO when the game exits
    if SENSORS_AVAILABLE:
        try:
            cleanup_ultrasonic()
            cleanup_sound()
        except:
            pass
    pygame.quit()
