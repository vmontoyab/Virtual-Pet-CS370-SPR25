from sprite_sheet_processor import load_sprite_sheet 
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
        }
        
    @classmethod
    def load(cls,filename):
        path = f"images/Cats/Sprites/{filename}"
        return load_sprite_sheet(path, cls.cat_size, cls.scale)

    @classmethod
    def get(cls, animation_name):
        return cls.animations.get(animation_name)