import random

class Coin(object):

    def __init__(self):
        self.sideup = 'Heads'

    def __str__(self):
        return 'Current state : {}'.format(self.sideup)
    
    def flip(self):
        self.sideup = random.choice(["Heads", "Tails"])
    def getstate(self):
        return self.sideup