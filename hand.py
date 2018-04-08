class Hand():

    def __init__(self,cards):

        self.cards = cards
        self.value = self.cards_value()
        self.has_ace = self.ace_check()
    
    def __str__(self):

        return str([str(card) for card in self.cards])

    def cards_value(self):

        val = 0
        for card in self.cards:
            val += card.value
        if val > 21:
            for card in self.cards:
                if card.ace == True:
                    card.ace = False
                    card.value -= 10
                    val -= 10
                    self.has_ace = self.ace_check()
                    break
        return val

    def ace_check(self):
        for card in self.cards:
            if card.ace == True:
                return True
            else:
                return False