from player import Player
from dealer import Dealer
from deck import Deck

class Game(object):

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer

    def deal_everyone(self):
        self.player.hand = self.dealer.deal()
        self.dealer.hand = self.dealer.deal()

    def play_hand(self):
        #First, update the points for player and dealer and reset double to False
        self.player.sum_points()
        self.dealer.sum_points()
        double = 0

        #Checks for a player Blackjack and returns the winner
        if self.player.points == 21:
            #Natural Black jack pays out immediatly unless dealer also had blackjack
            if self.dealer.points < 21:
                #player win
                self.print_hands()
                return 'Blackjack', double
            elif self.dealer.points == 21:
                #Dealer and player Blackjack results in Push
                self.print_hands()
                return 'Push', double
        else:
            #play normal, no blackjack
            self.player.play(self.dealer)
            # if the player has doubled sets double to true
            if self.player.double:
                    self.player.double = False
                    double = 1
            #Check for player bust
            if self.player.points <= 21:
                #No bust, Dealer plays
                self.dealer.play()
                self.print_hands()
                #If dealer busts or player points higher, player wins
                if self.dealer.points > 21 or self.player.points > self.dealer.points:
                    return 'Player', double
                #Tie - Push
                elif self.dealer.points == self.player.points:
                    return  'Push', double
                #Dealer wins
                else:
                    return 'Dealer', double
            else:
                #player busts
                self.print_hands()
                return 'Dealer', double
            self.print_hands()
            self.dealer.shoe.check_shuffle()


    def print_hands(self):
        # Helper function to visualize player and dealer hands
        print(self.player.hand)
        print(self.dealer.hand)
        print("----------")

def play_round(game):
    game.deal_everyone()
    game.print_hands()
    winner, double = game.play_hand()
    print(winner+'\n')

if __name__ == "__main__":
    deck = Deck(num_decks=7)
    dealer = Dealer(deck)
    player = Player(basic_strategy=True)
    game = Game(player, dealer)

    for _ in range(10):
        play_round(game)
