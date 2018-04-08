import sys

from deck import Deck
from player import Player
from dealer import Dealer

class Blackjack():

    def __init__(self):

        self.deck = Deck()
        self.player = Player(self.deck.deal_hand())
        self.dealer = Dealer(self.deck.deal_hand())
        self.money_on_table = 0

    def betting_fase(self):

        if self.player.money <= 0:
            print 'You are broke, go home!'
            sys.exit()

        print 'You have ${}'.format(self.player.money)
        print 'How much do you want to bet?'
        while True:
            bet = raw_input()
            try:
                bet = int(bet)
                if bet <= self.player.money:
                    break
                else:
                    print 'You do not have that cash! Try again'
            except ValueError:
                print 'Invalid input, try again!'

        self.money_on_table = self.player.bet(bet)

        print 'you bet ${}'.format(self.money_on_table)

    def player_fase(self):

        if self.player.hand.value == 21:
            print 'Blackjack!'
            return None
        
        self.dealer.show_one()

        while self.player.hand.value < 21:
            self.player.show_hand()
            print 'Do you want another card?'
            answer = raw_input().lower()
            if answer == 'y':
                self.player.hit(self.deck.deal_card())
            elif answer == 'n':
                break
            else:
                print 'I do not understand, please try again'
                continue
        
        if self.player.hand.value > 21:
            print 'You are busted!'
            self.player.hand.value = 0
        else:
            print 'You ended your turn with {} points'.format(self.player.hand.value)
    
    def dealer_fase(self):
        
        self.dealer.show_hand()
        if self.dealer.hand.value == 21:
            print 'Dealer has blackjack!'
        
        while self.dealer.hand.value <= 17:
            if self.dealer.hand.value < 17:
                self.dealer.hit(self.deck.deal_card())
            elif self.dealer.hand.value == 17 and self.dealer.hand.has_ace:
                self.dealer.hit(self.deck.deal_card())
                self.dealer.hand.has_ace = self.dealer.hand.ace_check()
            else:
                break

        if self.dealer.hand.value > 21:
            print 'Dealer has busted!'
            self.dealer.hand.value = 0       
                  
    def end_fase(self):
        '''Checks if the player won and pays'''
        if self.player.hand.value > self.dealer.hand.value:
            print 'You won and made {} dollar!'.format(self.money_on_table)
            self.player.money += (self.money_on_table)*2
        else:
            print 'You have lost {} dollar'.format(self.money_on_table)

    def reset(self):
        '''Resets the deck, money on table and deals new cards. Player money is saved'''
        self.deck = Deck()
        self.player.new_hand(self.deck.deal_hand())
        self.dealer.new_hand(self.deck.deal_hand())
        self.money_on_table = 0

