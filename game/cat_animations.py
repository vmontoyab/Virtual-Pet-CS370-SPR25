from sprite_sheet_processor import extract_frames 
class CatAnimations:
    # Size hard-coded to match sprite pngs
    # Scale 2 : cat proportional to background
    cat_size = 64
    scale = 2
    animations = {}

    @classmethod
    def load_all(cls):
        cls.animations = {
            "walk_right": cls.load("WalkRight.png"),
            "walk_left": cls.load("WalkLeft.png"),
            "jump_right": cls.load("JumpRight.png"),
            "jump_left": cls.load("JumpLeft.png"),
            "run_right": cls.load("Running.png"),
        }
        
    @classmethod
    def load(cls,filename):
        path = f"images/Cats/Sprites/{filename}"
        return extract_frames(path, cls.cat_size, cls.scale)

    @classmethod
    def get(cls, animation_name):
        return cls.animations.get(animation_name)