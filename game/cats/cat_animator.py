from core.animator import Animator
from cats.cat_animations import CatAnimations

class CatAnimator(Animator):
    def __init__(self):
        super().__init__()
        # Initial behavior is sleeping
        self.set_animation("sleep")
        self.facing = "right"

    def set_facing(self, direction):
        self.facing = direction

    def set_frame_duration(self, time):
        self.frame_duration = time
    
    # Replace current animation with passed-in animation
    def set_animation(self, animation_name, end_frame_index=0, loop=True):
        if self.current_animation != animation_name:
            super().set_animation(animation_name)
            self.frames = CatAnimations.get(animation_name)
            self.loop = loop
            self.finished = False
            # TODO: find more elegant way to handle ending at diff frames 
            self.end_frame = len(self.frames)-end_frame_index 

    # Hold frame for certain length, then switch to next frame
    def update(self):
        if self.finished:
            return  # Don't update

        self.timer += 1
        if self.timer >= self.frame_duration:
            self.timer = 0
            self.current_frame += 1

            if self.current_frame >= len(self.frames):
                if not self.loop:
                    self.finished = True
                    self.current_frame = self.end_frame  
                else:
                    self.current_frame = 0
                    
