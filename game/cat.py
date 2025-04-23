import pygame
from animal import Animal
from sprite_sheet_processor import load_sprite_sheet

class Cat(Animal):
    def __init__(self, scale, screen_width, screen_height, speed_x=2, speed_y=0):
        super().__init__(screen_width, screen_height)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.size = 64

        floor_offset = 50
        self.y = (screen_height - floor_offset) - self.size
        self.x = screen_width // 2 - self.size // 2

        self.animations = {
            "right": load_sprite_sheet('images/Cats/Sprites/WalkRight.png', self.size, scale),
            "left": load_sprite_sheet('images/Cats/Sprites/WalkLeft.png', self.size, scale)
        }
        self.facing = "right"
        self.frames = self.animations[self.facing]

        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 8
    
    def change_direction(self, direction):
        self.facing = direction
        self.frames = self.animations[direction]
        self.speed_x *= -1


    def update(self, screen_width, screen_height):
        # Simple horizontal movement + bounce
        self.x += self.speed_x
        self.y += self.speed_y
        wall_offset = 100

        if self.x < wall_offset:
            self.x = wall_offset

            # Cat starts facing right
            self.change_direction("right")

        elif self.x + self.size > screen_width-wall_offset:
            self.x = screen_width - wall_offset - self.size

            # Cat flips to face left 
            self.change_direction("left")

    def draw(self, surface):
        # Get current frame in action
        frame = self.frames[self.current_frame]
        # Draw frame
        surface.blit(frame, (self.x, self.y))

        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_timer = 0
        
