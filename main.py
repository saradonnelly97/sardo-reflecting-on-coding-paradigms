# Setting up the initial Podracer class with max_speed, condition, and price attributes
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Setting up a repair method that will update condition of Podracer to 'repaired'
    def repaired(self):
        self.condition = "repaired"


# Ani's Podracer to inherit (super) Podracer class attributes; also contains a speed booster!
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2


# We aren't too sure how this happened, but Sebulba's Podracer is absolutely trashed now, so we're setting the condition as such.
class SebulbasPod(Podracer):
    def __init__(max_speed, condition, price):
        super.init(max_speed, condition, price)

    def flame_jet(self, other_pod):
        other_pod.condition = "trashed"



'''
Make sure to answer the following prompts about your coding experience:

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
-Encapsulation is used while the classes encapsulate their attributes of max_speed, condition, and price; as well as their methods repair, boost, and flame_jet.
-Inheritance is used as AnakinsPod and SebulbasPod inherit their attributes and methods from the initial Podracer class.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
If there had been rock-solid data involved, Functional programming may have been the way to go. However, the podracer objects had unique encapsulated attributes and behaviors that OOP was much more suited to modeling.

How in particular did Object Oriented Programming assist in the solving of this problem?
OOP was more suited for modeling the podracer objects, handling encapsulated attributes, and defining their behaviors.
'''