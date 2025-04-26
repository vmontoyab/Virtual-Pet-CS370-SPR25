from motion import Motion
from cat_animator import CatAnimator

class PetBrain:

    def __init__(self, motion, animator):
        self.motion = motion
        self.animator = animator

    def change_direction(self, direction):
        self.animator.facing = direction
        self.motion.change_direction()
        self.animator.set_action(self.animator.action, direction)

    def idle(self):
        self.motion.idle()
        self.animator.set_action("idle")

    def walk(self):
        self.motion.walk(self.animator.facing)
        self.animator.set_action("walk")
    
    def jump(self):
        if not self.motion.jumping:
            self.motion.jump(self.animator.facing)
            self.animator.set_action("jump")




        