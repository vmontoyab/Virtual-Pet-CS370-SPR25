import pygame
from animal import Animal
from cat_animations import CatAnimations
class Cat(Animal):

    # Class Constants:
    SIZE = 64 # hard-coded to match sprite pngs
    FLOOR_OFFSET = 50 # for correct placement with current screen_height
    WALL_OFFSET = 100 # boundary so cat doesn't get too close to walls
    JUMP_SPEED = -20 # negative value will move self.y up 20 pixels
    GRAVITY = 1 # gravity is added to JUMP_SPEED to move self.y down

    def __init__(self, screen_width, screen_height, speed_x=2, speed_y=0):
        super().__init__(screen_width, screen_height)
        self.x = screen_width // 2 - Cat.SIZE // 2
        self.y = (screen_height - Cat.FLOOR_OFFSET) - Cat.SIZE
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.init_movement(speed_x,speed_y)
        self.init_animation()
    
    def init_animation(self):
        self.action = "walk"
        self.facing = "right"
        self.frames = CatAnimations.get(f"{self.action}_{self.facing}")
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 20

    def init_movement(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = 1
        self.jump_strength = -15
        self.jumping = False
    
    def set_animation(self, animation_name):
        new_frames = CatAnimations.get(animation_name)
        if new_frames:
            if new_frames != self.frames:
                self.frames = new_frames
                self.current_frame = 0

    def change_direction(self, direction):
        self.facing = direction
        self.speed_x *= -1
        self.set_animation(f"{self.action}_{self.facing}")

    def jump(self):
        # Prevent double-jumping
        if not self.jumping:
            self.jumping = True
            self.speed_y = Cat.JUMP_SPEED
            self.action = "jump"
            self.set_animation(f"{self.action}_{self.facing}")

            # Left jump needs to reverse order of frames
            if(self.facing == "left"):
                self.frames = list(reversed(self.frames))
            # Increase horizontal speed, for natural-looking jump
            self.speed_x += (2 if self.speed_x > 0 else -2)

    def walk(self):
        self.action = "walk"
        self.speed_x = (1 if self.speed_x > 0 else -1)
        self.speed_y = 0
        self.set_animation(f"{self.action}_{self.facing}")

    def update(self):
        # Horizontal and vertical movement
        self.x += self.speed_x
        self.y += self.speed_y

        # Apply gravity to bring cat back down after jump
        if self.jumping:
            self.speed_y += Cat.GRAVITY

        # Snap cat back to the floor after jump
        floor = self.screen_height - Cat.FLOOR_OFFSET - Cat.SIZE
        if self.y >= floor:
            self.jumping = False
            self.walk()

        # # Check collision with left wall
        if self.x < Cat.WALL_OFFSET:
            self.x = Cat.WALL_OFFSET

            # Cat flips to face right
            self.change_direction("right")

        # Check collision with right wall
        elif self.x + Cat.SIZE > self.screen_width - Cat.WALL_OFFSET:
            self.x = self.screen_width - Cat.WALL_OFFSET - Cat.SIZE

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
        
