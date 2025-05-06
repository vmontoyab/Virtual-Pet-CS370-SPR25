class PetState:
    MAX_HAPPINESS = 100
    FEED_BOOST = 5  # Changed from 20 to 5
    PLAY_BOOST = 10
    HUNGER_DECREMENT = -1
    BORED_DECREMENT = -5
    HUNGER_TIMER_MAX = 600
    FEEDING_DURATION = 180  # 3 seconds at 60fps

    def __init__(self):
        self.happiness = 75  # Start at 75 instead of MAX_HAPPINESS
        self.is_alive = True
        self.sad = False
        self.super_happy = True
        self.hunger_timer = 0
        self.is_feeding = False
        self.feeding_timer = 0  # New timer for feeding duration
        self.is_playing = False
        self.last_printed_happiness = 75  # Match initial happiness

    def feed(self):
        # Only start feeding if not already feeding
        if not self.is_feeding:
            print("Starting feeding sequence (3 seconds)")
            self.is_feeding = True
            self.hunger_timer = 0
            self.feeding_timer = 0  # Reset feeding timer
            # Don't call finish_eating() immediately anymore

    def finish_eating(self):
        self.happiness += self.FEED_BOOST
        self.is_feeding = False
        print(f"Feeding complete! Happiness increased by {self.FEED_BOOST}")

    #need to make these two methods affect cat actions loaded (sad and happpy in cat_animations)
    def is_sad(self):
        if(self.happiness < self.MAX_HAPPINESS/2):
            self.sad = True

    def is_super_happy(self):
        if(self.happiness == self.MAX_HAPPINESS or self.happiness >= self.MAX_HAPPINESS -10):
            self.super_happy = True

    def update(self):
        # Track happiness for printing
        old_happiness = self.happiness
            
        # Update feeding timer if currently feeding
        if self.is_feeding:
            self.feeding_timer += 1
            # After 3 seconds (180 frames), finish eating
            if self.feeding_timer >= self.FEEDING_DURATION:
                self.finish_eating()
        else:
            self.hunger_timer += 1

        # Decrease happiness less frequently and by smaller amounts
        if(self.hunger_timer >= self.HUNGER_TIMER_MAX):
            self.happiness += self.HUNGER_DECREMENT
            self.hunger_timer = 0  # Reset timer after decrementing
        
        # Only print when happiness reaches a new multiple of 5
        current_multiple = self.happiness - (self.happiness % 5)
        last_multiple = self.last_printed_happiness - (self.last_printed_happiness % 5)
        if current_multiple != last_multiple and self.happiness >= 0:
            print(f"Happiness: {current_multiple}")
            self.last_printed_happiness = self.happiness
            
        if(self.happiness == 0):
            # only print once
            print("Cat died!")
            self.happiness -= 1
        
        if(self.happiness <= 0):
            self.is_alive = False
