from core.animal import Animal
from core.motion import Motion
from cats.cat_animator import CatAnimator

class Cat(Animal):
    def __init__(self):
        motion = Motion()
        animator = CatAnimator()
        super().__init__(motion, animator)

    def draw(self, screen):
        position = self.motion.get_position()
        self.animator.draw(screen, position)

    def action(self, action):
        
        # Handle y-movement
        if action == "jump":
            self.animator.set_animation(action, loop=False)
            self.animator.set_frame_duration(3)
            self.motion.jump(self.animator.facing)
        elif action in ("idle", "sleep"):
            self.animator.set_animation(action, loop=True)
            self.motion.stop() # Do not move horizontally, stay in place
            pass
        else:
            # Actions like walking, running, etc. move horizontally
            self.animator.set_animation(action, loop=True)
            self.motion.move(self.animator.facing)
    
        
