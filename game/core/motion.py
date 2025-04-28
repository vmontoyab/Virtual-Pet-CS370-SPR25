from core.constants import SCREEN_WIDTH, SCREEN_HEIGHT, PET_SIZE, WALL_OFFSET, FLOOR_OFFSET

class Motion:
    def __init__(self):
        # Start in the center, and on the floor
        self.x = SCREEN_WIDTH // 2 - PET_SIZE // 2
        self.y = SCREEN_HEIGHT - FLOOR_OFFSET - PET_SIZE
    
        self.vx = 0  # velocity x (speed x with direction)
        self.vy = 0  # velocity y (speed y with direction)
        self.speed = 1 # How fast to move without direction

        self.is_jumping = False

    def update_position(self):
        self.x += self.vx
        self.y += self.vy

        # 1.3 takes cat_scale into account
        self.is_on_floor = self.y  >= SCREEN_HEIGHT - FLOOR_OFFSET - PET_SIZE*1.3
        if self.is_on_floor and self.is_jumping :
            self.snap_to_floor()
            self.is_jumping = False
        elif self.is_jumping:
            self.add_gravity()
            
    def move(self,direction):
        self.snap_to_floor()
        if direction == "left":
            self.vx = -self.speed
        elif direction == "right":
            self.vx = self.speed

    def stop(self):
        self.snap_to_floor()

    # Checks collision and changes movement accordingly, also returns new direction if applicable
    def check_wall_collision(self):
        if self.x < WALL_OFFSET:  # Left wall
            self.x = WALL_OFFSET
            return 'right'  # Change direction to right
        elif self.x + PET_SIZE > SCREEN_WIDTH - WALL_OFFSET:  # Right wall
            self.x = SCREEN_WIDTH - PET_SIZE - WALL_OFFSET
            return 'left'  # Change direction to left
        return False

    def snap_to_floor(self):
        # Cat scale must be taken into account, 
        self.y = SCREEN_HEIGHT - FLOOR_OFFSET
        if(self.is_jumping):
            self.y -= (PET_SIZE*1.6)
        else:
            self.y -= (PET_SIZE*1.3)
        self.vy = 0 
        self.vx = 0 # Horizontal movement should also stop

    def add_gravity(self):
        # Simulate gravity 
        if not self.is_on_floor or self.is_jumping:
            self.vy += 1 

    def jump(self, direction):
        # Negative y means pet moves up
        self.vy = -20
        self.vx = 2 if direction == 'right' else -2  # Apply horizontal movement for more natural jump
        self.is_jumping = True

    def get_position(self):
        return self.x, self.y
