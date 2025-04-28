from sprite_sheet_processor import extract_frames 
class CatAnimations:
    # Size hard-coded to match sprite pngs
    cat_size = 64
    animations = {}

    @classmethod
    def load_all(cls):
        cls.animations = {
            "walk_right": cls.load("WalkRight.png"),
            "walk_left": cls.load("WalkLeft.png"),
            "jump_right": cls.load("JumpRight.png"),
            "jump_left": cls.load("JumpLeft.png"),
            "run_right": cls.load("Running.png"),,
            "sleep_right": cls.load("SleepRight.png",1.5),
            "sleep_left": cls.load("SleepLeft.png",1.5),
            "idle_left": cls.load("IdleLeft.png",1.8),
            "idle_right": cls.load("IdleRight.png",1.8)
        }
        
    @classmethod
    def load(cls,filename, scale=2):
        path = f"images/Cats/Sprites/{filename}"
        return extract_frames(path, cls.cat_size, scale)

    @classmethod
    def get(cls, animation_name):
        return cls.animations.get(animation_name)