from game import Blackjack

def main():
    game = Blackjack()

    while True:
        game.betting_fase()
        game.player_fase()
        if game.player.hand.value > 0 and game.player.hand.value != 21:
            game.dealer_fase()
        game.end_fase()

        print 'Do you want to keep playing? y/n'
        answer = raw_input().lower()
        if answer == 'y':
            game.reset()
        else:
            break

if __name__ == "__main__":
    main()