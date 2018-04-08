import string

class Card():
    '''Card object containing suit, value, face and ace-boolean'''

    def __init__(self,suit,value):

        self.suit = suit
        self.ace = False
        self.face = value

        if value[0] not in string.ascii_letters:
            self.value = int(value)
        elif value == 'Jack' or value == 'Queen' or value == 'King':
            self.value = 10
        elif value == 'Ace':
            self.value = 11
            self.ace = True

    def __str__(self):
        return '{} {}'.format(self.suit,self.face)

