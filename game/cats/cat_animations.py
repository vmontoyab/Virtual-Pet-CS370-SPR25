from utils.sprite_sheet_processor import extract_frames 
from core.constants import PET_SIZE

class CatAnimations:
    animations = {}

    @classmethod
    def load_all(cls):
        cls.animations = {
            "walk": cls.load_action("Walk.png"),
            "jump": cls.load_action("Jump.png"),
            "sleep": cls.load_action("Sleep.png",1.5),
            "idle": cls.load_action("Idle.png",1.7),
            "die": cls.load_action("Dead2.png"),
            "throw_ball": cls.load_obj("BlueBall-Sheet.png",24,16) 
        }
        
    @classmethod
    def load_action(cls,filename, scale=2):
        path = f"cats/images/Cats/Sprites/{filename}"
        return extract_frames(path, PET_SIZE, PET_SIZE, scale)
    
    @classmethod
    def load_obj(cls, filename, frame_width, frame_height, scale=2):
        path = f"cats/images/CatItems/CatToys/{filename}"
        return extract_frames(path, frame_width, frame_height, scale)

    @classmethod
    def get(cls, animation_name):
        return cls.animations.get(animation_name)