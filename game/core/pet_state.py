
class PetState:
    MAX_HAPPINESS = 100
    FEED_BOOST = 20
    PLAY_BOOST = 10
    HUNGER_DECREMENT = -10
    BORED_DECREMENT = -5

    def __init__(self):
        self.happiness = self.MAX_HAPPINESS
        self.is_alive = True
        self.hunger_timer = 0
        self.is_feeding = False
        self.is_playing = False

    def feed(self):
        if(not self.is_feeding and not(self.happiness <= self.MAX_HAPPINESS-self.FEED_BOOST)):
            self.is_feeding = True
            self.hunger_timer = 0

    def finish_eating(self):
        self.happiness += self.FEED_BOOST
        self.is_feeding = False

    def update(self):
        # Below lines are temporary j to test!!!!!!
        if(self.hunger_timer % 100 == 0 and self.happiness >= 0):
            print("happiness: ",self.happiness)
        if(self.happiness == 0):
            # only print once
            print("Cat died!")
            self.happiness-=1
        # Temp lines end here
            
        if(not self.is_feeding):
            self.hunger_timer += 1

        if(self.hunger_timer % 100 == 0):
            self.happiness += self.HUNGER_DECREMENT
        
        if(self.happiness <= 0):
            self.is_alive = False
