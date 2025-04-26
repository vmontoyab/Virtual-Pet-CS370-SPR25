from abc import ABC, abstractmethod

class Animator(ABC):
    def __init__(self):
        self.facing = "left"
        self.frames = []
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 20

    @abstractmethod
    def load_frames(self, action, facing):
        pass

    def set_action(self, action, facing=None):
        self.action = action

        new_frames = self.load_frames(self.action)
        if new_frames and new_frames != self.frames:
            if(facing == "left"):
                new_frames = list(reversed(new_frames))
            self.frames = new_frames
            self.current_frame = 0

    def get_frame(self):
        return self.frames[self.current_frame]
    
    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_timer = 0