import pygame

class Animator:
    def __init__(self):
        self.frames = []  # List containing animation frames
        self.current_animation = None
        self.current_frame = 0
        self.timer = 0

        self.loop = True  # If we want animation to loop
        self.finished = False # If ^ loop = False, flag is set after playing all frames once
   
    def set_animation(self, animation_name):
            self.current_animation = animation_name
            self.current_frame = 0
            self.timer = 0
            self.frame_duration = 20

    # So different pets can move quicker/slower
    def update(self):
        pass

    def draw(self, screen, position):
        # Draw + display the current frame
        frame = self.frames[self.current_frame]

        # If facing left, flip frame horizontally
        if self.facing == "left":
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, position)



