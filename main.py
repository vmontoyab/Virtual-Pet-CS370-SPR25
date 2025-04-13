import sys
import pygame

from sensors.ultrasonic import read_distance, cleanup as ultrasonic_cleanup
from sensors.sound_sensor import sound_detected, cleanup as sound_cleanup
from game.cat import Cat

def main():
    # Initialize Pygame
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Virtual Pet - Purple Circle Cat")

    clock = pygame.time.Clock()
    running = True

    # Create a Cat instance
    cat = Cat(x=100, y=100)

    try:
        while running:
            clock.tick(30)  # ~30 FPS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # --- Read sensor data ---
            distance_cm = read_distance()
            sound_state = sound_detected()

            # If an object is <15 cm away, speed up
            if distance_cm is not None and distance_cm < 15.0:
                cat.speed_x = 5
            else:
                cat.speed_x = 2

            # If sound is detected, make the cat jump
            if sound_state:
                cat.speed_y = -3
            else:
                # Make the cat float back down to y=100
                if cat.y < 100:
                    cat.speed_y += 0.2
                else:
                    cat.y = 100
                    cat.speed_y = 0

            # --- Update cat ---
            cat.update(WIDTH, HEIGHT)

            # --- Draw everything ---
            screen.fill((255, 255, 255))  # White background
            cat.draw(screen)
            pygame.display.flip()

    except KeyboardInterrupt:
        pass
    finally:
        # Cleanup GPIO usage
        ultrasonic_cleanup()
        sound_cleanup()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
