import random

from card import Card

class Deck():
    '''List of 52 card objects in randomized order'''

    suits = ['Clubs', 'Spades','Hearts','Diamonds']
    values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

    def __init__(self):

        self.deck = []
        for s in Deck.suits:
            for v in Deck.values:
                self.deck.append(Card(s,v))
        random.shuffle(self.deck)

    def deal_card(self):
        '''Returns random card object'''

        return self.deck.pop()

    def deal_hand(self):
        '''Returns starting hand of two cards in list'''

        return [self.deck.pop(),self.deck.pop()]

    def __len__(self):
        '''Returns cards in deck for debugging purposes'''
        return len(self.deck)
