from animator import Animator
from cat_animations import CatAnimations

class CatAnimator(Animator):

    def __init__(self):
        super().__init__()
        self.set_action("sleep",self.facing)

    def load_frames(self, action):
        key = f"{action}_{self.facing}" if self.facing else action
        return CatAnimations.get(key)