from player import Player
from dealer import Dealer
from deck import Deck

class Game(object):

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer

    def deal_everyone(self):
        self.player.hand = dealer.deal()
        self.dealer.hand = dealer.deal()

    def play_hand(self):
        if self.player.sum_points()[0] == 21:
            #Natural Black jack pays out immediatly unless dealer also had blackjack
            if self.dealer.sum_points()[0] < 21:
                #player win
                self.print_hands()
                return 'Player'
            elif self.dealer.sum_points()[0] == 21:
                #Player push
                self.print_hands()
                return 'Push'
        else:
            #play normal no blackjack
            self.player.play_like_dealer(self.dealer)
            if self.player.points <= 21:
                self.dealer.play()
                self.print_hands()
                if dealer.points > 21 or player.points > dealer.points:
                    return 'Player'
                elif dealer.points == player.points:
                    return  'Push'
                else:
                    return 'Dealer'
            else:
                self.print_hands()
                return 'Dealer'
            self.print_hands()


    def print_hands(self):
        print(self.player.hand)
        print(self.dealer.hand)
        print("----------")

def play_round(game):
    game.deal_everyone()
    game.print_hands()
    print(game.play_hand()+'\n')

if __name__ == "__main__":
    deck = Deck(num_decks=7)
    dealer = Dealer(deck)
    player = Player()
    game = Game(player, dealer)

    for _ in range(10):
        play_round(game)
