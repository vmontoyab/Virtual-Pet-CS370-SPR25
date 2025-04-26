class Motion:
    SIZE = 64
    FLOOR_OFFSET = 50
    WALL_OFFSET = 100
    JUMP_SPEED = -20
    GRAVITY = 1

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.x = screen_width // 2 - Motion.SIZE // 2
        self.y = (screen_height - Motion.FLOOR_OFFSET) - Motion.SIZE

        self.speed_x = 0
        self.speed_y = 0
        self.jumping = False
    
    def change_direction(self):
        self.speed_x *= -1

    def check_wall_collision(self):
        flip = False
        if self.x < Motion.WALL_OFFSET:
            self.x = Motion.WALL_OFFSET
            flip = "right"
        elif self.x + Motion.SIZE > self.screen_width - Motion.WALL_OFFSET:
            self.x = self.screen_width - Motion.WALL_OFFSET - Motion.SIZE
            flip = "left"
        return flip
    
    def add_gravity(self):
        if self.jumping:
            self.speed_y += Motion.GRAVITY
    
    def is_on_floor(self):
        floor = self.screen_height - Motion.FLOOR_OFFSET - Motion.SIZE
        return self.y >= floor

    def snap_to_floor(self):
        self.y = self.screen_height - Motion.FLOOR_OFFSET - Motion.SIZE*1.5
        self.speed_y = 0
        self.jumping = False

    def idle(self,):
        if(self.y):
            self.speed_x = 0
            self.y = self.screen_height - Motion.FLOOR_OFFSET - Motion.SIZE*1.5

    def walk(self, direction):
        self.speed_x = 1 if direction == "right" else -1
        self.speed_y = 0

    def jump(self, direction):
        self.jumping = True
        self.speed_y = Motion.JUMP_SPEED
        self.speed_x += 2 if direction == "right" else -2

    def update_position(self):
        self.x += self.speed_x
        self.y += self.speed_y

