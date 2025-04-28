from utils.sprite_sheet_processor import extract_frames 
from core.constants import PET_SIZE

class CatAnimations:
    animations = {}

    @classmethod
    def load_all(cls):
        cls.animations = {
            "walk": cls.load("Walk.png"),
            "jump": cls.load("Jump.png"),
            "sleep": cls.load("Sleep.png",1.5),
            "idle": cls.load("Idle.png",1.7)
        }
        
    @classmethod
    def load(cls,filename, scale=2):
        path = f"cats/images/Cats/Sprites/{filename}"
        return extract_frames(path, PET_SIZE, scale)

    @classmethod
    def get(cls, animation_name):
        return cls.animations.get(animation_name)