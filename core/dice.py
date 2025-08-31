import random
class Dice:
    def __init__(self):
        self.value1 = None
        self.value2 = None
        self.doubles = False

    def roll(self):
        self.doubles = False
        self.value1 = random.randint(1, 6)
        self.value2 = random.randint(1, 6)
        if self.value1 == self.value2:
            self.doubles = True
        return (self.value1, self.value2)
    
    def get_values(self):
        return self.value1, self.value2
    
    def is_double(self):
        return self.doubles