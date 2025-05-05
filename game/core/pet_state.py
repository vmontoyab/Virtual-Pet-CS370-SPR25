class PetState:
    MAX_HAPPINESS = 100
    FEED_BOOST = 20
    PLAY_BOOST = 10
    HUNGER_DECREMENT = -1  # Reduce from -10 to -1
    BORED_DECREMENT = -5
    HUNGER_TIMER_MAX = 600  # New constant: 10 seconds at 60 FPS

    def __init__(self):
        self.happiness = self.MAX_HAPPINESS
        self.is_alive = True
        self.hunger_timer = 0
        self.is_feeding = False
        self.is_playing = False
        self.last_printed_happiness = self.MAX_HAPPINESS  # Track last printed value

    def feed(self):
        if(not self.is_feeding and not(self.happiness <= self.MAX_HAPPINESS-self.FEED_BOOST)):
            self.is_feeding = True
            self.hunger_timer = 0

    def finish_eating(self):
        self.happiness += self.FEED_BOOST
        self.is_feeding = False

    def update(self):
        # Track happiness for printing
        old_happiness = self.happiness
            
        if(not self.is_feeding):
            self.hunger_timer += 1

        # Decrease happiness less frequently and by smaller amounts
        if(self.hunger_timer >= self.HUNGER_TIMER_MAX):
            self.happiness += self.HUNGER_DECREMENT
            self.hunger_timer = 0  # Reset timer after decrementing
        
        # Only print when happiness reaches a new multiple of 5
        current_multiple = self.happiness - (self.happiness % 5)
        last_multiple = self.last_printed_happiness - (self.last_printed_happiness % 5)
        if current_multiple != last_multiple and self.happiness >= 0:
            print("happiness: ", current_multiple)
            self.last_printed_happiness = self.happiness
            
        if(self.happiness == 0):
            # only print once
            print("Cat died!")
            self.happiness -= 1
        
        if(self.happiness <= 0):
            self.is_alive = False
