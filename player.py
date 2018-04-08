from hand import Hand

class Player():

    def __init__(self,cards):

        self.hand = Hand(cards)
        self.money = 100

    def hit(self,card):
        
        self.hand.cards.append(card)
        self.hand.value = self.hand.cards_value()
        self.show_hand()

    def bet(self,value):
        if value <= self.money:
            self.money -= value
            return value
        else:
            return None

    def show_hand(self):
        print 'You have:'
        for card in self.hand.cards:
            print str(card) +',',
    
    def new_hand(self, cards):
        self.hand = Hand(cards)