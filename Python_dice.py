import random
class Dice:
    def roll(self):
        x = random.randint(1,6)
        y = random.randint(1,6)
        return (x,y)
dice = Dice()
print(dice.roll())
# This Excercise is to generate dice roll as a tuple 
    
