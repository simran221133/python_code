from random import choice

class Lottery:

    def __init__(self, characters=[1, 2, 3, 4, 5, 6, 7 , 8, 9, 0, 'f', 'g', 'k', 'c', 'b']):
        self.characters = characters

    def lottery_number(self):

    #characters=[1, 2, 3, 4, 5, 6, 7 , 8, 9, 0, 'f', 'g', 'k', 'c', 'b']
        test = []

        for i in self.characters:
            char = choice(self.characters)
            char = str(char)
            if len(test) < 4:
                test.append(char) 
            else:
                test
        str1 = ''

#        print(str1.join(test))
        if (str1.join(test)) == "576f":
            print("You won the lottery")
        else:
            print("Better luck next time!")

    def lottery_analysis(self):
        counter = 0
        lottery_2 = Lottery()
        if lottery_2.lottery_number() == "You won the lottery":
            counter += 1
        else:
            print(counter)

lottery_1 = Lottery()
lottery_1.lottery_number()
lottery_1.lottery_analysis()