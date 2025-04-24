from sprite_sheet_processor import load_sprite_sheet 
class CatAnimations:
    def _init_(self, scale):
        self.scale = scale
        self.size = 64
        self.animations = {
            "walk_right": self.load("WalkRight.png"),
            "walk_left": self.load("WalkLeft.png"),
        }

    def load(self,filename):
        path = f"images/Cats/Sprites/{filename}"
        return load_sprite_sheet(path, self.size, self.scale)

    def get(self, animation_name):
        pass