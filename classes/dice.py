from random import randint

class Dice:
    """Class for all Dice instances"""

    def __int__(self, sides):
        """Initilize attributes for a Dice Class"""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 to 6"""
        self.sides = 6
        print(randint(1, self.sides))

roll_1 = Dice()
"""Roll a dice 20 times"""
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()