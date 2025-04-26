import pygame
from animal import Animal
from motion import Motion
from cat_animator import CatAnimator
from pet_brain import PetBrain
class Cat(Animal):

    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.motion = Motion(screen_width, screen_height)
        self.animator = CatAnimator()
        self.brain = PetBrain(self.motion, self.animator)

    def draw(self, screen):
        frame = self.animator.get_frame()
        screen.blit(frame, (self.motion.x, self.motion.y))

    def update(self):

        if self.motion.jumping:
            if self.motion.is_on_floor():
                self.motion.snap_to_floor()
                self.brain.walk()
            else :
                self.motion.add_gravity()
        
        new_direction = self.motion.check_wall_collision()
        if new_direction:
            self.brain.change_direction(new_direction)

        self.animator.update()
        self.motion.update_position()
        
