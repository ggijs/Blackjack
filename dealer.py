from hand import Hand

class Dealer():

    def __init__(self,cards):

        self.hand = Hand(cards)

    def hit(self,card):
        
        self.hand.cards.append(card)
        self.hand.value = self.hand.cards_value()
        self.show_hand()

    def show_one(self):
        print str(self.hand.cards[0]) + ' and another card'

    def show_hand(self):
        print 'The dealer has:'
        for card in self.hand.cards:
            print str(card) +',',
    
    def new_hand(self, cards):
        self.hand = Hand(cards)