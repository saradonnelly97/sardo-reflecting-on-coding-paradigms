class Podracer: 
    def __init__ (self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price 

    def repaired(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


    