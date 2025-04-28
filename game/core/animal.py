from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, motion, animator):
        self.motion = motion
        self.animator = animator

    def update(self):
        self.motion.update_position()
        self.animator.update()

        # Check if there is a collision and update both animator + motion accordingly
        new_direction = self.motion.check_wall_collision()
        if new_direction:
            self.animator.set_facing(new_direction)
            self.motion.move(new_direction)

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def action(self, action):
        pass
