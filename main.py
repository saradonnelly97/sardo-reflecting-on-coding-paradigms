#Setting up the initial Podracer class with max_speed, condition, and price attributes
class Podracer: 
    def __init__ (self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price 
#Setting up a repair method that will update condition of Podracer to 'repaired'
    def repaired(self):
        self.condition = "repaired"

#Ani's Podracer to inherit (super) Podracer class attributes; also contains a speed booster!
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
    def boost(self):
        self.max_speed *= 2

#We aren't too sure how this happened, but Sebulba's Podracer is absolutely trashed now, so we're setting the condition as such.
class SebulbasPod(Podracer):
    def __init__(max_speed, condition, price):
        super.init(max_speed, condition, price)
    def flame_jet(self, other_pod):
        other_pod.condition = "trashed"